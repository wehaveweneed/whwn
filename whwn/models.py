from annoying.functions import get_object_or_None
from copy import deepcopy

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models
from django.db.models.signals import pre_delete
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from whwn.util.models import TimestampedModel, LocatableModel


class Item(TimestampedModel, LocatableModel):
    """An item represents a quantity of an object. The object type is
    determined by the sku association. Items can be held by both Teams
    and Users. Generally, items can only be passed within a single team.
    """
    sku = models.ForeignKey('whwn.SKU')
    quantity = models.PositiveIntegerField(default=1, blank=True)
    requested = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True)
    holder = generic.GenericForeignKey()

def Item_pre_delete(sender, instance, **kwargs):
    if instance.quantity > 0:
        raise Exception("Item has a positive quantity, and should not be",
                "deleted.")

pre_delete.connect(Item_pre_delete, sender=Item)

class SKU(TimestampedModel):
    upc = models.CharField(null=True, blank=True, max_length=54)
    team = models.ForeignKey('whwn.Team')
    name = models.CharField(max_length=64)
    category = models.ForeignKey('whwn.Category', null=True, blank=True)

    def save(self, *args, **kwargs):
        """Generate a UPC on create."""
        # TODO: Look into using python-barcode instead of uuid
        if self.__is_persisted() is False:
            import uuid; self.upc = str(uuid.uuid4())
        return super(SKU, self).save(*args, **kwargs)

    def __is_persisted(self):
        """Check if object has persisted."""
        if self.pk:
            return True
        else:
            return False


class Category(models.Model):
    """Categories are used to sort items into logical groups"""
    name = models.CharField(max_length=32)

    def items(self):
        """
        Return a list of item names in this category.
        """
        items = [sku.item_set.all() for sku in self.sku_set.all()]
        return reduce(lambda x,y: x+y, items)


class Message(TimestampedModel):
    """Keeps track of conversation between the system and users"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    contents = models.TextField(default='')
    flagged = models.BooleanField(default=False)
    team = models.ForeignKey('whwn.Team')

    def save(self, *args, **kwargs):
        """Set team to be author's team if not provided."""
        if self.team is None:
            self.team = self.author.team
        return super(Message, self).save(*args, **kwargs)

class Team(TimestampedModel, LocatableModel):
    """A collection of users. Used to indicate a group that
    shares a common ground for interaction."""
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    items = generic.GenericRelation('whwn.Item')


class Membership(TimestampedModel):
    user = models.ForeignKey('whwn.User', related_name="memberships")
    team = models.ForeignKey('whwn.Team', related_name="memberships")
    is_admin = models.BooleanField(default=False)
    read_only = models.BooleanField(default=False)

    class Meta:
        unique_together = ("user", "team")


class User(AbstractUser, TimestampedModel, LocatableModel):
    """This is our user class. Reference Django 1.5's AbstractUser for the
    complete picture of what a User object is capable of."""
    phone_number = models.CharField(max_length=32, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    items = generic.GenericRelation('whwn.Item')

    def join_team(self, team):
        """
        Join a team

        :param team: team that the user is associated with
        :type team: whwn.Team
        :returns: New Membership
        """
        m = Membership.objects.create(user=self, team=team)
        m.save()
        if m.pk:
            return None
        else:
            raise Exception("Joining team failed. Check that your arguments are as expected.")

    def leave_team(self, team):
        """
        Leave a team

        :param team: team that the user is leaving from.
        :type team: whwn.Team
        :returns: None
        """
        m = get_object_or_None(Membership, user=self, team=team)
        if m is None:
            raise Exception("The user cannot leave a team of which he is not",
                    "already a member.")
        else:
            m.delete()
            return None

    def teams(self):
        """
        Return QuerySet of teams
        """

        return Team.objects.filter(memberships__user=self)
    teams = property(teams)

    def checkout_item(self, item, quantity=-1):
        """
        Checkout a `quantity` of an item. Should be called when a user is
        taking items from the common inventory. Due to not being able to
        define a default value for `quantity` to item.quantity, a negative
        quantity will logically be equivalent to all
        items rather than no items.

        :param item: item to checkout
        :type quantity: whwn.Item
        :param quantity: amount to checkout
        :type quantity: integer
        """
        # TODO: Discuss the return type for this method.
        return self.give_item(self, item, quantity)

    def checkin_item(self, item, quantity=-1):
        """
        Checkin a `quantity` of an item. Should be called when a user is
        putting items back into the common inventory.

        :param item: item to checkout
        :type quantity: whwn.Item
        :param quantity: amount to checkin
        :type quantity: integer
        """
        # TODO: Discuss the return type of this method.
        return self.give_item(self.team, item, quantity)

    def give_item(self, recipient, item, quantity=-1):
        """
        Give a `quantity` of an `item` to a `recipient`. The `recipient`
        must be in the same team as the current user.

        :param recipient: user to give items to.
        :type recipient: whwn.User or whwn.Team
        :param item: item to checkout
        :type item: whwn.Item
        :param quantity: amount to give
        :type quantity: integer
        :returns: Item tuple (Item on Sender, Item on Reciever)
        """
        # TODO: Discuss the return type of this method.

        # If provided quantity is negative, we define it as being all items in
        # this transaction
        if quantity < 0:
            quantity = item.quantity

        # If available quantity is less than requested, we raise an exception.
        if item.quantity < quantity:
            raise Exception("Requested quantity to checkin is over the quantity"
                                " available.")

        # If quantity is the same as the item quantity we just edit the holder value
        # to the new recipient.
        if quantity == item.quantity:
            holder_type = ContentType.objects.get_for_model(recipient)
            existing = get_object_or_None(Item, content_type__pk=holder_type.id, object_id=recipient.id)

            if existing is not None:
                existing.quantity = existing.quantity + quantity
                existing.save()
                item.quantity = 0
                item.save()
                return (None, existing)
            else:
                item.holder = recipient
                item.save()
                return (None, item)

        # Else we do the math.
        else:
            # We first subtract the quantity from the item.
            item.quantity = item.quantity - quantity
            item.save()

            holder_type = ContentType.objects.get_for_model(recipient)
            existing = get_object_or_None(Item, content_type__pk=holder_type.id, object_id=recipient.id)

            if existing is not None:
                existing.quantity = existing.quantity + quantity
                existing.save()
                return (item, existing)
            else:
                # We deepcopy the item so we can return it.
                tmp = deepcopy(item)

                # Changing the pk allows us to create a new db entry on save.
                item.pk = None
                item.quantity = quantity
                item.holder = recipient
                item.save()
                return (tmp, item)

    def send_message_str(self, team, string):
        """
        Send a `string` to the team as a Message.

        :param message: message to send to teh team
        :type message: String
        """
        m = get_object_or_None(Membership, team=team, user=self)
        if m:
            msg = Message(author=self, contents=string, team=m.team)
            msg.save()
            if msg.pk:
                return msg
            raise Exception("Error saving message.")
        else:
            raise Exception("This user is not a member of the intended recipient",
                    "team.")

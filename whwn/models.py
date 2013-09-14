from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
import datetime


# Abstract classes that are used by our models

class Timestamps(models.Model):
    """
    Used to attach *created at* and *updated at* timestamps for any model class
    that mixes this in.
    """
    created_at = models.DateTimeField(auto_now_add=True,
                                        default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True,
                                        default=datetime.datetime.now)
    class Meta:
        abstract = True


class Locatable(models.Model):
    """
    Give *latitude* and *longitude* properties to any model that mixes
    this in
    """
    latitude = models.DecimalField(max_digits=8, decimal_places=3, null=True,
                                    blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=3, null=True,
                                    blank=True)
    def _get_point(self):
        if self.latitude and self.longitude:
            return Point(self.longitude, self.latitude)
        else:
            return Point(0, 0)
    def _set_point(self, point):
        self.latitude = point.y
        self.longitude = point.x
        self.save()
    point = property(_get_point, _set_point)
    class Meta:
        abstract = True

# Models

class Item(Timestamps, Locatable):
    """
    An item represents a quantity of objects (an object is represented by a SKU)
    """
    sku = models.ForeignKey('whwn.SKU')
    quantity = models.PositiveIntegerField()
    requested = models.BooleanField(default=False)
    possessor = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,
                                    blank=True)


class SKU(Timestamps):
    """Stock Keeping Unit."""
    upc = models.CharField(null=True, blank=True, max_length=54)
    team = models.ForeignKey('whwn.Team')
    name = models.CharField(max_length=64)


class Category(models.Model):
    """Categorize items"""
    name = models.CharField(max_length=32)

    def item_names(self):
        """
        Return a unique list of item names in this category.
        """


class Message(Timestamps):
    """Keeps track of conversation between the system and users"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    contents = models.TextField(default='')
    flagged = models.BooleanField(default=False)
    team = models.ForeignKey('whwn.Team')
    

class Team(Timestamps, Locatable):
    """A collection of users. Used to indicate a group that
    shares a common ground for interaction."""
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="owner",
                                null=True)



class User(AbstractUser, Timestamps, Locatable):
    """
    This is our user class. Reference Django 1.5's AbstractUser for the
    complete picture of what a User object is capable of.
    """
    phone_number = models.CharField(max_length=32, blank=True, null=True)
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    team = models.ForeignKey('whwn.Team')

    def change_team(self, team):
        """
        Leave current team for a new `team`

        :param team: team that the user is associated with
        :type team: whwn.Team
        """
        raise NotImplementedError

    def checkout_item(self, quantity, item):
        """
        Checkout a `quantity` of an item. Should be called when a user is
        taking items from the common inventory.

        :param quantity: amount to checkout
        :type quantity: integer
        :param item: item to checkout
        :type quantity: whwn.Item
        """
        raise NotImplementedError

    def checkin_item(self, quantity, item):
        """
        Checkin a `quantity` of an item. Should be called when a user is
        putting items back into the common inventory.

        :param quantity: amount to checkin
        :type quantity: integer
        :param item: item to checkout
        :type quantity: whwn.Item
        """
        raise NotImplementedError

    def give_item(self, quantity, item, recipient):
        """
        Give a `quantity` of an `item` to a `recipient`. The `recipient`
        must be in the same team as the current user.

        :param quantity: amount to checkin
        :type quantity: integer
        :param item: item to checkout
        :type quantity: whwn.Item
        """
        raise NotImplementedError

    def _get_items(self):
        """
        Current list of items this user has in his possession.
        """
        raise NotImplementedError
    items = property(_get_items)

    def send_message(self, message):
        """
        Send a `message` to the team.

        :param message: message to send to teh team
        :type message: whwn.Message
        """
        raise NotImplementedError
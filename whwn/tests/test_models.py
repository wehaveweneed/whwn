from django.test import TestCase
from model_mommy import mommy


class UserTestCase(TestCase):

    def setUp(self):
        self.team_a = mommy.make('whwn.Team', name="Team A")
        self.team_b = mommy.make('whwn.Team', name="Team B")
        self.user_a = mommy.make('whwn.User', team=self.team_a)
        self.user_b = mommy.make('whwn.User', team=self.team_b)
        self.user_b2 = mommy.make('whwn.User', team=self.team_b)
        self.item_a = mommy.make('whwn.Item', holder=self.team_a, quantity=5)
        self.item_b = mommy.make('whwn.Item', quantity=1, holder=self.user_b)
        self.sku_a = mommy.make('whwn.SKU')

    def test_change_team(self):
        self.user_a.change_team(self.team_b)
        self.assertEqual(self.user_a.team, self.team_b)

    def test_checkout_item(self):
        self.user_a.checkout_item(self.item_a)
        skus = [i.sku for i in self.user_a.items]
        self.assertIn(self.item_a.sku, skus)

        item = mommy.make('whwn.Item', holder=self.team_a, quantity=10)
        self.user_a.checkout_item(item, quantity=4)
        skus = [i.sku for i in self.user_a.items]
        self.assertIn(item.sku, skus)
        skus = [i.sku for i in self.team_a.items]
        self.assertIn(item.sku, skus)

        x = self.user_a.items.get(object_id=item.id,
                        content_object=ContentType.objects.get_for_model(item))
        assertEqual(x.quantity, 4)
        assertEqual(item.quantity, 6)


    def test_checkin_item(self):
        self.user_b.checkin_item(self.item_b)
        self.assertEqual(self.item_b.holder, self.team_b)

    def test_give_item(self):
        self.user_b.give_item(1, self.item_b, self.user_b2)
        self.assertEqual(self.item_b.holder, self.user_b2)

    def test_send_message_string(self):
        message = self.user_a.send_message("Test message!")
        self.assertIn(message, self.team_a.message_set)


class CategoryTestCase(TestCase):

    def setUp(self):
        self.cat_a = mommy.make('whwn.Category')
        self.sku = mommy.make('whwn.SKU', category=self.cat_a)
        self.item_a = mommy.make('whwn.Item', sku=self.sku)
        self.item_b = mommy.make('whwn.Item', sku=self.sku)
        self.item_c = mommy.make('whwn.Item', sku=self.sku)

    def test_get_items(self):
        items = self.cat_a.items()
        assertIn(self.item_a, items)
        assertIn(self.item_b, items)
        assertIn(self.item_c, items)

class SKUTestCase(TestCase):

    def test_upc_on_create(self):
        sku = mommy.make('whwn.SKU')
        self.assertIsNotNone(sku.upc)

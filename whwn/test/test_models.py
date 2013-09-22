from django.test import TestCase
from model_mommy import Mommy


class UserTestCase(TestCase):

    def setUp(self):
        self.team_a = mommy.make('whwn.Team', name="Team A")
        self.team_b = mommy.make('whwn.Team', name="Team B")
        self.user_a = mommy.make('whwn.User', team=self.team_a)
        self.user_b = mommy.make('whwn.User', team=self.team_b)
        self.sku_a = mommy.make('whwn.SKU')
        self.kid = mommy.make('whwn.User')

    def test_change_team(self):
        self.user_a.change_team(self.team_b)
        assertEqual(self.user_a.team, self.team_b)

    def test_checkout_item(self):
        raise NotImplementedError

    def test_checkin_item(self):
        raise NotImplementedError

    def test_give_item(self):
        raise NotImplementedError

    def test_send_message(self):
        raise NotImplementedError

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
        sku = model.make('whwn.SKU')
        self.assertIsNotNone(sku.upc)

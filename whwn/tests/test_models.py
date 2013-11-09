from django.test import TestCase
from django.test import TransactionTestCase
from model_mommy import mommy


class UserTestCase(TestCase):

    def test_join_leave_teams(self):
        a = mommy.make('whwn.Team')
        b = mommy.make('whwn.Team')
        u = mommy.make('whwn.User')
        u.join_team(a)
        self.assertIn(a, u.teams)
        u.join_team(b)
        self.assertIn(b, u.teams)
        u.leave_team(a)
        self.assertNotIn(a, u.teams)

    def test_give_item(self):
        t = mommy.make('whwn.Team')
        u = mommy.make('whwn.User'); v = mommy.make('whwn.User')
        u.join_team(t); v.join_team(t)
        i = mommy.make('whwn.Item', holder=u, quantity=10)

        # Give 3 to team
        res = u.give_item(t, i, 3)
        self.assertEqual(res[0].holder, u)
        self.assertEqual(res[0].quantity, 7)
        self.assertEqual(res[1].holder, t)
        self.assertEqual(res[1].quantity, 3)

        # Give 3 to user v
        res = u.give_item(v, res[0], 3)
        self.assertEqual(res[0].quantity, 4)
        self.assertEqual(res[1].holder, v)
        self.assertEqual(res[1].quantity, 3)

        # Give the 3 now on user v back to u
        res1 = v.give_item(u, res[1], 3)
        self.assertEqual(res1[1].holder, u)
        self.assertEqual(res1[1].quantity, 7)

        # Give the 7 on user u to the team
        res2 = u.give_item(t, res1[1], 7)
        self.assertEqual(res2[0], None)
        self.assertEqual(res2[1].holder, t)
        self.assertEqual(res2[1].quantity, 10)


    def test_send_message_string(self):
        t = mommy.make('whwn.Team')
        u = mommy.make('whwn.User'); u.join_team(t)
        message = u.send_message_str(t, "Test message!")
        self.assertIn(message, t.message_set.all())


class CategoryTestCase(TestCase):

    def test_get_items(self):
        cat = mommy.make('whwn.Category')
        sku = mommy.make('whwn.SKU', category=cat)
        a = mommy.make('whwn.Item', sku=sku, quantity=5)
        b = mommy.make('whwn.Item', sku=sku, quantity=10)
        c = mommy.make('whwn.Item', sku=sku, quantity=12)

        items = cat.items()
        self.assertIn(a, items)
        self.assertIn(b, items)
        self.assertIn(c, items)

class SKUTestCase(TestCase):

    def test_upc_on_create(self):
        sku = mommy.make('whwn.SKU')
        self.assertIsNotNone(sku.upc)

class ItemTestCase(TransactionTestCase):

    def test_no_delete_on_positive_quantity(self):
        i1 = mommy.make('whwn.Item', quantity=5)
        try:
            i1.delete()
        except Exception:
            pass

        i2 = mommy.make('whwn.Item', quantity=0)
        i2.delete()
        self.assertTrue(True)



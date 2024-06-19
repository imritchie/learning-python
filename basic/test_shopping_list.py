import unittest
from shopping_list import ShoppingList


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"Macbook": 14000, "iPhone": 6000, "iPad": 5000})

    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 25000)

# 在 Terminal 中输入： python -m unittest
# .代表通过 F代表失败
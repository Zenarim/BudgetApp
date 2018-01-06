import unittest
from unittest.mock import Mock

from goal import Goal


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.empty_category = Goal()
        self.amazon_category = Goal()
        self.simple_transaction = Mock()
        self.simple_transaction.value = 150.0

    def test_transactions_can_be_added_to_category(self):
        self.amazon_category.add_transaction(self.simple_transaction)

        self.assertEqual(1, self.amazon_category.num_of_transactions)
        self.assertIn(self.simple_transaction, self.amazon_category)

    def test_transactions_can_be_removed_from_category(self):
        another_expense = Mock()
        another_expense.expense = 450.0

        self.amazon_category.add_transaction(self.simple_transaction)
        self.amazon_category.add_transaction(another_expense)

        self.amazon_category.remove_transaction(self.simple_transaction)

        self.assertEqual(1, self.amazon_category.num_of_transactions)
        self.assertNotIn(self.simple_transaction, self.amazon_category)

    def test_get_total_transactions_from_a_category(self):
        self.empty_category.add_transaction(self.simple_transaction)
        self.empty_category.add_transaction(self.simple_transaction)
        self.empty_category.add_transaction(self.simple_transaction)

        self.assertEqual(450, self.empty_category.get_total_transactions())

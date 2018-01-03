import unittest
from unittest.mock import Mock

from category import Category


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.catg = Category()
        self.amazon_category = Category(name='Amazon', goal=1000.0)
        self.simple_transaction = Mock()
        self.simple_transaction.expense = 150.0

    def test_categories_should_have_default_name_uncategorized(self):
        self.assertEqual('Uncategorized', self.catg.name)

    def test_category_can_initialize_name_in_constructor(self):
        expected_name = 'Amazon'
        category = Category(name=expected_name)
        self.assertEqual(expected_name, category.name)

    def test_a_category_has_a_default_goal_of_zero(self):
        self.assertEqual(0.0, self.catg.goal)

    def test_category_can_initialize_goal_in_constructor(self):
        goal = 500.0
        category = Category(goal=goal)
        self.assertEqual(goal, category.goal)

    def test_category_can_set_goal_directly(self):
        goal = 500.0
        self.catg.goal = goal
        self.assertEqual(goal, self.catg.goal)

    def test_transactions_can_be_added_to_category(self):
        self.amazon_category.add_transaction(self.simple_transaction)

        self.assertEqual(1, len(self.amazon_category.transactions))
        self.assertIn(self.simple_transaction, self.amazon_category.transactions)
        self.assertEqual(self.simple_transaction.expense, self.amazon_category.transactions[0].expense)

    def test_category_should_deduct_expense_from_goal_when_added(self):
        self.amazon_category.add_transaction(self.simple_transaction)

        self.assertEqual(850.0, self.amazon_category.get_remaining_balance())

        self.amazon_category.add_transaction(self.simple_transaction)
        self.amazon_category.add_transaction(self.simple_transaction)

        self.assertEqual(450.0, self.amazon_category.get_total_expenses())
        self.assertEqual(550.0, self.amazon_category.get_remaining_balance())

    def test_transactions_can_be_removed_from_category(self):
        another_transaction = Mock()
        another_transaction.expense = 450.0

        self.amazon_category.add_transaction(self.simple_transaction)
        self.amazon_category.add_transaction(another_transaction)

        self.amazon_category.remove_transaction(self.simple_transaction)

        self.assertEqual(1, len(self.amazon_category.transactions))
        self.assertNotIn(self.simple_transaction, self.amazon_category.transactions)


if '__name__' == '__main__':
    unittest.main()
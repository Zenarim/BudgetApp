import unittest
from unittest.mock import Mock

from goal import ExpenseGoal


class TestExpenseCategory(unittest.TestCase):
    def setUp(self):
        self.expense_goal = ExpenseGoal()
        self.amazon_goal = ExpenseGoal(name='Amazon', goal=1000.0)
        self.simple_expense = Mock()
        self.simple_expense.value = 150.0

    def test_expense_goals_should_have_default_name_uncategorized(self):
        self.assertEqual('UncategorizedExpenseGoal', self.expense_goal.name)

    def test_expense_goal_can_initialize_name_in_constructor(self):
        expected_name = 'Amazon'
        goal = ExpenseGoal(name=expected_name)
        self.assertEqual(expected_name, goal.name)

    def test_a_expense_goal_has_a_default_goal_of_zero(self):
        self.assertEqual(0.0, self.expense_goal.goal)

    def test_expense_goal_can_initialize_goal_in_constructor(self):
        goal_value = 500.0
        goal = ExpenseGoal(goal=goal_value)
        self.assertEqual(goal_value, goal.goal)

    def test_expense_goal_can_set_goal_directly(self):
        goal = 500.0
        self.expense_goal.goal = goal
        self.assertEqual(goal, self.expense_goal.goal)

    def test_expense_goal_can_return_total_expenses(self):
        self.amazon_goal.add_transaction(self.simple_expense)
        self.amazon_goal.add_transaction(self.simple_expense)
        self.assertEqual(-300.0, self.amazon_goal.get_total_expenses())

    def test_expense_goal_should_deduct_transactions_from_goal_when_added(self):
        self.amazon_goal.add_transaction(self.simple_expense)

        self.assertEqual(850.0, self.amazon_goal.get_remaining_goal())

        self.amazon_goal.add_transaction(self.simple_expense)
        self.amazon_goal.add_transaction(self.simple_expense)

        self.assertEqual(550.0, self.amazon_goal.get_remaining_goal())


if '__name__' == '__main__':
    unittest.main()

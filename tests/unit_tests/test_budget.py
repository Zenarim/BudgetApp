import unittest
from unittest.mock import Mock

from budget.budget import Budget
from budget.account import ExpenseAccount
from budget.account import AssetAccount


class TestBudgetApp(unittest.TestCase):
    def setUp(self):
        self.expense_account = Mock(spec_set=ExpenseAccount())
        self.expense_account.name = 'Arbitrary Goal'
        self.expense_account.total_spent = 500.0
        self.asset_account = Mock(spec_set=AssetAccount())
        self.asset_account.name = 'Fake Asset'
        self.asset_account.total_deposits = 1000.0
        self.my_budget = Budget()

    def test_can_add_categories_to_budget(self):
        my_budget = Budget()
        my_budget.add_expense_account(self.expense_account)
        self.assertEqual(1, len(my_budget._categories))

    def test_can_remove_category_from_budget(self):
        self.my_budget.add_expense_account(self.expense_account)
        self.my_budget.remove_expense_account("Arbitrary Goal")
        self.assertEqual(0, len(self.my_budget._categories))

    def test_budget_will_have_default_balance_of_zero(self):
        self.assertEqual(0.0, self.my_budget.get_current_balance())

    def test_budget_can_set_default_balance(self):
        starting_balance = 1000.0
        my_budget = Budget(start_balance=self.asset_account)
        self.assertEqual(starting_balance, my_budget.get_current_balance())

    def test_budget_can_return_total_expenses(self):
        self.my_budget.add_expense_account(self.expense_account)
        self.my_budget.add_expense_account(self.expense_account)
        self.my_budget.add_expense_account(self.expense_account)
        self.assertEqual(-1500.0, self.my_budget.get_total_expenses())

    def test_can_add_asset_to_deposit(self):
        self.my_budget.add_asset_account(self.asset_account)
        self.assertEqual(1, len(self.my_budget._assets))

        self.my_budget.add_asset_account(self.asset_account)
        self.my_budget.add_asset_account(self.asset_account)
        self.assertEqual(3, len(self.my_budget._assets))

    def test_can_remove_asset_from_budget(self):
        self.my_budget.add_asset_account(self.asset_account)
        self.my_budget.remove_asset_account('Fake Asset')
        self.assertEqual(0, len(self.my_budget._assets))

    def test_budget_can_return_total_assets(self):
        self.my_budget.add_asset_account(self.asset_account)
        self.my_budget.add_asset_account(self.asset_account)
        self.my_budget.add_asset_account(self.asset_account)
        self.assertEqual(3000.0, self.my_budget.get_total_assets())

    def test_budget_can_return_current_balance(self):
        self.my_budget.add_asset_account(self.asset_account)
        self.my_budget.add_expense_account(self.expense_account)
        self.assertEqual(500.0, self.my_budget.get_current_balance())

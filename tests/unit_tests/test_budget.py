import unittest
from unittest.mock import Mock

from budget_core.budget import Budget
from budget_core.account import ExpenseAccount
from budget_core.account import AssetAccount


class TestBudgetApp(unittest.TestCase):
    def setUp(self):
        self.expense_account = Mock(spec_set=ExpenseAccount())
        self.expense_account.name = 'Arbitrary Goal'
        self.expense_account.account_balance = -500.0
        self.asset_account = Mock(spec_set=AssetAccount())
        self.asset_account.name = 'Fake Asset'
        self.asset_account.account_balance = 1000.0
        self.blank_budget = Budget()

    def test_can_add_account_to_budget(self):
        self.blank_budget.add_account(self.expense_account)
        self.assertEqual(1, len(self.blank_budget._accounts))

    def test_can_remove_account_from_budget(self):
        self.blank_budget.add_account(self.expense_account)
        self.blank_budget.remove_account("Arbitrary Goal")
        self.assertEqual(0, len(self.blank_budget._accounts))

    def test_budget_will_have_default_balance_of_zero(self):
        self.assertEqual(0.0, self.blank_budget.account_balance)

    def test_budget_can_return_total_expenses(self):
        self.blank_budget.add_account(self.expense_account)
        self.blank_budget.add_account(self.expense_account)
        self.blank_budget.add_account(self.expense_account)
        self.assertEqual(-1500.0, self.blank_budget.account_balance)

    def test_can_add_asset_to_deposit(self):
        self.blank_budget.add_account(self.asset_account)
        self.assertEqual(1, len(self.blank_budget._accounts))

        self.blank_budget.add_account(self.asset_account)
        self.blank_budget.add_account(self.asset_account)
        self.assertEqual(3, len(self.blank_budget._accounts))

    def test_can_remove_asset_from_budget(self):
        self.blank_budget.add_account(self.asset_account)
        self.blank_budget.remove_account('Fake Asset')
        self.assertEqual(0, len(self.blank_budget._accounts))

    def test_budget_can_return_total_assets(self):
        self.blank_budget.add_account(self.asset_account)
        self.blank_budget.add_account(self.asset_account)
        self.blank_budget.add_account(self.asset_account)
        self.assertEqual(3000.0, self.blank_budget.account_balance)

    def test_budget_can_return_current_balance(self):
        self.blank_budget.add_account(self.asset_account)
        self.blank_budget.add_account(self.expense_account)
        self.assertEqual(500.0, self.blank_budget.account_balance)

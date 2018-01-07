import unittest

from budget.budget import Budget
from budget.account import AssetAccount
from budget.account import ExpenseAccount


class TestAccountsWithBudget(unittest.TestCase):
    def setUp(self):
        self.simple_budget = Budget()
        self.savings_account = AssetAccount(name='Bank of America')
        self.dine_out_account = ExpenseAccount(name='Dine Out')

        self.paycheck_account = AssetAccount(name='Ding Tai Fung: Waiter')
        self.monthly_rent_account = ExpenseAccount(name='Columbia Apartments')

    def test_add_accounts_to_a_budget(self):
        num_of_accounts = 2

        self.simple_budget.add_account(self.savings_account)
        self.simple_budget.add_account(self.dine_out_account)

        self.assertEqual(num_of_accounts, len(self.simple_budget))
        self.assertIn(self.savings_account, self.simple_budget)
        self.assertIn(self.dine_out_account, self.simple_budget)

    def test_remove_accounts_from_a_budget(self):
        budget_with_one_account = 1
        budget_with_no_accounts = 0

        self.simple_budget.add_account(self.paycheck_account)
        self.simple_budget.add_account(self.monthly_rent_account)

        self.simple_budget.remove_account(self.paycheck_account.name)
        self.assertEqual(budget_with_one_account, len(self.simple_budget))

        self.simple_budget.remove_account(self.monthly_rent_account.name)
        self.assertEqual(budget_with_no_accounts, len(self.simple_budget))

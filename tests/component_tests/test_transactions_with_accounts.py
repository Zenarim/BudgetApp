import unittest
from datetime import date, timedelta

from budget.account import AssetAccount
from budget.account import ExpenseAccount
from budget.transaction import Transaction


class TestTransactionsWithAccounts(unittest.TestCase):
    def setUp(self):
        self.vanguard_retirement_account = AssetAccount(name='Vanguard Retirement')
        self.college_tuition_account = ExpenseAccount(name='State University', spending_limit=24000.0)

        retirement_account_start_date = date.today() - timedelta(days=730)
        self.starting_investment_balance = Transaction(base_value=11000.0, transaction_date=retirement_account_start_date,
                                                       category='Retirement')
        self.ira_contribution = Transaction(base_value=5500.0, transaction_date=date.today(), category='Retirement')
        self.tuition_payment = Transaction(base_value=6000.0, transaction_date=date.today(), category='Education')
        self.tuition_payment_with_grant = Transaction(base_value=6000.0, transaction_date=date.today(),
                                                      category='Education', financial_aid=-3000.0)

    def test_adding_transactions_to_an_asset_account(self):
        self.vanguard_retirement_account.add_transaction(self.starting_investment_balance)
        self.assertEqual(11000.0, self.vanguard_retirement_account.account_balance)

        self.vanguard_retirement_account.add_transaction(self.ira_contribution)
        self.assertEqual(16500.0, self.vanguard_retirement_account.account_balance)

    def test_adding_transactions_to_an_expense_account(self):
        self.college_tuition_account.add_transaction(self.tuition_payment)
        self.assertEqual(-6000.0, self.college_tuition_account.account_balance)

        self.college_tuition_account.add_transaction(self.tuition_payment_with_grant)
        self.assertEqual(-9000.0, self.college_tuition_account.account_balance)

    def test_expense_account_will_return_remaining_limit_for_spending(self):
        self.college_tuition_account.add_transaction(self.tuition_payment_with_grant)
        self.college_tuition_account.add_transaction(self.tuition_payment_with_grant)

        self.assertEqual(18000.0, self.college_tuition_account.remaining_limit)

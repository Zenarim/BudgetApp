import unittest
from unittest.mock import Mock

from budget.account import ExpenseAccount
from budget.transaction import Transaction


class TestExpenseAccount(unittest.TestCase):
    def setUp(self):
        self.blank_expense_account = ExpenseAccount()
        self.amazon_account = ExpenseAccount(name='Amazon', spending_limit=1000.0)
        self.simple_expense = Mock(spec_set=Transaction())
        self.simple_expense.total_value = 150.0

    def test_expense_accounts_should_have_default_name_uncategorized(self):
        self.assertEqual('UncategorizedExpenseAccount', self.blank_expense_account.name)

    def test_expense_account_can_initialize_name_in_constructor(self):
        expected_name = 'Amazon'
        simple_expense_account = ExpenseAccount(name=expected_name)
        self.assertEqual(expected_name, simple_expense_account.name)

    def test_a_expense_account_has_a_default_spending_limit_of_zero(self):
        self.assertEqual(0.0, self.blank_expense_account.spending_limit)

    def test_expense_account_can_initialize_spending_limit_in_constructor(self):
        spending_limit = 500.0
        simple_expense_account = ExpenseAccount(spending_limit=spending_limit)
        self.assertEqual(spending_limit, simple_expense_account.spending_limit)

    def test_expense_account_can_set_spending_limit_directly(self):
        spending_limit = 500.0
        self.blank_expense_account.spending_limit = spending_limit
        self.assertEqual(spending_limit, self.blank_expense_account.spending_limit)

    def test_expense_account_can_return_total_expenses(self):
        self.amazon_account.add_transaction(self.simple_expense)
        self.amazon_account.add_transaction(self.simple_expense)
        self.assertEqual(-300.0, self.amazon_account.total_spent)

    def test_expense_account_should_deduct_transactions_from_spending_limit_when_added(self):
        self.amazon_account.add_transaction(self.simple_expense)

        self.assertEqual(850.0, self.amazon_account.remaining_limit)

        self.amazon_account.add_transaction(self.simple_expense)
        self.amazon_account.add_transaction(self.simple_expense)

        self.assertEqual(550.0, self.amazon_account.remaining_limit)

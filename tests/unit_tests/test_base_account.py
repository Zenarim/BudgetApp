import unittest
from unittest.mock import Mock

from budget_core.account import Account
from budget_core.transaction import Transaction


class TestBaseAccount(unittest.TestCase):
    def setUp(self):
        self.blank_account = Account()
        self.amazon_account = Account()
        self.simple_transaction = Mock(spec_set=Transaction())
        self.simple_transaction.total_value = 150.0

    def test_transactions_can_be_added_to_account(self):
        self.amazon_account.add_transaction(self.simple_transaction)

        self.assertEqual(1, self.amazon_account.num_of_transactions)
        self.assertIn(self.simple_transaction, self.amazon_account)

    def test_transactions_can_be_removed_from_account(self):
        another_expense = Mock()
        another_expense.expense = 450.0

        self.amazon_account.add_transaction(self.simple_transaction)
        self.amazon_account.add_transaction(another_expense)

        self.amazon_account.remove_transaction(self.simple_transaction)

        self.assertEqual(1, self.amazon_account.num_of_transactions)
        self.assertNotIn(self.simple_transaction, self.amazon_account)

    def test_get_total_transactions_from_a_account(self):
        self.blank_account.add_transaction(self.simple_transaction)
        self.blank_account.add_transaction(self.simple_transaction)
        self.blank_account.add_transaction(self.simple_transaction)

        self.assertEqual(450, self.blank_account.get_total_transactions())

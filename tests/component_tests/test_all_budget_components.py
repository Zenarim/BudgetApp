import unittest

from budget_core.budget import Budget
from budget_core.account import ExpenseAccount
from budget_core.account import AssetAccount
from budget_core.transaction import Transaction


class TestBudgetCoreComponents(unittest.TestCase):
    def test_get_current_balance_for_budget(self):
        """
        Will refactor when I write a fixture generator

        Probably didn't need to go this far to test everything, but eh.
        """
        budget_2017 = Budget()
        books_expense_account = ExpenseAccount(name='Books', spending_limit=200.0)
        education_expense_account = ExpenseAccount(name='Education', spending_limit=18000.0)
        groceries_expense_account = ExpenseAccount(name='Groceries', spending_limit=300.0)
        travel_expense_account = ExpenseAccount(name='Gas', spending_limit=960)

        savings_bank_account = AssetAccount(name='Gesa Credit Union')
        checking_bank_account = AssetAccount(name='Bank of America')
        brokerage_fund_account = AssetAccount(name='Fidelity')

        book_001 = Transaction(base_value=30.0, name='How to Read a Book', category=books_expense_account.name)
        book_002 = Transaction(base_value=20.0, name='Learn SQL in 24 Hours', category=books_expense_account.name)

        tuition = Transaction(base_value=2900.0, name='Summer 2017 Tuition', category=education_expense_account.name)
        lab_fee = Transaction(base_value=200.0, name='Lab Fees 2017', category=education_expense_account.name)

        rice = Transaction(base_value=25.0, name='Rice 50 lbs', category=groceries_expense_account.name)
        pork_loin = Transaction(base_value=10.0, name='Pork Loin 2lbs', category=groceries_expense_account.name)
        soda = Transaction(base_value=2.0, name='Pepsi 2L', category=groceries_expense_account.name)

        gas = Transaction(base_value=35.0, name='Gas 3.75 $/Gal', category=travel_expense_account.name)

        monthly_paycheck_savings = Transaction(base_value=3500.0, name='Monthly Deposit',
                                               category=savings_bank_account.name)
        monthly_paycheck_checking = Transaction(base_value=6500.0, name='Monthly Deposit',
                                                category=checking_bank_account.name)
        monthly_investment = Transaction(base_value=1300.0, name='Monthly Investment',
                                         category=brokerage_fund_account.name)

        budget_2017.add_account(books_expense_account)
        budget_2017.add_account(education_expense_account)
        budget_2017.add_account(groceries_expense_account)
        budget_2017.add_account(travel_expense_account)
        budget_2017.add_account(savings_bank_account)
        budget_2017.add_account(checking_bank_account)
        budget_2017.add_account(brokerage_fund_account)

        books_expense_account.add_transaction(book_001)
        books_expense_account.add_transaction(book_002)

        education_expense_account.add_transaction(tuition)
        education_expense_account.add_transaction(lab_fee)

        groceries_expense_account.add_transaction(rice)
        groceries_expense_account.add_transaction(pork_loin)
        groceries_expense_account.add_transaction(soda)

        travel_expense_account.add_transaction(gas)

        savings_bank_account.add_transaction(monthly_paycheck_savings)
        checking_bank_account.add_transaction(monthly_paycheck_checking)
        brokerage_fund_account.add_transaction(monthly_investment)

        self.assertEqual(8078.0, budget_2017.account_balance)

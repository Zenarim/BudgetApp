import unittest
import unittest.mock as umock

from budget import Budget
from goal import ExpenseGoal


class TestBudgetApp(unittest.TestCase):
    def setUp(self):
        self.fake_expense_category = umock.Mock(spec_set=ExpenseGoal())
        self.fake_expense_category.name = 'Fake Category'
        self.fake_expense_category.get_total_expenses = umock.Mock(return_value=500.0)
        self.fake_asset_category = umock.Mock()
        self.fake_asset_category.name = 'Fake Asset'
        self.fake_asset_category.value = 1000.0
        self.my_budget = Budget()

    def test_can_add_categories_to_budget(self):
        my_budget = Budget()
        my_budget.add_category(self.fake_expense_category)
        self.assertEqual(1, len(my_budget._categories))

    def test_can_remove_category_from_budget(self):
        self.my_budget.add_category(self.fake_expense_category)
        self.my_budget.remove_category("Fake Category")
        self.assertEqual(0, len(self.my_budget._categories))

    def test_budget_will_have_default_balance_of_zero(self):
        self.assertEqual(0.0, self.my_budget.get_current_balance())

    def test_budget_can_set_default_balance(self):
        start_value = 500.0
        self.fake_asset_category.value = start_value
        my_budget = Budget(start_balance=self.fake_asset_category)
        self.assertEqual(start_value, my_budget.get_current_balance())

    def test_budget_can_return_total_expenses(self):
        self.my_budget.add_category(self.fake_expense_category)
        self.my_budget.add_category(self.fake_expense_category)
        self.my_budget.add_category(self.fake_expense_category)
        self.assertEqual(-1500.0, self.my_budget.get_total_expenses())

    def test_can_add_asset_to_deposit(self):
        self.my_budget.add_asset(self.fake_asset_category)
        self.assertEqual(1, len(self.my_budget._assets))

        self.my_budget.add_asset(self.fake_asset_category)
        self.my_budget.add_asset(self.fake_asset_category)
        self.assertEqual(3, len(self.my_budget._assets))

    def test_can_remove_asset_from_budget(self):
        self.my_budget.add_asset(self.fake_asset_category)
        self.my_budget.remove_asset('Fake Asset')
        self.assertEqual(0, len(self.my_budget._assets))

    def test_budget_can_return_total_assets(self):
        self.my_budget.add_asset(self.fake_asset_category)
        self.my_budget.add_asset(self.fake_asset_category)
        self.my_budget.add_asset(self.fake_asset_category)
        self.assertEqual(3000.0, self.my_budget.get_total_assets())

    def test_budget_can_return_current_balance(self):
        self.my_budget.add_asset(self.fake_asset_category)
        self.my_budget.add_category(self.fake_expense_category)
        self.assertEqual(500.0, self.my_budget.get_current_balance())


if '__name__' == '__main__':
    unittest.main()
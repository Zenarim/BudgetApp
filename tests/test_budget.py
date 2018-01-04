import unittest
import unittest.mock as umock

from budget import Budget
from category import Category


class TestBudgetApp(unittest.TestCase):
    def setUp(self):
        self.fakeCategory = umock.Mock(spec_set=Category())
        self.fakeCategory.name = 'Fake Category'
        self.fakeCategory.get_total_expenses = umock.Mock(return_value=500.0)
        self.my_budget = Budget()

    def test_can_add_categories_to_budget(self):
        my_budget = Budget()
        my_budget.add_category(self.fakeCategory)
        self.assertEqual(1, len(my_budget.categories))

    def test_can_remove_categories_to_budget(self):
        self.my_budget.add_category(self.fakeCategory)
        self.my_budget.remove_category("Fake Category")
        self.assertEqual(0, len(self.my_budget.categories))

    def test_budget_will_have_default_balance_of_zero(self):
        self.assertEqual(0.0, self.my_budget.get_balance())

    def test_budget_can_set_default_balance(self):
        default_bal = 777.0
        my_budget = Budget(balance=default_bal)
        self.assertEqual(default_bal, my_budget.get_balance())

    def test_budget_will_return_difference_between_balance_and_total_balance_of_all_categories(self):
        self.my_budget.add_category(self.fakeCategory)
        self.my_budget.add_category(self.fakeCategory)
        self.my_budget.add_category(self.fakeCategory)
        self.assertEqual(-1500.0, self.my_budget.get_balance())


if '__name__' == '__main__':
    unittest.main()
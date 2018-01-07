import unittest
from unittest.mock import Mock
from datetime import date, timedelta


from transaction import Transaction


class TestBaseTransaction(unittest.TestCase):
    def setUp(self):
        self.empty_transaction = Transaction()
        self.my_transaction = Transaction(1000.0)

    def test_transactions_have_a_default_base_cost(self):
        self.assertEqual(0.0, self.empty_transaction.base_value)

    def test_transaction_can_set_base_cost_in_constructor(self):
        a_transaction = Transaction(500.0)
        self.assertEqual(500.0, a_transaction.base_value)

    def test_transaction_can_set_base_cost_dynamically(self):
        self.empty_transaction.base_value = 1000.0
        self.assertEqual(1000.0, self.empty_transaction.base_value)

    def test_transactions_will_have_default_creation_date_of_today(self):
        today_date = date.today()
        new_transaction = Transaction()
        self.assertEqual(today_date, new_transaction.creation_date)

    def test_transaction_can_set_custom_creation_date_on_creation(self):
        yesterday_date = date.today() - timedelta(days=1)
        new_transaction = Transaction(creation_date=yesterday_date)
        self.assertEqual(yesterday_date, new_transaction.creation_date)

    def test_transaction_entry_date_can_be_set_at_creation(self):
        entry_date = date.today() + timedelta(days=30)
        new_transaction = Transaction(date_entered=entry_date)
        self.assertEqual(entry_date, new_transaction.date_entered)

    def test_transaction_entry_date_can_be_modified_after_creation(self):
        late_entry_date = date.today() - timedelta(days=30)
        self.my_transaction.date_entered = late_entry_date
        self.assertEqual(late_entry_date, self.my_transaction.date_entered)

    def test_transaction_raises_exception_if_non_date_used_for_entry_date(self):
        self.assertRaises(TypeError, self.empty_transaction.date_entered, 5)

    def test_transactions_have_a_default_category(self):
        self.assertEqual('UncategorizedTransaction', self.empty_transaction.category)

    def test_transactions_can_set_their_category_at_creation(self):
        amazon_transaction = Transaction(category='Amazon')
        self.assertEqual('Amazon', amazon_transaction.category)

    def test_transaction_can_set_their_category_after_creation(self):
        self.empty_transaction.category = 'ChangedCategory'
        self.assertEqual('ChangedCategory', self.empty_transaction.category)

    def test_can_add_additional_costs_to_transaction(self):
        dinner_transaction = Transaction(base_value=25.0, category='Dinner', tip=5.0, discount=-10.0)
        self.assertEqual(20.0, dinner_transaction.total_value)


if '__name__' == '__main__':
    unittest.main()

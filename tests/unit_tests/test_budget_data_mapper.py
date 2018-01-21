import unittest


from data_mapper.budget_data_mapper import BudgetDataMapper


class TestBudgetDataMapper(unittest.TestCase):
    def test_budget_insert_statement(self):
        expected_sql_statement = "INSERT INTO budget VALUES \"Untitled Budget\" 2018-01-01"
        sql_insert_statement = BudgetDataMapper.insert_statement(budget_name=None, budget_date_created="2018-01-01")
        self.assertEqual(expected_sql_statement, sql_insert_statement)

    def test_budget_update_statement(self):
        expected_sql_statement = "UPDATE budget SET budgetName = 'Titled Budget' WHERE budgetKey = 1"
        sql_update_statement = BudgetDataMapper.update_statement(budget_name='Titled Budget', budget_key=1)
        self.assertEqual(expected_sql_statement, sql_update_statement)

    def test_budget_delete_statement(self):
        expected_sql_statement = "DELETE FROM budget WHERE budgetKey = 1"
        sql_delete_statement = BudgetDataMapper.delete_statement(1)
        self.assertEqual(expected_sql_statement, sql_delete_statement)

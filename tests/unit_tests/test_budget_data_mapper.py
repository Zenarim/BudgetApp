import unittest


from data_mapper.budget_data_mapper import BudgetDataMapper


class TestBudgetDataMapper(unittest.TestCase):
    def test_budget_insert_statement(self):
        expected_sql_statement = "INSERT INTO budget VALUES 1 \"Untitled Budget\" 2018-01-01"
        sql_insert_statement = BudgetDataMapper.insert_statement(key=1, budget_name=None,
                                                                 budget_date_created="2018-01-01")
        self.assertEqual(expected_sql_statement, sql_insert_statement)


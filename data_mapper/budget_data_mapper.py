

class BudgetDataMapper:
    @staticmethod
    def insert_statement(budget_name, budget_date_created):
        if not budget_name:
            budget_name = 'Untitled Budget'
        return f"INSERT INTO budget VALUES \"{budget_name}\" {budget_date_created}"

    @staticmethod
    def update_statement(budget_name, budget_key):
        return f"UPDATE budget SET budgetName = '{budget_name}' WHERE budgetKey = {budget_key}"

    @staticmethod
    def delete_statement(budget_key):
        return f"DELETE FROM budget WHERE budgetKey = {budget_key}"

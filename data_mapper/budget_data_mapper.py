

class BudgetDataMapper:
    @staticmethod
    def insert_statement(key, budget_name, budget_date_created):
        if not budget_name:
            budget_name = 'Untitled Budget'
        return f"INSERT INTO budget VALUES {key} \"{budget_name}\" {budget_date_created}"

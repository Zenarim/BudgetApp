

class Category():
    def __init__(self, name='Uncategorized', goal=0.0):
        self._name = name
        self._goal = goal
        self._transactions = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, goal):
        self._goal = goal

    @property
    def transactions(self):
        return self._transactions

    def add_transaction(self, transaction):
        self._transactions.append(transaction)

    def remove_transaction(self, del_transaction):
        for index, transaction in enumerate(self._transactions):
            if transaction == del_transaction:
                del self._transactions[index]
                break

    def get_total_expenses(self):
        return sum(trans.expense for trans in self._transactions)

    def get_remaining_balance(self):
        return self._goal - self.get_total_expenses()


"""

"""


class Goal():
    def __init__(self, name='UncategorizedGoal', goal=0.0):
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
    def num_of_transactions(self):
        return len(self._transactions)

    def add_transaction(self, transaction):
        self._transactions.append(transaction)

    def remove_transaction(self, del_transaction):
        for index, transaction in enumerate(self._transactions):
            if transaction == del_transaction:
                del self._transactions[index]
                break

    def get_total_transactions(self):
        return sum(transaction.value for transaction in self._transactions)

    def get_remaining_goal(self):
        return self._goal - self.get_total_transactions()

    def __contains__(self, transaction):
        return transaction in self._transactions


class ExpenseGoal(Goal):
    def __init__(self, name='UncategorizedExpenseGoal', goal=0.0):
        super().__init__(name, goal)

    def get_total_expenses(self):
        return -1 * self.get_total_transactions()


class AssetGoal(Goal):
    def __init__(self, name='UncategorizedAssetGoal', goal=0.0):
        super().__init__(name, goal)

    def get_total_assets(self):
        return self.get_total_transactions()


class Account:
    def __init__(self, name='UncategorizedGoal'):
        self.name = name
        self._transactions = []

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
        return sum(transaction.total_value for transaction in self._transactions)

    def __contains__(self, transaction):
        return transaction in self._transactions


class ExpenseAccount(Account):
    def __init__(self, name='UncategorizedExpenseAccount', spending_limit=0.0):
        super().__init__(name)
        self.spending_limit = spending_limit

    @property
    def account_balance(self):
        return -1 * self.get_total_transactions()

    @property
    def remaining_limit(self):
        return self.spending_limit + self.account_balance


class AssetAccount(Account):
    def __init__(self, name='UncategorizedAssetAccount'):
        super().__init__(name)

    @property
    def account_balance(self):
        return self.get_total_transactions()


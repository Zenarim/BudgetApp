

class Budget():
    def __init__(self, start_balance=None):
        self._accounts = []

        if start_balance:
            self._accounts.append(start_balance)

    def add_account(self, account):
        # Need to verify account is correct interface
        self._accounts.append(account)

    def remove_account(self, account_name):
        # Need to figure better qualification than account name
        for account_id, account in enumerate(self._accounts):
            if account.name == account_name:
                del self._accounts[account_id]
                break

    def __contains__(self, account):
        return account in self._accounts

    @property
    def account_balance(self):
        return sum(account.account_balance for account in self._accounts)

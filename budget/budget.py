

class Budget():
    def __init__(self, start_balance=None):
        self._categories = []
        self._assets = []

        if start_balance:
            self._assets.append(start_balance)

    def add_expense_account(self, category):
        # Need to verify category is correct interface
        self._categories.append(category)

    def remove_expense_account(self, category_name):
        # Need to figure better qualification than category name
        for category_id, category in enumerate(self._categories):
            if category.name == category_name:
                del self._categories[category_id]

    def add_asset_account(self, asset):
        # Need to verify asset is correct interface
        self._assets.append(asset)

    def remove_asset_account(self, asset_name):
        # Need to figure better qualification than asset name
        for asset_id, asset in enumerate(self._assets):
            if asset.name == asset_name:
                del self._assets[asset_id]

    def get_total_assets(self):
        return sum(asset_account.total_deposits for asset_account in self._assets)

    def get_total_expenses(self):
        return -1 * sum(expense_account.total_spent for expense_account in self._categories)

    def get_current_balance(self):
        return self.get_total_assets() + self.get_total_expenses()

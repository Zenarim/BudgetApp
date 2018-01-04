

class Budget():
    def __init__(self, balance=0.0):
        self._balance = balance
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)

    def remove_category(self, category_name):
        for id, category in enumerate(self.categories):
            if category.name == category_name:
                del self.categories[id]

    def get_balance(self):
        return self._balance - sum(category.get_total_expenses() for category in self.categories)

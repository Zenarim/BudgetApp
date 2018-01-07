from datetime import date


class Transaction:
    def __init__(self, base_value=0.0, creation_date=date.today(), date_entered=date.today(),
                 category='UncategorizedTransaction', expense=True, **kwargs):
        self.base_value = base_value
        self.category = category
        self.creation_date = creation_date
        self._date_entered = date_entered
        self.expense = expense
        self.additional_costs = kwargs

    @property
    def date_entered(self):
        return self._date_entered

    @date_entered.setter
    def date_entered(self, date_entered):
        if isinstance(date_entered, date):
            self._date_entered = date_entered
        else:
            raise TypeError("Must use a date object.")

    @property
    def total_value(self):
        if self.expense:
            return self.base_value + sum(value for value in self.additional_costs.values())
        else:
            return self.base_value

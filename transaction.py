from datetime import date

class Transaction:
    def __init__(self, base_value=0.0, creation_date=date.today(), date_entered=date.today()):
        self._base_value = base_value
        self._creation_date = creation_date
        self._date_entered = date_entered

    @property
    def base_value(self):
        return self._base_value

    @base_value.setter
    def base_value(self, base_cost):
        self._base_value = base_cost

    @property
    def total_cost(self):
        return self._base_value

    @property
    def creation_date(self):
        return self._creation_date

    @property
    def date_entered(self):
        return self._date_entered

    @date_entered.setter
    def date_entered(self, date_entered):
        self._date_entered = date_entered


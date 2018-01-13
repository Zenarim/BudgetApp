from datetime import date


class Transaction:
    def __init__(self, base_value=0.0, name='', creation_date=date.today(), transaction_date=date.today(),
                 category='UncategorizedTransaction', **kwargs):
        """
        :param base_value: The base amount being spent / deposited
        :param creation_date: The date the entry was made
        :param transaction_date: The date the transaction occurred
        :param category: The category this type of transaction would fall under
        :param kwargs:  Transactions can have additional costs / discounts
        """
        self.name = name
        self.base_value = base_value
        self.category = category
        self.creation_date = creation_date
        self._transaction_date = transaction_date
        self.additional_costs = kwargs

    @property
    def transaction_date(self):
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, date_entered):
        if isinstance(date_entered, date):
            self._transaction_date = date_entered
        else:
            raise TypeError("Must use a date object.")

    @property
    def total_value(self):
        if self.additional_costs:
            return self.base_value + sum(value for value in self.additional_costs.values())
        else:
            return self.base_value

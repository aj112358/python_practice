"""An implementation of a credit card, taken from the textbook.

Created By: AJ Singh
Date: Feb 9, 2021
"""


class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer, bank, account, limit):
        """Create a new credit card instance.

        The initial balance is zero.

        @param customer:    the name of the customer
        @param bank:        the name of the bank
        @param account:     the account identification number
        @param limit:       credit limit (in CAD)
        """

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return customer name."""
        return self._customer

    def get_bank(self):
        """Return bank name."""
        return self._bank

    def get_account(self):
        """Return card ID number (as a string)."""
        return self._account

    def get_limit(self):
        """Return credit limit."""
        return self._limit

    def get_balance(self):
        """ Return current card balance."""
        return self._balance

    def charge(self, price):
        """Charge price to card, after checking for sufficient credit available.

        @param price:   amount to charge to card
        @return:        True -> processed; False -> denied
        """

        if price + self._balance > self._limit:
            return False
        self._balance += price
        return True

    def make_payment(self, amount):
        """Apply payment to credit card.

        @param amount:  amount to pay on card
        @return:        None
        """

        self._balance -= amount

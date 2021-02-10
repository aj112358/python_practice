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


if __name__ == "__main__":
    # Doing some quick manual error checking

    wallet = []

    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('John Bowman', 'California Federal', '3485 0399 3395 1954', 3500))
    wallet.append(CreditCard('John Bowman', 'California Finance', '5391 0375 9387 5309', 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print()
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())

        while wallet[c].get_balance() > 0:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())

"""An implementation of a credit card, taken from the textbook.

Created By: AJ Singh
Date: Feb 9, 2021
"""


class CreditCard:
    """A consumer credit card."""

    __slots__ = "_customer", "_bank", "_account", "_limit", "_balance"

    def __init__(self, customer, bank, account, limit, balance=0):
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
        self._balance = balance

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

        try:
            if price + self._balance > self._limit:
                return False
            self._balance += price
            return True
        except TypeError:
            raise TypeError("Price must be a number.")

    def make_payment(self, amount):
        """Apply payment to credit card.

        @param amount:  amount to pay on card
        @return:        None
        """

        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")

        if amount < 0:
            raise ValueError("Amount must be a positive number.")

        self._balance -= amount


class PredatoryCreditCard(CreditCard):
    """An extension to the CreditCard class that incorporates compound interest and fees."""

    __slots__ = "_apr"

    OVERLIMIT_FEE = 5

    def __init__(self, customer, bank, account, limit, apr):
        """Create a new predatory credit card instance.

        The initial balance is zero.

        @param customer:    the name of the customer
        @param bank:        the name of the bank
        @param account:     the account identification number
        @param limit:       credit limit (in CAD)
        @param apr:         annual percentage rate (as a decimal)
        """

        super().__init__(customer, bank, account, limit)  # Call original constructor for it's initializations.
        self._apr = apr  # Have to manually initialize this ourselves.

    def charge(self, price):
        """Charge price to card, after checking for sufficient credit available.

        @param price:   amount to charge to card
        @return:        True -> processed; False -> denied (add overlimit fee to balance)
        """

        success = super().charge(price)  # Call to inherited method 'charge' (from parent class)

        # Checking if we need to add overlimit penalty for going over credit limit.
        if not success:
            self._balance += PredatoryCreditCard.OVERLIMIT_FEE
        return success  # That call expects a Boolean return value.

    def process_month(self):
        """Assess and apply monthly interest on outstanding balance."""

        if self._balance > 0:
            # If positive balance, convert APR to monthly multiplicative factor.
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor


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

    print("*" * 50)
    wallet.append(PredatoryCreditCard('Tina Turner', 'Las Vegas Finance', '1234 5678 4321 8765', 1500, 0.0825))

    print('Customer = ', wallet[3].get_customer())
    print('Limit = ', wallet[3].get_limit())
    print('Balance = ', wallet[3].get_balance())

    for val in range(1, 5):
        wallet[3].charge(100*val)
    print("New balance = ", wallet[3].get_balance())

    wallet[3].charge(600)
    print("Balance after overcharge = ", wallet[3].get_balance())

    wallet[3].process_month()
    print("Balance after added interest = ", wallet[3].get_balance())

    print("*" * 50)

    wallet.append(CreditCard("Vincent Valentine", 'Sector 7 Bank', "12345", 1000))
    # wallet[4].charge("hello")
    wallet[4].charge(500)
    # wallet[4].make_payment("Hello")
    wallet[4].make_payment(-250)

    print('Customer = ', wallet[4].get_customer())
    print('Limit = ', wallet[4].get_limit())
    print('Balance = ', wallet[4].get_balance())

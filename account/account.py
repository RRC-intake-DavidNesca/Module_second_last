"""This module defines the Account class."""

__author__ = "ACE Faculty"
__version__ = "1.3.21.2025"

from account.account_type import AccountType

class Account:
    """
    Uncomment given docstring
    """
    def __init__(self, account_type: AccountType, account_number: int, balance: float):
        """
        Uncomment given docstring.
        """
        if isinstance(account_type, AccountType):
            self._account_type = account_type
        else:
            raise ValueError("Invalid account type.")
        try:
            account_number = int(account_number)
        except ValueError:
            raise ValueError("Account number must be a whole number.")
        if account_number < 0:
            raise ValueError("Account number must be positive.")
        try:
            balance = float(balance)
        except ValueError:
            raise ValueError("Balance must be numeric.")
        self._account_number = account_number
        self._balance = balance

    @property
    def account_type(self) -> AccountType:
        """
        Accessor for the _account_type attribute.
        """
        return self._account_type
    
    @property
    def account_number(self) -> int:
        """
        Accessor for the _account_number attribute.
        """
        return self._account_number
 
    @property
    def balance(self) -> float:
        """
        Accessor for the _balance attribute.
        """
        return self._balance

        
    @account_type.setter
    def account_type(self, value: AccountType):
        """ Uncomment given docstring. """
        if isinstance(value, AccountType):
            self._account_type = value
        else:
            raise ValueError("Invalid account type.")

    @account_number.setter
    def account_number(self, value: int):
        """ Uncomment given docstring """
        try:
                value = int(value)
        except ValueError:
                raise ValueError("Account number must be numeric")
        if value < 0:
                raise ValueError("Account number must be positive.")
        self._account_number = value

    @balance.setter
    def balance(self, value: float):
        """ Uncomment given docstring. """
        try:
            value = float(value)
        except ValueError:
            raise ValueError("Balance number must be numeric")
        self._balance = value



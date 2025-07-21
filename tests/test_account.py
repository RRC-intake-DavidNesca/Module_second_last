"""The modules defines the unit test class TestAccount.

Example:
    $ python -m unittest -v tests/account_tests.py
"""

import unittest
from account.account import Account
from account.account_type import AccountType

class TestAccount(unittest.TestCase):
    """Defines the test cases for the Account class."""

    def test_account_type_accessor(self):
    # Arrange and Act
        account = Account(AccountType.SAVINGS, 999999,
        100.00)
        # Assert
        self.assertEqual(account.account_type, AccountType.SAVINGS)
    
    def test_init_invalid_account_type(self):    
        # Arrange:
        account_type = "INVALID"
        account_number = 123456789
        balance = 100
    
        expected = "Invalid account type."
    
        # Act and Assert:
        with self.assertRaises(ValueError) as context:
            Account(account_type, account_number, balance)
        self.assertEqual(expected, str(context.exception))
    
    def test_init_valid(self):
        # Arrange:
        account_type = AccountType.MORTGAGE
        account_number = 123456789
        balance = 100
    
        # Act:
        bank_account = Account(account_type, account_number, balance)
    
        # Assert:
        self.assertEqual(bank_account._account_type,account_type)
        self.assertEqual(bank_account._account_number, account_number)
        self.assertEqual(bank_account._balance, balance)
    
    def test_account_type_mutator_valid(self):
    # Arrange
        account = Account(AccountType.MORTGAGE, 100, 100)
        expected = AccountType.CHEQUING

    # Act
        account.account_type = AccountType.CHEQUING

    # Assert (uses the accessor to verify results)
        self.assertEqual(expected, account.account_type)

    def test_account_type_mutator_invalid(self):
    # Arrange
        account = Account(AccountType.MORTGAGE, 100, 100)
        expected = "Invalid account type."

    # Act and Assert
        with self.assertRaises(ValueError) as context:
            account.account_type = "INVALID"

    # Assert (uses the accessor to verify results)
        self.assertEqual(expected, str(context.exception))



if __name__ == "__main__":
    unittest.main()

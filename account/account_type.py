"""This module defines the AccountType enumeration."""

__author__ = "ACE Faculty"
__version__ = "1.3.21.2025"

from enum import Enum

class AccountType(Enum):
    SAVINGS = 1
    CHEQUING = 2
    MORTGAGE = 3
    CREDIT = 4


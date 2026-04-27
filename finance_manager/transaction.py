from enum import Enum


class TransactionType(Enum):
    INCOME = "income"
    EXPENSE = "expense"


class Transaction:

    def __init__(self, amount, transaction_type, description=""):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description

    def __repr__(self):
        return f"Transaction({self.transaction_type.value}, ${self.amount:.2f}, '{self.description}')"

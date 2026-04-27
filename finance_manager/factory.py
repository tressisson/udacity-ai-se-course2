from abc import ABC, abstractmethod

from finance_manager.transaction import Transaction, TransactionType


class TransactionFactory(ABC):

    @abstractmethod
    def create(self, amount, description=""):
        pass


class IncomeTransactionFactory(TransactionFactory):

    def create(self, amount, description=""):
        return Transaction(amount, TransactionType.INCOME, description)


class ExpenseTransactionFactory(TransactionFactory):

    def create(self, amount, description=""):
        return Transaction(amount, TransactionType.EXPENSE, description)

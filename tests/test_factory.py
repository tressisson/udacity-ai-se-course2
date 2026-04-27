import unittest

from finance_manager.factory import IncomeTransactionFactory, ExpenseTransactionFactory
from finance_manager.transaction import TransactionType


class TestIncomeTransactionFactory(unittest.TestCase):

    def setUp(self):
        self.factory = IncomeTransactionFactory()

    def test_creates_income_transaction(self):
        t = self.factory.create(500.0, "Freelance work")
        self.assertEqual(t.transaction_type, TransactionType.INCOME)

    def test_amount_is_set_correctly(self):
        t = self.factory.create(750.0)
        self.assertEqual(t.amount, 750.0)

    def test_description_is_set_correctly(self):
        t = self.factory.create(100.0, "Side project")
        self.assertEqual(t.description, "Side project")

    def test_default_description_is_empty(self):
        t = self.factory.create(200.0)
        self.assertEqual(t.description, "")


class TestExpenseTransactionFactory(unittest.TestCase):

    def setUp(self):
        self.factory = ExpenseTransactionFactory()

    def test_creates_expense_transaction(self):
        t = self.factory.create(75.0, "Groceries")
        self.assertEqual(t.transaction_type, TransactionType.EXPENSE)

    def test_amount_is_set_correctly(self):
        t = self.factory.create(300.0)
        self.assertEqual(t.amount, 300.0)


class TestFactoriesProduceDifferentTypes(unittest.TestCase):

    def test_income_and_expense_factories_differ(self):
        income = IncomeTransactionFactory().create(100.0)
        expense = ExpenseTransactionFactory().create(100.0)
        self.assertNotEqual(income.transaction_type, expense.transaction_type)


if __name__ == "__main__":
    unittest.main()

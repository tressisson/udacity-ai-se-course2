import unittest

from finance_manager.transaction import Transaction, TransactionType


class TestTransaction(unittest.TestCase):

    def test_create_income_transaction(self):
        t = Transaction(100.0, TransactionType.INCOME, "Salary")
        self.assertEqual(t.amount, 100.0)
        self.assertEqual(t.transaction_type, TransactionType.INCOME)
        self.assertEqual(t.description, "Salary")

    def test_create_expense_transaction(self):
        t = Transaction(50.0, TransactionType.EXPENSE, "Lunch")
        self.assertEqual(t.transaction_type, TransactionType.EXPENSE)
        self.assertEqual(t.amount, 50.0)

    def test_negative_amount_raises_value_error(self):
        with self.assertRaises(ValueError):
            Transaction(-10.0, TransactionType.INCOME)

    def test_zero_amount_raises_value_error(self):
        with self.assertRaises(ValueError):
            Transaction(0.0, TransactionType.EXPENSE)

    def test_default_description_is_empty_string(self):
        t = Transaction(25.0, TransactionType.INCOME)
        self.assertEqual(t.description, "")

    def test_transaction_type_enum_values(self):
        self.assertEqual(TransactionType.INCOME.value, "income")
        self.assertEqual(TransactionType.EXPENSE.value, "expense")

    def test_repr_contains_type_and_amount(self):
        t = Transaction(200.0, TransactionType.EXPENSE, "Rent")
        self.assertIn("expense", repr(t))
        self.assertIn("200.00", repr(t))


if __name__ == "__main__":
    unittest.main()

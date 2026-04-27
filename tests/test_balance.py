import unittest

from finance_manager.balance import Balance
from finance_manager.transaction import Transaction, TransactionType


class TestBalance(unittest.TestCase):

    def setUp(self):
        # Reset singleton before every test so each test gets a clean slate
        Balance._reset()
        self.balance = Balance(initial_balance=1000.0)

    def test_singleton_returns_same_instance(self):
        b1 = Balance()
        b2 = Balance()
        self.assertIs(b1, b2)

    def test_initial_balance_is_set_correctly(self):
        self.assertEqual(self.balance.balance, 1000.0)

    def test_income_increases_balance(self):
        t = Transaction(200.0, TransactionType.INCOME, "Bonus")
        self.balance.apply_transaction(t)
        self.assertEqual(self.balance.balance, 1200.0)

    def test_expense_decreases_balance(self):
        t = Transaction(300.0, TransactionType.EXPENSE, "Rent")
        self.balance.apply_transaction(t)
        self.assertEqual(self.balance.balance, 700.0)

    def test_multiple_transactions_update_balance_correctly(self):
        self.balance.apply_transaction(Transaction(500.0, TransactionType.INCOME))
        self.balance.apply_transaction(Transaction(200.0, TransactionType.EXPENSE))
        self.assertEqual(self.balance.balance, 1300.0)

    def test_second_call_to_balance_ignores_new_initial_value(self):
        # Singleton should return existing instance, not reinitialize with 9999
        b2 = Balance(initial_balance=9999.0)
        self.assertEqual(b2.balance, 1000.0)

    def test_remove_observer_stops_it_from_receiving_updates(self):
        from unittest.mock import MagicMock
        observer = MagicMock()
        self.balance.add_observer(observer)
        self.balance.remove_observer(observer)
        self.balance.apply_transaction(Transaction(50.0, TransactionType.INCOME))
        observer.update.assert_not_called()


if __name__ == "__main__":
    unittest.main()

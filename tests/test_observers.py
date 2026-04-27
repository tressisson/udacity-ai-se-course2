import unittest
from unittest.mock import patch, MagicMock

from finance_manager.balance import Balance
from finance_manager.observers import LowBalanceAlertObserver, PrintBalanceObserver
from finance_manager.transaction import Transaction, TransactionType


class TestLowBalanceAlertObserver(unittest.TestCase):

    def test_alert_is_printed_when_balance_below_threshold(self):
        observer = LowBalanceAlertObserver(threshold=100.0)
        with patch("builtins.print") as mock_print:
            observer.update(50.0)
            mock_print.assert_called_once()
            output = mock_print.call_args[0][0]
            self.assertIn("ALERT", output)

    def test_no_alert_when_balance_above_threshold(self):
        observer = LowBalanceAlertObserver(threshold=100.0)
        with patch("builtins.print") as mock_print:
            observer.update(200.0)
            mock_print.assert_not_called()

    def test_no_alert_when_balance_exactly_at_threshold(self):
        # The alert should only fire when strictly less than the threshold
        observer = LowBalanceAlertObserver(threshold=100.0)
        with patch("builtins.print") as mock_print:
            observer.update(100.0)
            mock_print.assert_not_called()

    def test_alert_message_shows_current_balance(self):
        observer = LowBalanceAlertObserver(threshold=200.0)
        with patch("builtins.print") as mock_print:
            observer.update(75.50)
            output = mock_print.call_args[0][0]
            self.assertIn("75.50", output)


class TestPrintBalanceObserver(unittest.TestCase):

    def test_balance_is_printed_on_update(self):
        observer = PrintBalanceObserver()
        with patch("builtins.print") as mock_print:
            observer.update(250.0)
            mock_print.assert_called_once()

    def test_output_contains_the_balance_value(self):
        observer = PrintBalanceObserver()
        with patch("builtins.print") as mock_print:
            observer.update(999.99)
            output = mock_print.call_args[0][0]
            self.assertIn("999.99", output)


class TestObserverIntegration(unittest.TestCase):

    def setUp(self):
        Balance._reset()

    def test_observer_is_called_when_transaction_applied(self):
        balance = Balance(initial_balance=500.0)
        mock_observer = MagicMock()
        balance.add_observer(mock_observer)

        t = Transaction(100.0, TransactionType.EXPENSE, "Test expense")
        balance.apply_transaction(t)

        mock_observer.update.assert_called_once_with(400.0)

    def test_multiple_observers_all_get_notified(self):
        balance = Balance(initial_balance=300.0)
        obs1 = MagicMock()
        obs2 = MagicMock()
        balance.add_observer(obs1)
        balance.add_observer(obs2)

        balance.apply_transaction(Transaction(50.0, TransactionType.INCOME))

        obs1.update.assert_called_once_with(350.0)
        obs2.update.assert_called_once_with(350.0)


if __name__ == "__main__":
    unittest.main()

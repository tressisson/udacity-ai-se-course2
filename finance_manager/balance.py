from finance_manager.transaction import TransactionType


class Balance:
    # singleton - only one instance should exist
    _instance = None

    def __new__(cls, initial_balance=0.0):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._balance = initial_balance
            cls._instance._observers = []
        return cls._instance

    @classmethod
    def _reset(cls):
        # used in tests to get a fresh instance each time
        cls._instance = None

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._balance)

    def apply_transaction(self, transaction):
        if transaction.transaction_type == TransactionType.INCOME:
            self._balance += transaction.amount
        elif transaction.transaction_type == TransactionType.EXPENSE:
            self._balance -= transaction.amount
        self._notify_observers()

    @property
    def balance(self):
        return self._balance

    def __repr__(self):
        return f"Balance(${self._balance:.2f})"

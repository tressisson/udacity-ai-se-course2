from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, balance):
        pass


class LowBalanceAlertObserver(Observer):

    def __init__(self, threshold):
        self.threshold = threshold

    def update(self, balance):
        if balance < self.threshold:
            print(f"[ALERT] Low balance! ${balance:.2f} is below the threshold of ${self.threshold:.2f}")


class PrintBalanceObserver(Observer):

    def update(self, balance):
        print(f"[INFO] Balance updated: ${balance:.2f}")

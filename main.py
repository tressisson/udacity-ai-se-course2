from finance_manager.balance import Balance
from finance_manager.adapter import ExternalFreelanceIncome, TransactionAdapter
from finance_manager.observers import LowBalanceAlertObserver, PrintBalanceObserver
from finance_manager.factory import IncomeTransactionFactory, ExpenseTransactionFactory


def main():
    print("Personal Finance Manager")
    print("-" * 30)

    Balance._reset()

    balance = Balance(initial_balance=500.00)
    balance.add_observer(PrintBalanceObserver())
    balance.add_observer(LowBalanceAlertObserver(threshold=100.00))

    print("Starting balance: $500.00\n")

    income_factory = IncomeTransactionFactory()
    expense_factory = ExpenseTransactionFactory()

    print("Monthly transactions:")
    balance.apply_transaction(income_factory.create(2000.00, "Monthly salary"))
    balance.apply_transaction(expense_factory.create(1200.00, "Rent"))
    balance.apply_transaction(expense_factory.create(150.00, "Groceries"))
    balance.apply_transaction(expense_factory.create(80.00, "Electricity bill"))

    print("\nFreelance invoice:")
    invoice = ExternalFreelanceIncome(
        invoice_id="INV-2024-042",
        project_name="Website Redesign",
        amount_due=750.00,
    )
    balance.apply_transaction(TransactionAdapter(invoice).to_transaction())

    print("\nLarge expense:")
    balance.apply_transaction(expense_factory.create(1800.00, "Emergency car repair"))

    print(f"\nFinal {balance}")


if __name__ == "__main__":
    main()

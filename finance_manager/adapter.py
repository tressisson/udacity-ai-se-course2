from finance_manager.transaction import Transaction, TransactionType


class ExternalFreelanceIncome:
    # this simulates data coming in from a third-party invoicing system

    def __init__(self, invoice_id, project_name, amount_due):
        self.invoice_id = invoice_id
        self.project_name = project_name
        self.amount_due = amount_due


class TransactionAdapter:
    # converts an ExternalFreelanceIncome into a Transaction the app can use

    def __init__(self, external_income):
        self.external_income = external_income

    def to_transaction(self):
        description = (
            f"Freelance payment for '{self.external_income.project_name}' "
            f"(Invoice ID: {self.external_income.invoice_id})"
        )
        return Transaction(
            amount=self.external_income.amount_due,
            transaction_type=TransactionType.INCOME,
            description=description,
        )

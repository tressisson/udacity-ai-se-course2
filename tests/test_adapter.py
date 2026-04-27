import unittest

from finance_manager.adapter import ExternalFreelanceIncome, TransactionAdapter
from finance_manager.transaction import Transaction, TransactionType


class TestTransactionAdapter(unittest.TestCase):

    def setUp(self):
        self.external = ExternalFreelanceIncome(
            invoice_id="INV-001",
            project_name="Logo Design",
            amount_due=500.0,
        )
        self.adapter = TransactionAdapter(self.external)

    def test_adapter_returns_a_transaction_object(self):
        result = self.adapter.to_transaction()
        self.assertIsInstance(result, Transaction)

    def test_amount_matches_external_amount_due(self):
        result = self.adapter.to_transaction()
        self.assertEqual(result.amount, 500.0)

    def test_transaction_type_is_income(self):
        result = self.adapter.to_transaction()
        self.assertEqual(result.transaction_type, TransactionType.INCOME)

    def test_description_includes_project_name(self):
        result = self.adapter.to_transaction()
        self.assertIn("Logo Design", result.description)

    def test_description_includes_invoice_id(self):
        result = self.adapter.to_transaction()
        self.assertIn("INV-001", result.description)

    def test_different_invoices_produce_different_descriptions(self):
        other = ExternalFreelanceIncome("INV-002", "Mobile App", 1200.0)
        result = TransactionAdapter(other).to_transaction()
        self.assertIn("Mobile App", result.description)
        self.assertIn("INV-002", result.description)


if __name__ == "__main__":
    unittest.main()

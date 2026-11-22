from datetime import date
from decimal import Decimal

import pytest
from pydantic import ValidationError

from app.models.invoice import Invoice, InvoiceLine, InvoiceParty


def valid_invoice() -> Invoice:
    return Invoice(
        invoice_number="INV-001",
        issue_date=date(2026, 2, 1),
        currency="eur",
        seller=InvoiceParty(name="Seller GmbH", country_code="de", vat_id="de 123456789"),
        buyer=InvoiceParty(name="Buyer GmbH"),
        lines=[InvoiceLine(
            description="Service", quantity=Decimal("1"),
            unit_price=Decimal("100"), tax_rate=Decimal("19"),
            line_net_amount=Decimal("100"),
        )],
        net_total=Decimal("100"), tax_total=Decimal("19"), gross_total=Decimal("119"),
        iban="de02 1203 0000 0000 2020 51",
    )


def test_values_are_normalized():
    invoice = valid_invoice()
    assert invoice.currency == "EUR"
    assert invoice.seller.country_code == "DE"
    assert invoice.seller.vat_id == "DE123456789"
    assert invoice.iban == "DE02120300000000202051"


def test_empty_invoice_is_representable():
    # Extraction can fail to find everything; the schema must still hold the partial result.
    invoice = Invoice()
    assert invoice.invoice_number is None
    assert invoice.lines == []
    assert invoice.seller.name is None


def test_present_values_are_still_constrained():
    with pytest.raises(ValidationError):
        Invoice(currency="EURO")
    with pytest.raises(ValidationError):
        Invoice(net_total=Decimal("-1"))
    with pytest.raises(ValidationError):
        InvoiceLine(quantity=Decimal("0"))
    with pytest.raises(ValidationError):
        InvoiceLine(tax_rate=Decimal("101"))


def test_round_trip_through_json_dump():
    invoice = valid_invoice()
    again = Invoice.model_validate(invoice.model_dump(mode="json"))
    assert again == invoice

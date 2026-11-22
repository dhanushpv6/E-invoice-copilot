"""Invoice domain schema aligned with the EN 16931 business terms used by XRechnung.

Every value is optional on purpose. Extraction from documents is lossy, so a missing
mandatory value must surface as a validation finding and a human-review task instead of a
crash. Constraints still apply to values that are present. Rule checks live in
``business_rules`` (week 4), not in this schema, so that inconsistent documents (for example
wrong printed totals) can be represented faithfully and then flagged.
"""
from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, field_validator


class InvoiceParty(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    name: str | None = Field(default=None, max_length=200)  # BT-27 / BT-44
    street: str | None = Field(default=None, max_length=200)  # BT-35 / BT-50
    city: str | None = Field(default=None, max_length=100)  # BT-37 / BT-52
    postal_code: str | None = Field(default=None, max_length=20)  # BT-38 / BT-53
    country_code: str | None = Field(default=None, min_length=2, max_length=2)  # BT-40 / BT-55
    vat_id: str | None = Field(default=None, max_length=30)  # BT-31 / BT-48
    contact_name: str | None = Field(default=None, max_length=200)  # BT-41 (seller)
    contact_phone: str | None = Field(default=None, max_length=50)  # BT-42 (seller)
    # Electronic address (BT-34 / BT-49) and, for the seller, contact e-mail (BT-43).
    email: str | None = Field(default=None, max_length=200)

    @field_validator("country_code", "vat_id")
    @classmethod
    def normalize_upper(cls, value: str | None) -> str | None:
        return value.replace(" ", "").upper() if value else value


class InvoiceLine(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    description: str | None = Field(default=None, max_length=500)  # BT-153
    quantity: Decimal | None = Field(default=None, gt=0)  # BT-129
    unit_code: str | None = Field(default="C62", max_length=3)  # BT-130 (C62 = piece)
    unit_price: Decimal | None = Field(default=None, ge=0)  # BT-146
    tax_rate: Decimal | None = Field(default=None, ge=0, le=100)  # BT-152 (percent)
    line_net_amount: Decimal | None = Field(default=None, ge=0)  # BT-131


class Invoice(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    invoice_number: str | None = Field(default=None, max_length=100)  # BT-1
    issue_date: date | None = None  # BT-2
    due_date: date | None = None  # BT-9
    currency: str | None = Field(default=None, min_length=3, max_length=3)  # BT-5
    buyer_reference: str | None = Field(default=None, max_length=100)  # BT-10
    seller: InvoiceParty = Field(default_factory=InvoiceParty)
    buyer: InvoiceParty = Field(default_factory=InvoiceParty)
    lines: list[InvoiceLine] = Field(default_factory=list)
    payment_terms: str | None = Field(default=None, max_length=500)  # BT-20
    iban: str | None = Field(default=None, max_length=40)  # BT-84
    net_total: Decimal | None = Field(default=None, ge=0)  # BT-109
    tax_total: Decimal | None = Field(default=None, ge=0)  # BT-110
    gross_total: Decimal | None = Field(default=None, ge=0)  # BT-112

    @field_validator("currency")
    @classmethod
    def normalize_currency(cls, value: str | None) -> str | None:
        return value.upper() if value else value

    @field_validator("iban")
    @classmethod
    def normalize_iban(cls, value: str | None) -> str | None:
        return value.replace(" ", "").upper() if value else value

import logging

from app.core.logging import RedactingFilter, redact


def test_redacts_email_iban_phone_and_vat_id():
    text = (
        "mail anna@example.com iban DE02 1203 0000 0000 2020 51 "
        "tel +49 89 1234567 vat DE123456789"
    )
    cleaned = redact(text)
    assert "anna@example.com" not in cleaned
    assert "2020 51" not in cleaned
    assert "1234567" not in cleaned
    assert "DE123456789" not in cleaned
    for tag in ("[email]", "[iban]", "[phone]", "[vat-id]"):
        assert tag in cleaned


def test_plain_text_is_untouched():
    assert redact("job 1234 finished in 12 ms") == "job 1234 finished in 12 ms"


def test_filter_masks_formatted_log_records():
    record = logging.LogRecord("t", logging.INFO, __file__, 1, "sent to %s", ("a@b.example",), None)
    assert RedactingFilter().filter(record) is True
    assert "a@b.example" not in record.getMessage()

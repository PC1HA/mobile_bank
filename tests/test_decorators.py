from typing import Iterator

import pytest

from src.decorators import log
from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def setup_logging(caplog: pytest.LogCaptureFixture) -> Iterator:
    yield caplog


def test_function_logging(setup_logging: pytest.LogCaptureFixture) -> None:
    @log()
    def test_function(x: int, y: int) -> int:
        return x + y

    result = test_function(3, 4)

    assert result == 7
    assert "Calling test_function with args: (3, 4), kwargs: {}" in setup_logging.text
    assert "test_function returned 7" in setup_logging.text


def test_function_error_logging(setup_logging: pytest.LogCaptureFixture) -> None:
    @log()
    def faulty_function(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        faulty_function(1, 0)

    assert "Calling faulty_function with args: (1, 0), kwargs: {}" in setup_logging.text
    assert "faulty_function raised ZeroDivisionError" in setup_logging.text  # Проверка на ошибку


@log()
def test_get_mask_card_number_valid() -> None:
    assert get_mask_card_number(1234567812345678) == "1234 56** **** 5678"
    assert get_mask_card_number("1234 5678 1234 5678") == "1234 56** **** 5678"


@log()
def test_get_mask_card_number_invalid() -> None:
    assert get_mask_card_number("1234 5678 1234") == "Неверный номер карты"
    assert get_mask_card_number("some_invalid_string") == "Неверный номер карты"
    assert get_mask_card_number(123) == "Неверный номер карты"

    with pytest.raises(ValueError, match="Неверный тип данных. Ожидается целое число или строка."):
        get_mask_card_number([])  # type: ignore


@log()
def test_get_mask_account_valid() -> None:
    assert get_mask_account(12345678901234567890) == "**7890"
    assert get_mask_account("12345678901234567890") == "**7890"


@log()
def test_get_mask_account_invalid() -> None:
    assert get_mask_account("1234567890123456789") == "Неверный номер счета"
    assert get_mask_account("invalid_account") == "Неверный номер счета"
    assert get_mask_account(123) == "Неверный номер счета"

    with pytest.raises(ValueError, match="Неверный тип данных. Ожидается целое число или строка."):
        get_mask_account([])  # type: ignore

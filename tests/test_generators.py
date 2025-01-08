from typing import Any, Dict, List, Union

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {"description": "Transaction 1", "operationAmount": {"amount": 100, "currency": {"code": "USD"}}},
        {"description": "Transaction 2", "operationAmount": {"amount": 200, "currency": {"code": "EUR"}}},
        {"description": "Transaction 3", "operationAmount": {"amount": 300, "currency": {"code": "USD"}}},
    ]


@pytest.mark.parametrize(
    "currency_code, expected_descriptions",
    [("USD", ["Transaction 1", "Transaction 3"]), ("EUR", ["Transaction 2"]), ("GBP", [])],
)
def test_filter_by_currency(
    sample_transactions: List[Dict[str, Any]], currency_code: str, expected_descriptions: List[str]
) -> None:
    filtered_transactions = list(filter_by_currency(sample_transactions, currency_code))
    result_descriptions = [t["description"] for t in filtered_transactions]
    assert result_descriptions == expected_descriptions


def test_filter_by_currency_empty_list() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == ["Список транзакций пуст."]


def test_filter_by_currency_invalid_input() -> None:
    with pytest.raises(ValueError) as excinfo:
        list(filter_by_currency("invalid", "USD"))  # type: ignore
    assert str(excinfo.value) == "Входные данные должны быть списком."


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Transaction 1", "Transaction 2", "Transaction 3"]


def test_transaction_descriptions_empty_list() -> None:
    result = list(transaction_descriptions([]))
    assert result == ["Список транзакций пуст."]


def test_transaction_descriptions_invalid_input() -> None:
    with pytest.raises(ValueError) as excinfo:
        list(transaction_descriptions("invalid"))  # type: ignore
    assert str(excinfo.value) == "Входные данные должны быть списком."


@pytest.mark.parametrize(
    "start, stop, expected_output",
    [
        (" 1 2 3 ", " 1 2 4 ", ["0000000000000123", "0000000000000124"]),
        (1, 5, ["0000000000000001", "0000000000000002", "0000000000000003", "0000000000000004", "0000000000000005"]),
        ("10", "12", ["0000000000000010", "0000000000000011", "0000000000000012"]),
    ],
)
def test_card_number_generator(start: Union[str, int], stop: Union[str, int], expected_output: List[str]) -> None:
    generated_numbers = list(card_number_generator(start, stop))
    assert generated_numbers == [f"{num[:4]} {num[4:8]} {num[8:12]} {num[12:16]}" for num in expected_output]


def test_card_number_generator_empty_range() -> None:
    with pytest.raises(ValueError) as excinfo:
        list(card_number_generator("10", "5"))
    assert str(excinfo.value) == "Параметр start должен быть меньше или равен параметру stop."


def test_card_number_generator_invalid_input() -> None:
    with pytest.raises(ValueError) as excinfo:
        list(card_number_generator("1a", "5"))
    assert str(excinfo.value) == "Параметры должны содержать только целые числа."

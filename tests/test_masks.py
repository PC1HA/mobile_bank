import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def mask_account_number() -> str:
    return "**4305"


@pytest.fixture()
def mask_card_number() -> str:
    return "7000 79** **** 6361"


@pytest.fixture()
def incorrect_number() -> str:
    return "Неверный номер карты"


def test_mask_card_number(mask_card_number: str) -> None:
    assert get_mask_card_number("7000792289606361") == mask_card_number
    assert get_mask_card_number("70 007 92289 6063 61") == mask_card_number
    assert get_mask_card_number(7000792289606361) == mask_card_number


def test_mask_account_number(mask_account_number: str) -> None:
    assert get_mask_account(73654108430135874305) == mask_account_number
    assert get_mask_account("73654108430135874305") == mask_account_number
    assert get_mask_account("73    6541 084301358743 05") == mask_account_number


def test_incorrect_number(incorrect_number: str) -> None:
    assert get_mask_card_number("transactionsaaaa") == incorrect_number
    assert get_mask_card_number(14345454363636346346346) == incorrect_number
    assert get_mask_card_number(121231) == incorrect_number
    assert get_mask_account("") == incorrect_number
    assert get_mask_account(73654108430) == incorrect_number
    assert get_mask_account("fatgpvktjfkvlfotfvfd") == incorrect_number

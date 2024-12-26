import pytest
from src.widget import mask_account_card, git_date


@pytest.fixture()
def mask_account():
    return 'Счет **4305'

@pytest.fixture()
def mask_card_maestro():
    return 'Maestro 7000 79** **** 6361'

@pytest.fixture()
def mask_card_visa():
    return 'Visa Platinum 7000 79** **** 6361'

@pytest.fixture()
def incorrect_data():
    return 'Неверные данные'

@pytest.fixture()
def isdigit_data():
    return (
        'Неверные данные,'
        ' возможно вы сначала ввели номер Счета или Карты'
    )


def test_mask_account(mask_account):
    assert mask_account_card('Счет 73654108430135874305') == mask_account
    assert mask_account_card('Счет73654108430135874305') == mask_account
    assert mask_account_card('Счет     73654108430135874305') == mask_account
    assert mask_account_card('Сч  ет73 65410  8430135  8743 05') == mask_account
    assert mask_account_card('Счёт 73654108430135874305') == mask_account
    assert mask_account_card('счет73654108430135874305') == mask_account
    assert mask_account_card('счёт73654108430135874305') == mask_account
    assert mask_account_card('СЧЕТ73654108430135874305') == mask_account
    assert mask_account_card('СЧЁТ73654108430135874305') == mask_account
    assert mask_account_card('Счёт73654108430135874305') == mask_account
    assert mask_account_card('сч ёт73 654108 4301358 74305') == mask_account
    assert mask_account_card('счЁт73654108430135874305') == mask_account
    assert mask_account_card('счЕт73654108430135874305') == mask_account
    assert mask_account_card('    счёт73654108430135874305    ') == mask_account

def test_mask_card_maestro(mask_card_maestro):
    assert mask_account_card('Maestro 7000792289606361') == mask_card_maestro
    assert mask_account_card('maestro 7000792289606361') == mask_card_maestro
    assert mask_account_card('Maestro7000792289606361') == mask_card_maestro
    assert mask_account_card('MAESTRO 7000792289606361') == mask_card_maestro
    assert mask_account_card('MAESTRO7000792289606361') == mask_card_maestro
    assert mask_account_card('mAestro 7000792289606361') == mask_card_maestro
    assert mask_account_card('mAestro7000792289606361') == mask_card_maestro
    assert mask_account_card('Ma estr o 7000 7922 89606 361') == mask_card_maestro
    assert mask_account_card('    Maestro 7000792289606361   ') == mask_card_maestro

def test_mask_card_visa(mask_card_visa):
    assert mask_account_card('Visa Platinum 7000792289606361') == mask_card_visa
    assert mask_account_card('visa platinum 7000792289606361') == mask_card_visa
    assert mask_account_card('VISA PLATINUM 7000792289606361') == mask_card_visa
    assert mask_account_card('VisaPlatinum 7000792289606361') == mask_card_visa
    assert mask_account_card('VisaPlatinum7000792289606361') == mask_card_visa
    assert mask_account_card('visaplatinum 7000792289606361') == mask_card_visa
    assert mask_account_card('visaplatinum7000792289606361') == mask_card_visa
    assert mask_account_card('VISAPLATINUM 7000792289606361') == mask_card_visa
    assert mask_account_card('VISAPLATINUM7000792289606361') == mask_card_visa
    assert mask_account_card(' V is a Pla tin um 70 00792 289606 361 ') == mask_card_visa
    assert mask_account_card(' v is a p la tinu m 700 0792 289606 361 ') == mask_card_visa
    assert mask_account_card('V I SA P LAT INUM 700 079228 96063 61 ') == mask_card_visa

def test_incorrect_data(incorrect_data):
    assert mask_account_card(12133546656) == incorrect_data
    assert mask_account_card([]) == incorrect_data
    assert mask_account_card({}) == incorrect_data
    assert mask_account_card('     Platinum 7000792289606361') == incorrect_data
    assert mask_account_card('Visa          7000792289606361') == incorrect_data
    assert mask_account_card('Visa Maestro  7000792289606361') == incorrect_data
    assert mask_account_card(()) == incorrect_data
    assert mask_account_card('isa Platinum 7000792289606361') == incorrect_data

def test_isdigit_data(isdigit_data):
    assert mask_account_card('7000792289606361 Visa Platinum') == isdigit_data
    assert mask_account_card('73654108430135874305 Счет') == isdigit_data
    assert mask_account_card('7000792289606361 Maestro') == isdigit_data
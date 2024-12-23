import pytest
from src.masks import get_mask_card_number


def test_str_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('70 007 92289 6063 61') == '7000 79** **** 6361'

def test_int_mask_card_number():
    assert get_mask_card_number(7000792289606361) == '7000 79** **** 6361'
    assert get_mask_card_number(121231) == 'Неверный номер карты'
    assert get_mask_card_number(14345454363636346346346) == 'Неверный номер карты'

def test_list_mask_card_number():
    assert get_mask_card_number(['7000792289606361']) == 'Неверный номер карты'

def test_tuple_mask_card_number():
    assert get_mask_card_number((7000792289606361, )) == 'Неверный номер карты'

def test_None_mask_card_number():
    assert get_mask_card_number(None) == 'Неверный номер карты'

def test_isalpha_mask_card_number():
    assert get_mask_card_number('transactionsaaaa')
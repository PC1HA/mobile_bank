from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Преобразуем номер карты в строку, удаляем лишние пробелы"""
    card_number = str(card_number)
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16 or card_number.isalpha():
        return "Неверный номер карты"
    else:
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

        return masked_number


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Преобразует номер счёта в номер со '**' и четыре последних цифры"""
    account_number = str(account_number)
    account_number = account_number.replace(" ", "")
    if len(account_number) != 20 or account_number.isalpha():
        return "Неверный номер счёта"
    else:
        masked_account = f"**{account_number[-4:]}"

        return masked_account

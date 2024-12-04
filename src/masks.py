from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Преобразуем номер карты в строку, удаляем лишние пробелы"""
    card_number = str(card_number)
    card_number = card_number.replace(" ", "")
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

    return masked_number


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Преобразует номер счёта в номер со '**' и четыре последних цифры"""
    account_number = str(account_number)
    account_number = account_number.replace(" ", "")
    masked_account = f"**{account_number[-4:]}"

    return masked_account


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))

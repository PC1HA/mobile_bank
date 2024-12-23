from datetime import datetime
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: Union[str]) -> Union[str]:
    """Функция маскирует номер карты или счёт по функциям из masks.py"""

    if "Счет" in card_or_account_number:
        account_number_list = card_or_account_number.split()
        account_name = account_number_list[0]
        account_number = account_number_list[1]

        mask_account_number = get_mask_account(account_number)

        return f"{account_name} {mask_account_number}"

    else:
        card_numer_list = card_or_account_number.split()
        card_name = card_numer_list[0]
        card_number = card_numer_list[1]

        mask_card_number = get_mask_card_number(card_number)

        return f"{card_name} {mask_card_number}"


def git_date(date_and_time: Union[str]) -> Union[str]:
    """
    Преобразует строку с датой в формате "YYYY-MM-DDTHH:MM:SS.ssssss"
    в строку с датой в формате "ДД.ММ.ГГГГ".
    """
    date_object = datetime.fromisoformat(date_and_time)
    formatted_date = date_object.strftime("%d.%m.%Y")

    return formatted_date

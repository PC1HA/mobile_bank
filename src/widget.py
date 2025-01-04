from datetime import datetime
from typing import Union

from src.masks import get_mask_account, get_mask_card_number

triggers = ["счет", "счёт", "maestro", "visa platinum", "visaplatinum"]


def mask_account_card(card_or_account_number: Union[str]) -> Union[str]:
    """
    Функция принимает строку, представляющую номер карты или счета,
    и маскирует ее через mask.py либо через условие
    """
    if not isinstance(card_or_account_number, str):

        raise ValueError("Неверный тип данных, ожидается ТОЛЬКО строка: str!")

    elif len(card_or_account_number) < 23:

        return "Неверные данные"

    elif card_or_account_number.split()[0].isdigit():

        return "Неверные данные, возможно вы сначала ввели номер Счета или Карты"

    elif "Maestro" in card_or_account_number.title() and len(card_or_account_number) == 24:
        card_number_list = card_or_account_number.title().split()
        card_name = card_number_list[0]
        card_number = card_number_list[1]

        mask_card_number = get_mask_card_number(card_number)

        return f"{card_name} {mask_card_number}"

    elif "Счет" in card_or_account_number.title() and len(card_or_account_number) == 25:
        account_number_list = card_or_account_number.title().split()
        account_name = account_number_list[0]
        account_number = account_number_list[1]

        mask_account_number = get_mask_account(account_number)

        return f"{account_name} {mask_account_number}"

    elif "Счёт" in card_or_account_number.title() and len(card_or_account_number) == 25:
        account_number_list = card_or_account_number.title().split()
        account_name = triggers[0].title()
        account_number = account_number_list[1]

        mask_account_number = get_mask_account(account_number)

        return f"{account_name} {mask_account_number}"

    elif "Visa Platinum" in card_or_account_number.title() and len(card_or_account_number) == 30:
        card_number_list = card_or_account_number.title().split()
        card_name = card_number_list[0] + " " + card_number_list[1]
        card_number = card_number_list[2]

        mask_card_number = get_mask_card_number(card_number)

        return f"{card_name} {mask_card_number}"

    else:
        card_or_account_number = card_or_account_number.replace(" ", "")
        card_or_account_number = card_or_account_number.title()
        for trigger in triggers:
            if trigger.title() in card_or_account_number:
                if len(card_or_account_number) == 28:
                    return (
                        f"{card_or_account_number[:4].title()}"
                        f" {card_or_account_number[4:12].title()}"
                        f" {card_or_account_number[12:16]}"
                        f" {card_or_account_number[16:18]}**"
                        f" **** {card_or_account_number[-4:]}"
                    )

                elif len(card_or_account_number) == 23:
                    return (
                        f"{card_or_account_number[:7]}"
                        f" {card_or_account_number[7:11]}"
                        f" {card_or_account_number[11:13]}**"
                        f" **** {card_or_account_number[-4:]}"
                    )

                elif len(card_or_account_number) == 24:
                    return f"{triggers[0].title()}" f" **{card_or_account_number[-4:]}"

    return "Неверные данные"


def git_date(date_and_time: Union[str]) -> Union[str]:
    """
    Преобразует строку с датой в формате "YYYY-MM-DDTHH:MM:SS.ssssss"
    в строку с датой в формате "ДД.ММ.ГГГГ".
    """
    if not isinstance(date_and_time, str):

        raise ValueError("Неверный тип данных, ожидается ТОЛЬКО строка: str!")

    if len(date_and_time) < 10:

        return "Неверные данные"

    for item in date_and_time[:10]:
        if item == "-":

            continue

        elif item.isalpha():

            return "Неверные данные"

    if date_and_time[0:4] == "0000" or date_and_time[5:7] == "00" or date_and_time[8:10] == "00":

        return "Неверные данные"

    if date_and_time[4] != "-" or date_and_time[7] != "-":

        return "Неверные данные"

    date_object = datetime.fromisoformat(date_and_time)
    formatted_date = date_object.strftime("%d.%m.%Y")

    return formatted_date

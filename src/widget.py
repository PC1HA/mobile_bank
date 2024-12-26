from datetime import datetime
from typing import Union

from src.masks import get_mask_account, get_mask_card_number

triggers = ['счет', 'счёт', 'maestro', 'visa platinum', 'visaplatinum']

def mask_account_card(card_or_account_number: Union[str]) -> Union[str]:
    """
    Функция принимает строку, представляющую номер карты или счета,
    и маскирует ее через mask.py либо через условие
    """
    checks_triggers = lambda check_trigger: check_trigger not in triggers

    if not isinstance(card_or_account_number, str):
        return 'Неверные данные'

    elif card_or_account_number.split()[0].isdigit():
        return (
            'Неверные данные,'
            ' возможно вы сначала ввели номер Счета или Карты'
        )

    elif len(card_or_account_number) < 23 and checks_triggers(card_or_account_number.lower()):
        return 'Неверные данные'

    elif 'Maestro' in card_or_account_number.title() and len(card_or_account_number) == 24:
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
        card_name = card_number_list[0] + ' ' + card_number_list[1]
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
                        f'{card_or_account_number[:4].title()}'
                        f' {card_or_account_number[4:12].title()}'
                        f' {card_or_account_number[12:16]}'
                        f' {card_or_account_number[16:18]}**'
                        f' **** {card_or_account_number[-4:]}'
                    )

                elif len(card_or_account_number) == 23:
                    return (
                        f'{card_or_account_number[:7]}'
                        f' {card_or_account_number[7:11]}'
                        f' {card_or_account_number[11:13]}**'
                        f' **** {card_or_account_number[-4:]}'
                    )

                elif len(card_or_account_number) == 24:
                    return (
                        f'{triggers[0].title()}'
                        f' **{card_or_account_number[-4:]}'
                    )


    return 'Неверные данные'

def git_date(date_and_time: Union[str]) -> Union[str]:
    """
    Преобразует строку с датой в формате "YYYY-MM-DDTHH:MM:SS.ssssss"
    в строку с датой в формате "ДД.ММ.ГГГГ".
    """
    date_object = datetime.fromisoformat(date_and_time)
    formatted_date = date_object.strftime("%d.%m.%Y")

    return formatted_date

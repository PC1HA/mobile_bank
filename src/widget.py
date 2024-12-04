from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_number: Union[str]) -> Union[str]:
    """Функция маскирует номер карты или счёт"""

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


if __name__ == "__main__":
    print(mask_account_card("Счет 64686473678894779589"))

import logging
import os
from typing import Union

log_directory = 'logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logging.basicConfig(
    filename=os.path.join(log_directory, 'masks.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='w'
)

logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Преобразуем номер карты в строку, удаляем лишние пробелы"""
    if not isinstance(card_number, (int, str)):
        logger.error("Неверный тип данных для номера карты: %s", type(card_number))
        raise ValueError("Неверный тип данных. Ожидается целое число или строка.")

    card_number = str(card_number).replace(" ", "")

    if len(card_number) != 16 or card_number.isalpha():
        logger.warning("Неверный номер карты: %s", card_number)
        return "Неверный номер карты"
    else:
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info("Успешно замаскирован номер карты: %s", masked_number)
        return masked_number


def get_mask_account(account_number: Union[int, str]) -> Union[str]:
    """Преобразует номер счёта в номер со '**' и четыре последних цифры"""
    if not isinstance(account_number, (int, str)):
        logger.error("Неверный тип данных для номера счета: %s", type(account_number))
        raise ValueError("Неверный тип данных. Ожидается целое число или строка.")

    account_number = str(account_number).replace(" ", "")

    if len(account_number) != 20 or account_number.isalpha():
        logger.warning("Неверный номер счета: %s", account_number)
        return "Неверный номер счета"
    else:
        masked_account = f"**{account_number[-4:]}"
        logger.info("Успешно замаскирован номер счета: %s", masked_account)
        return masked_account

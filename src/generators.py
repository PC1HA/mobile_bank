from typing import Any, Dict, List, Iterator, Union


def filter_by_currency(transactions: List[Dict[str, Any]], currency_code: str) -> Iterator[Dict[str, Any]]:
    """
    Функция принимает список транзакций в виде списка(словарь(транзакция)) и возвращает транзакцию(итератор)
    если Валюта в транзакции совпадает с запросом "currency_code"
    """
    if not isinstance(transactions, list):

        raise ValueError("Входные данные должны быть списком.")

    if len(transactions) == 0:

        yield "Список транзакций пуст."
        return

    for transaction in transactions:

        if not isinstance(transaction, dict):
            continue

        operation_amount = transaction.get('operationAmount')

        if isinstance(operation_amount, dict) and 'currency' in operation_amount:

            currency_info = operation_amount.get('currency')

            if isinstance(currency_info, dict) and 'code' in currency_info:

                if currency_info['code'].upper() == currency_code.upper():

                    yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Функция принимает список операций и возвращает описание операции в виде строки
    """
    if not isinstance(transactions, list):

        raise ValueError("Входные данные должны быть списком.")

    if len(transactions) == 0:

        yield "Список транзакций пуст."
        return

    for transaction in transactions:

        if not isinstance(transaction, dict):
            continue

        if isinstance(transaction.get("description"), str):

            yield transaction['description']


def card_number_generator(start: Union[int, str], stop: Union[int, str]) -> Union[str]:
    """
    Функция генерирует номер карты по заданному диапазону, если start > stop, будет вызвано исключение
    """
    def to_int(value):
        """
        Функция проверяет, являются ли start и stop целыми числами или строкой.
        Строки преобразует в числа
        Во всех остальных случаях вызывает исключение
        """
        if isinstance(value, int):
            return value
        elif isinstance(value, str):
            stripped_value = value.strip()
            parts = stripped_value.split()
            concatenated_number = ''.join(parts)

            if concatenated_number.isdigit():

                return int(concatenated_number)

            else:
                raise ValueError("Параметры должны содержать только целые числа.")

        else:
            raise ValueError("Параметры должны быть целыми числами или строками, содержащими числа.")

    start = to_int(start)
    stop = to_int(stop)

    if start > stop:
        raise ValueError("Параметр start должен быть меньше или равен параметру end.")

    for number in range(start, stop + 1):

        formatted_number = f"{number:016}"

        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:16]}"

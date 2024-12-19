from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Функция, которая принимает список словарей и значение для ключа "state",
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ "state" соответствует указанному значению
    """
    filter_operations = []

    for transaction in transactions:
        if transaction["state"] == state:
            filter_operations.append(transaction)

    return filter_operations


def sort_by_date(transactions: List[Dict[str, Any]], sort_order: bool = False) -> List[Dict[str, Any]]:
    """
    Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)
    и возвращает новый список, отсортированный по дате
    """

    return sorted(transactions, key=lambda transaction: transaction.get("date", datetime.min), reverse=sort_order)

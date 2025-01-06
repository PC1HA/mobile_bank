from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(transactions: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Функция, которая принимает список словарей и значение для ключа "state",
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ "state" соответствует указанному значению
    """
    filter_operations = []

    if not isinstance(transactions, List):

        raise ValueError("Неверный тип данных, ожидается List(список)")

    if not isinstance(state, str):

        raise ValueError("Неверный state")

    for transaction in transactions:
        if not isinstance(transaction, Dict):

            raise ValueError("Неверный тип данных, ожидается List[Dict](список[словарь])")

        if set(transaction.keys()) != {"id", "state", "date"}:

            continue

        elif "state" not in transaction:
            continue

        elif transaction["state"].upper() == state.upper():
            filter_operations.append(transaction)

    return filter_operations


def sort_by_date(transactions: List[Dict[str, Any]], sort_order: bool = True) -> List[Dict[str, Any]]:
    """
    Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)
    и возвращает новый список, отсортированный по дате
    """
    if not isinstance(transactions, List):

        raise ValueError("Неверный тип данных, ожидается List(список)")

    filtered_transactions = []

    for transaction in transactions:
        if isinstance(transaction, dict) and "date" in transaction:
            date_str = transaction["date"]
            try:
                datetime.fromisoformat(date_str)
                filtered_transactions.append(transaction)
            except ValueError:
                continue

    return sorted(filtered_transactions, key=lambda t: t["date"], reverse=sort_order)

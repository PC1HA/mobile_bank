from typing import Any, Dict, List


def filter_by_state(list_of_dictionaries: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """
    Функция, которая принимает список словарей и значение для ключа "state",
    и возвращает новый список словарей, содержащий только те словари,
    у которых ключ "state" соответствует указанному значению
    """
    filter_list = []

    for some_dictionary in list_of_dictionaries:
        if some_dictionary["state"] == state:
            filter_list.append(some_dictionary)

    return filter_list

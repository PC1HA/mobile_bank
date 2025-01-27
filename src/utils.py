import json
import os
from typing import Any, Dict, List


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о транзакциях из JSON-файла.

    Args:
        file_path (str): Путь к файлу JSON.

    Returns:
        List[Dict[str, Any]]: Список словарей с данными о транзакциях,
        или пустой список, если файл не найден, пуст или не является списком.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, OSError):
        return []

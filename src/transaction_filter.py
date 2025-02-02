import re
from collections import Counter
from typing import Dict, List


def search_transactions(transactions: List[Dict[str, str]], search_string: str) -> List[Dict[str, str]]:
    """Находит транзакции по заданной строке в описании."""
    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction['description'])]


def count_operations_by_category(transactions: List[Dict[str, str]]) -> Dict[str, int]:
    """Подсчитывает количество транзакций по категориям."""
    counter = Counter(transaction['category'] for transaction in transactions)
    return dict(counter)

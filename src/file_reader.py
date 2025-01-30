import csv
from typing import Dict, List

import pandas as pd


def read_financial_operations_csv(file_path: str) -> List[Dict[str, str]]:
    """Считывает финансовые операции из CSV файла.

    Args:
        file_path (str): Путь к файлу CSV.

    Returns:
        List[Dict[str, str]]: Список словарей с транзакциями.
    """
    transactions = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(row)
    return transactions


def read_financial_operations_xlsx(file_path: str) -> List[Dict[str, str]]:
    """Считывает финансовые операции из Excel файла.

    Args:
        file_path (str): Путь к файлу Excel.

    Returns:
        List[Dict[str, str]]: Список словарей с транзакциями.
    """
    df = pd.read_excel(file_path)
    transactions = df.to_dict(orient='records')

    return [{str(k): str(v) for k, v in transaction.items()} for transaction in transactions]

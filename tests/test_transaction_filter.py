import unittest
from typing import Dict, List

from src.transaction_filter import count_operations_by_category, search_transactions


class TestTransactionFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.transactions: List[Dict[str, str]] = [
            {
                'date': '2023-01-01',
                'description': 'Транзакция на покупку',
                'category': 'Покупка'
            },
            {
                'date': '2023-01-02',
                'description': 'Перевод между счетами',
                'category': 'Перевод'
            },
            {
                'date': '2023-01-03',
                'description': 'Транзакция на оплату услуг',
                'category': 'Оплата'
            },
            {
                'date': '2023-01-04',
                'description': 'Транзакция на покупку продуктов',
                'category': 'Покупка'
            },
        ]

    def test_search_transactions(self) -> None:
        result = search_transactions(self.transactions, 'покупку')
        self.assertEqual(len(result), 2)  # Две транзакции связаны с покупками
        self.assertEqual(result[0]['description'], 'Транзакция на покупку')
        self.assertEqual(result[1]['description'], 'Транзакция на покупку продуктов')

    def test_count_operations_by_category(self) -> None:
        result = count_operations_by_category(self.transactions)
        self.assertEqual(result['Покупка'], 2)  # Две транзакции в категории 'Покупка'
        self.assertEqual(result['Перевод'], 1)   # Одна транзакция в категории 'Перевод'
        self.assertEqual(result['Оплата'], 1)    # Одна транзакция в категории 'Оплата'
        self.assertEqual(len(result), 3)          # Всего три уникальные категории

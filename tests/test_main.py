import unittest
from typing import Dict, List, Union

from main import (filter_by_currency, filter_by_description, filter_transactions_by_status, print_transactions,
                  sort_transactions)


class TestTransactionFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.transactions: List[Dict[str, Union[str, float]]] = [
            {
                'date': '2023-01-01',
                'description': 'Тестовая транзакция 1',
                'account': '123456',
                'amount': 100.0,
                'currency': 'RUB',
                'status': 'EXECUTED'
            },
            {
                'date': '2023-01-02',
                'description': 'Тестовая транзакция 2',
                'account': '123457',
                'amount': 200.0,
                'currency': 'USD',
                'status': 'CANCELED'
            },
            {
                'date': '2023-01-03',
                'description': 'Тестовая транзакция 3',
                'account': '123458',
                'amount': 300.0,
                'currency': 'RUB',
                'status': 'PENDING'
            }
        ]

    def test_filter_transactions_by_status(self) -> None:
        result = filter_transactions_by_status(self.transactions, 'EXECUTED')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['description'], 'Тестовая транзакция 1')

    def test_sort_transactions(self) -> None:
        sorted_transactions = sort_transactions(self.transactions, 'по возрастанию')
        self.assertEqual(sorted_transactions[0]['date'], '2023-01-01')

    def test_filter_by_currency(self) -> None:
        result = filter_by_currency(self.transactions, 'RUB')
        self.assertEqual(len(result), 2)  # Транзакции с RUB - транзакция 1 и 3

    def test_filter_by_description(self) -> None:
        result = filter_by_description(self.transactions, 'транзакция 1')
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['description'], 'Тестовая транзакция 1')

    def test_print_transactions(self) -> None:
        # Здесь вы можете использовать mock для проверки вывода
        from unittest.mock import patch
        with patch('builtins.print') as mocked_print:
            print_transactions(self.transactions)
            mocked_print.assert_called()

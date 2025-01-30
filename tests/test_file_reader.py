import unittest
from typing import Any, Dict, List
from unittest.mock import mock_open, patch

import pandas as pd

from src.file_reader import read_financial_operations_csv, read_financial_operations_xlsx


class TestFileReader(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='date,amount\n2022-01-01,100\n2022-01-02,200\n')
    def test_read_financial_operations_csv(self, mock_file: Any) -> None:
        expected: List[Dict[str, str]] = [{'date': '2022-01-01', 'amount': '100'},
                                          {'date': '2022-01-02', 'amount': '200'}]
        result: List[Dict[str, str]] = read_financial_operations_csv('dummy_path.csv')
        self.assertEqual(result, expected)

    @patch('pandas.read_excel')
    def test_read_financial_operations_xlsx(self, mock_read_excel: Any) -> None:
        mock_read_excel.return_value = pd.DataFrame({'date': ['2022-01-01', '2022-01-02'], 'amount': [100, 200]})
        expected: List[Dict[str, str]] = [{'date': '2022-01-01', 'amount': '100'},
                                          {'date': '2022-01-02', 'amount': '200'}]
        result: List[Dict[str, str]] = read_financial_operations_xlsx('dummy_path.xlsx')
        self.assertEqual(result, expected)

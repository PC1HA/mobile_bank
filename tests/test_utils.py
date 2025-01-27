import json
import unittest
from typing import Any, Dict, List
from unittest import mock
from unittest.mock import mock_open

from src.utils import load_transactions


class TestLoadTransactions(unittest.TestCase):

    @mock.patch("builtins.open", new_callable=mock_open, read_data=json.dumps([{"id": 1, "amount": 100}]))
    @mock.patch("os.path.exists", return_value=True)
    def test_load_transactions_success(self, mock_exists: mock.Mock, mock_open: mock.Mock) -> None:
        file_path: str = "fake_path.json"
        result: List[Dict[str, Any]] = load_transactions(file_path)
        expected: List[Dict[str, Any]] = [{"id": 1, "amount": 100}]
        self.assertEqual(result, expected)
        mock_open.assert_called_once_with(file_path, 'r', encoding='utf-8')
        mock_exists.assert_called_once_with(file_path)

    @mock.patch("os.path.exists", return_value=False)
    def test_load_transactions_file_not_found(self, mock_exists: mock.Mock) -> None:
        file_path: str = "fake_path.json"
        result: List[Dict[str, Any]] = load_transactions(file_path)
        self.assertEqual(result, [])
        mock_exists.assert_called_once_with(file_path)

    @mock.patch("builtins.open", new_callable=mock_open, read_data="")
    @mock.patch("os.path.exists", return_value=True)
    def test_load_transactions_empty_file(self, mock_exists: mock.Mock, mock_open: mock.Mock) -> None:
        file_path: str = "fake_path.json"
        result: List[Dict[str, Any]] = load_transactions(file_path)
        self.assertEqual(result, [])
        mock_open.assert_called_once_with(file_path, 'r', encoding='utf-8')
        mock_exists.assert_called_once_with(file_path)

    @mock.patch("builtins.open", new_callable=mock_open, read_data="not a json")
    @mock.patch("os.path.exists", return_value=True)
    def test_load_transactions_invalid_json(self, mock_exists: mock.Mock, mock_open: mock.Mock) -> None:
        file_path: str = "fake_path.json"
        result: List[Dict[str, Any]] = load_transactions(file_path)
        self.assertEqual(result, [])
        mock_open.assert_called_once_with(file_path, 'r', encoding='utf-8')
        mock_exists.assert_called_once_with(file_path)

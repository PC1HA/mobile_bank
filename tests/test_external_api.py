import unittest
from unittest.mock import MagicMock, patch

from src.external_api import get_exchange_rate, get_transaction_amount_in_rub


class TestExchangeFunctions(unittest.TestCase):

    @patch("os.getenv", return_value="fake_api_key")
    @patch("requests.get")
    def test_get_exchange_rate_success(self, mock_get: MagicMock, mock_getenv: MagicMock) -> None:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "rates": {
                "RUB": 75.0
            }
        }

        base_currency: str = "USD"
        target_currency: str = "RUB"

        rate: float = get_exchange_rate(base_currency, target_currency)

        self.assertEqual(rate, 75.0)
        mock_get.assert_called_once_with(
            f"https://api.apilayer.com/exchangerates_data/latest?base={base_currency}&symbols={target_currency}",
            headers={"apikey": "fake_api_key"}
        )

    @patch("os.getenv", return_value="fake_api_key")
    @patch("requests.get")
    def test_get_exchange_rate_failure(self, mock_get: MagicMock, mock_getenv: MagicMock) -> None:
        mock_get.return_value.status_code = 400

        with self.assertRaises(Exception) as context:
            get_exchange_rate("USD", "RUB")

        self.assertEqual(str(context.exception), "Error fetching data from API")
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/latest?base=USD&symbols=RUB",
            headers={"apikey": "fake_api_key"}
        )

    @patch("src.external_api.get_exchange_rate", return_value=75.0)
    def test_get_transaction_amount_in_rub_rub_currency(self, mock_get_rate: MagicMock) -> None:
        transaction: dict = {"amount": 1000, "currency": "RUB"}

        result: float = get_transaction_amount_in_rub(transaction)

        self.assertEqual(result, 1000.0)
        mock_get_rate.assert_not_called()

    @patch("src.external_api.get_exchange_rate", return_value=75.0)
    def test_get_transaction_amount_in_rub_usd_currency(self, mock_get_rate: MagicMock) -> None:
        transaction: dict = {"amount": 100, "currency": "USD"}

        result: float = get_transaction_amount_in_rub(transaction)

        self.assertEqual(result, 7500.0)
        mock_get_rate.assert_called_once_with("USD", "RUB")

    @patch("src.external_api.get_exchange_rate", return_value=80.0)
    def test_get_transaction_amount_in_rub_eur_currency(self, mock_get_rate: MagicMock) -> None:
        transaction: dict = {"amount": 50, "currency": "EUR"}

        result: float = get_transaction_amount_in_rub(transaction)

        self.assertEqual(result, 4000.0)
        mock_get_rate.assert_called_once_with("EUR", "RUB")

    def test_get_transaction_amount_in_rub_unknown_currency(self) -> None:
        transaction: dict = {"amount": 100, "currency": "JPY"}

        result: float = get_transaction_amount_in_rub(transaction)

        self.assertEqual(result, 100.0)

import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def get_exchange_rate(base_currency: str, target_currency: str) -> float:
    """
    Получает текущий курс обмена из API.

    Args:
        base_currency (str): Исходная валюта.
        target_currency (str): Целевая валюта.

    Returns:
        float: Курс обмена.
    """
    api_key = os.getenv("EXCHANGE_RATES_API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/latest?base={base_currency}&symbols={target_currency}"

    headers = {
        "apikey": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        rate = data['rates'].get(target_currency)

        if rate is None:
            raise ValueError(f"Currency '{target_currency}' not found in response data")

        if isinstance(rate, (float, int)):
            return float(rate)
        else:
            raise TypeError("The exchange rate is not a valid number.")
    else:
        raise Exception("Error fetching data from API")


def get_transaction_amount_in_rub(transaction: Dict[str, Any]) -> float:
    """
    Получает сумму транзакции в рублях.

    Args:
        transaction (Dict[str, Any]): Транзакция с данными.

    Returns:
        float: Сумма транзакции в рублях.
    """
    amount = transaction.get("amount", 0.0)
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return float(amount)

    if currency in ["USD", "EUR"]:
        exchange_rate = get_exchange_rate(currency, "RUB")
        return float(amount) * exchange_rate

    return float(amount)

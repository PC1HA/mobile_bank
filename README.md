# Мобильный банк

## Краткое описание

Данный проект представляет собой совокупностью функций для банковских операций


## Установка и использование

- Для использования данной библиотеки необходимо иметь установленный Python версии 3.6 и выше.
Убедитесь, что у вас установлен пакет datetime, который входит в стандартную библиотеку Python.
- Склонируйте репозиторий:

    [git clone](https://github.com/PC1HA/mobile_bank.git)
- Убедитесь, что у вас установлен Python и необходимые библиотеки.
- Лучше всего будет использовать всё через файл main.py, пропишите импорты
    и данные, с которыми будете работать
- ```.env```
EXCHANGE_RATES_API_KEY=your_api_key_here
Вместо ```your_api_key_here``` вставьте свой ключ
## Примеры использования

### Файл main.py
Основной файл всего проекта, через который стоит работать и тестировать.
Пример для конфига ```main.py```

```
from src.processing import filter_by_state, sort_by_date
from src.widget.py import mask_account_card, git_date

if __name__ == "__main__":

```

- файл ```masks.py``` включен в импортах ```widget.py```

### Файл ```masks.py```


#### Пример использования функции get_mask_card_number:
```
card_number = "1234 5678 9012 3456"
masked_card = get_mask_card_number(card_number)
print(f"Маскированный номер карты: {masked_card}")
```
- Вывод: Маскированный номер карты: 1234 56** **** 3456


#### Пример использования функции get_mask_account:
```
account_number = "123456789012"
masked_account = get_mask_account(account_number)
print(f"Маскированный номер счета: {masked_account}")
```
- Вывод: Маскированный номер счета: **9012


### Файл ```widget.py```

#### Пример использования функции mask_account_card:
```
account_input = "Счет 123456789012"
masked_account = mask_account_card(account_input)
print(f"Маскированный номер счета: {masked_account}")
```
- Вывод: Маскированный номер счета: Счет **9012
```
card_input = "Visa 1234 5678 9012 3456"
masked_card = mask_account_card(card_input)
print(f"Маскированный номер карты: {masked_card}")
```
- Вывод: Маскированный номер карты: Visa 1234 56** **** 3456


#### Пример использования функции git_date:
```
date_input = "2023-10-01T12:30:45.123456"
formatted_date = git_date(date_input)
print(f"Отформатированная дата: {formatted_date}")
```
- Вывод: Отформатированная дата: 01.10.2023


### Файл ```processing.py```

- Пример данных

```
transactions = [
    {"state": "EXECUTED", "date": "2023-10-01T12:30:45.123456", "amount": 100},
    {"state": "CANCELLED", "date": "2023-09-30T10:15:30.123456", "amount": 200},
    {"state": "EXECUTED", "date": "2023-10-02T09:00:00.123456", "amount": 150},
]
```

- Фильтрация по состоянию:

```
filtered_transactions = filter_by_state(transactions)
print("Отфильтрованные транзакции:", filtered_transactions)
```

- Вывод: Отфильтрованные транзакции:

```
[
{'state': 'EXECUTED', 'date': '2023-10-01T12:30:45.123456','amount': 100},
{'state': 'EXECUTED', 'date': '2023-10-02T09:00:00.123456', 'amount': 150}
]
```

- Сортировка по дате

```
sorted_transactions = sort_by_date(filtered_transactions)
print("Отсортированные транзакции:", sorted_transactions)
```

- Вывод: Отсортированные транзакции:

```
[
{'state': 'EXECUTED', 'date': '2023-10-02T09:00:00.123456', 'amount': 150},
{'state': 'EXECUTED', 'date': '2023-10-01T12:30:45.123456', 'amount': 100}
]
```
### Файл ``` generators.py```

- Пример входных данных:

```
transacrions = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
]
```
#### Функция ```filter_by_currency()``` 
- Принимает список транзакций в виде list, который содержит словари
с транзакциями и возвращает транзакцию(и) по заданному значению валюты
- Пример:
```
if __name__ == "__main__":
    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
        try:
            print(next(usd_transactions))
        except StopIteration:
            print('Операции закончились')
            break
```
- Вывод:
```
{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```

#### Функция ```transaction_descriptions()```
- Принимает список транзакций list, и возвращает описание транзакций в нем
- Пример:
```
if __name__ == "__main__":
    name_transaction = transaction_descriptions(transaction)

    for _ in range(2):
        try:
            print(next(name_transaction))
        except StopIteration:
            print('Операции закончились')
            break
```
- Вывод:
```
Перевод организации
Перевод со счета на счет
```

#### Функция ```card_number_generator()```
- Функция генерирует 16-значный номер карты по заданному промежутку
начало start, конец stop
- ограничения: от 0 до 9999999999999999
- Пример:
```
for card_number in card_number_generator('  1 2 3  ', ' 1  2  4'):
    print(card_number)
```
- Вывод:
```
0000 0000 0000 0123
0000 0000 0000 0124
```

### Файл ```decorators.py```
Содержит в себе декоратор ```log()```, который автоматически регистрирует все детали
выполнения функций
- Пример использования:
- 
```
from src.decorators import log


if __name__ == "__main__":
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)

```

- Вывод в консоль:

```
2025-01-08 20:46:37,523 - Calling my_function with args: (1, 2), kwargs: {}
2025-01-08 20:46:37,523 - my_function returned 3 in 0.0001 seconds
```

### Файл ```utils.py```
Загружает данные о транзакциях из JSON-файла

- Пример использования
```
from src.utils import load_transactions

if __name__ == "__main__":
    path = 'data/operations.json'
    transactions = load_transactions(path)
    
    if transactions:
        print("Транзакции загружены:")
        for transaction in transactions:
            print(transaction)
    else:
        print("Не удалось загрузить транзакции или файл пуст.")
```

### Файл ```external_api.py```

#### Функция ```get_exchange_rate```

Получает текущий курс обмена из API

#### Функция ```get_transaction_amount_in_rub```

Получает сумму транзакции в рублях

- Пример
```
from src.external_api import get_transaction_amount_in_rub

if __name__ == "__main__":
    # Пример транзакции
    transaction = {
        "amount": 100.0,
        "currency": "USD"
    }
    
    amount_in_rub = get_transaction_amount_in_rub(transaction)
    print(f"Сумма транзакции в рублях: {amount_in_rub:.2f}")
```
## Ветка тестирования кода

### Папка tests
В ней отрабатываются возможные входные данные по
```masks.py```, ```widget.py```, ```processing.py```, ```generators.py```

#### Пример тестирования ```masks.py``` в ```test_masks.py```
```
@pytest.fixture
def mask_account_number() -> str:
    return "**4305"


@pytest.fixture()
def mask_card_number() -> str:
    return "7000 79** **** 6361"


@pytest.fixture()
def incorrect_number() -> str:
    return "Неверный номер карты"


@pytest.fixture()
def incorrect_account() -> str:
    return "Неверный номер счета"


def test_mask_card_number(mask_card_number: str) -> None:
    assert get_mask_card_number("7000792289606361") == mask_card_number
    assert get_mask_card_number("70 007 92289 6063 61") == mask_card_number
    assert get_mask_card_number(7000792289606361) == mask_card_number


def test_mask_account_number(mask_account_number: str) -> None:
    assert get_mask_account(73654108430135874305) == mask_account_number
    assert get_mask_account("73654108430135874305") == mask_account_number
    assert get_mask_account("73    6541 084301358743 05") == mask_account_number


def test_incorrect_number(incorrect_number: str) -> None:
    assert get_mask_card_number("transactionsaaaa") == incorrect_number
    assert get_mask_card_number(14345454363636346346346) == incorrect_number
    assert get_mask_card_number(121231) == incorrect_number


def test_incorrect_account(incorrect_account: str) -> None:
    assert get_mask_account("") == incorrect_account
    assert get_mask_account(73654108430) == incorrect_account
    assert get_mask_account("fatgpvktjfkvlfotfvfd") == incorrect_account
```

#### Пример тестирования ```widget.py``` в ```test_widget.py```

```
@pytest.fixture()
def normal_data() -> str:
    return "03.07.2019"


@pytest.fixture()
def zero_date() -> str:
    return "Неверные данные"


@pytest.fixture()
def mask_account() -> str:
    return "Счет **4305"


@pytest.fixture()
def mask_card_maestro() -> str:
    return "Maestro 7000 79** **** 6361"


@pytest.fixture()
def mask_card_visa() -> str:
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture()
def incorrect_data() -> str:
    return "Неверные данные"


@pytest.fixture()
def isdigit_data() -> str:
    return "Неверные данные, возможно вы сначала ввели номер Счета или Карты"


def test_mask_account(mask_account: str) -> None:
    assert mask_account_card("Счет 73654108430135874305") == mask_account
    assert mask_account_card("Счет73654108430135874305") == mask_account
    assert mask_account_card("Счет     73654108430135874305") == mask_account
    assert mask_account_card("Сч  ет73 65410  8430135  8743 05") == mask_account
    assert mask_account_card("Счёт 73654108430135874305") == mask_account
    assert mask_account_card("счет73654108430135874305") == mask_account
    assert mask_account_card("счёт73654108430135874305") == mask_account
    assert mask_account_card("СЧЕТ73654108430135874305") == mask_account
    assert mask_account_card("СЧЁТ73654108430135874305") == mask_account
    assert mask_account_card("Счёт73654108430135874305") == mask_account
    assert mask_account_card("сч ёт73 654108 4301358 74305") == mask_account
    assert mask_account_card("счЁт73654108430135874305") == mask_account
    assert mask_account_card("счЕт73654108430135874305") == mask_account
    assert mask_account_card("    счёт73654108430135874305    ") == mask_account


def test_mask_card_maestro(mask_card_maestro: str) -> None:
    assert mask_account_card("Maestro 7000792289606361") == mask_card_maestro
    assert mask_account_card("maestro 7000792289606361") == mask_card_maestro
    assert mask_account_card("Maestro7000792289606361") == mask_card_maestro
    assert mask_account_card("MAESTRO 7000792289606361") == mask_card_maestro
    assert mask_account_card("MAESTRO7000792289606361") == mask_card_maestro
    assert mask_account_card("mAestro 7000792289606361") == mask_card_maestro
    assert mask_account_card("mAestro7000792289606361") == mask_card_maestro
    assert mask_account_card("Ma estr o 7000 7922 89606 361") == mask_card_maestro
    assert mask_account_card("    Maestro 7000792289606361   ") == mask_card_maestro


def test_mask_card_visa(mask_card_visa: str) -> None:
    assert mask_account_card("Visa Platinum 7000792289606361") == mask_card_visa
    assert mask_account_card("visa platinum 7000792289606361") == mask_card_visa
    assert mask_account_card("VISA PLATINUM 7000792289606361") == mask_card_visa
    assert mask_account_card("VisaPlatinum 7000792289606361") == mask_card_visa
    assert mask_account_card("VisaPlatinum7000792289606361") == mask_card_visa
    assert mask_account_card("visaplatinum 7000792289606361") == mask_card_visa
    assert mask_account_card("visaplatinum7000792289606361") == mask_card_visa
    assert mask_account_card("VISAPLATINUM 7000792289606361") == mask_card_visa
    assert mask_account_card("VISAPLATINUM7000792289606361") == mask_card_visa
    assert mask_account_card(" V is a Pla tin um 70 00792 289606 361 ") == mask_card_visa
    assert mask_account_card(" v is a p la tinu m 700 0792 289606 361 ") == mask_card_visa
    assert mask_account_card("V I SA P LAT INUM 700 079228 96063 61 ") == mask_card_visa


def test_incorrect_data(incorrect_data: str) -> None:
    assert mask_account_card("     Platinum 7000792289606361") == incorrect_data
    assert mask_account_card("Visa          7000792289606361") == incorrect_data
    assert mask_account_card("Visa Maestro  7000792289606361") == incorrect_data
    assert mask_account_card("isa Platinum 7000792289606361") == incorrect_data


def test_isdigit_data(isdigit_data: str) -> None:
    assert mask_account_card("7000792289606361 Visa Platinum") == isdigit_data
    assert mask_account_card("73654108430135874305 Счет") == isdigit_data
    assert mask_account_card("7000792289606361 Maestro") == isdigit_data


def test_error_account_number() -> None:
    with pytest.raises(ValueError) as exc_info:
        mask_account_card(1244545)  # type: ignore
        mask_account_card([])  # type: ignore
        mask_account_card({})  # type: ignore
        mask_account_card(())  # type: ignore

    assert str(exc_info.value) == "Неверный тип данных, ожидается ТОЛЬКО строка: str!"


def test_normal_data(normal_data: str) -> None:
    assert git_date("2019-07-03T18:35:29.512364") == normal_data
    assert git_date("2019-07-03") == normal_data


def test_zero_date(zero_date: str) -> None:
    assert git_date("0000-07-03") == zero_date
    assert git_date("2019-00-03") == zero_date
    assert git_date("2019-07-00") == zero_date
    assert git_date("2019-0a-03") == zero_date
    assert git_date("20a9-01-03") == zero_date
    assert git_date("2019-01-a3") == zero_date
    assert git_date("20190003") == zero_date
    assert git_date("2019:00:03") == zero_date


def test_error_git_data() -> None:
    with pytest.raises(ValueError) as exc_info:
        git_date(1243435)  # type: ignore
        git_date([])  # type: ignore
        git_date({})  # type: ignore
        git_date(())  # type: ignore

    assert str(exc_info.value) == "Неверный тип данных, ожидается ТОЛЬКО строка: str!"
    
```

#### Пример тестирования ```processing.py``` в ```test_processing.py```
```
def test_list_filter_by_state() -> None:
    with pytest.raises(ValueError) as exc_info:
        filter_by_state(123443)  # type: ignore
        filter_by_state("frrg")  # type: ignore
        filter_by_state(())  # type: ignore
        filter_by_state({})  # type: ignore
        filter_by_state([], 124)  # type: ignore
        filter_by_state(["rrrt"])  # type: ignore
        filter_by_state() # type: ignore
    assert str(exc_info.value) == "Неверный тип данных, ожидается List(список)"


def test_list_sort_by_date() -> None:
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(123443)  # type: ignore
        sort_by_date("frrg")  # type: ignore
        sort_by_date(())  # type: ignore
        sort_by_date({})  # type: ignore

    assert str(exc_info.value) == "Неверный тип данных, ожидается List(список)"


def test_error_state() -> None:
    with pytest.raises(ValueError) as exc_info:
        filter_by_state([{}], 1213)  # type: ignore
        filter_by_state([], [])  # type: ignore
        filter_by_state([], {})  # type: ignore
        filter_by_state([], ())  # type: ignore

    assert str(exc_info.value) == "Неверный state"


@pytest.mark.parametrize(
    "a, b, c",
    [
        (
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
            "EXECUTED",
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
            "executed",
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], "CANCELED", []),
        ([{"id": 41428829, "date": "2019-07-03T18:35:29.512364"}], "EXECUTED", []),
        ([{"state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], "EXECUTED", []),
        ([{"id": 41428829, "state": "EXECUTED"}], "EXECUTED", []),
        ([], "EXECUTED", []),
    ],
)
def test_filter_by_state(a: list, b: str, c: list) -> None:
    assert filter_by_state(a, b) == c


@pytest.fixture()
def sort_date() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_date(sort_date: list) -> None:
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"state": "CANCELED", "state": "CANCELED", "state": "EXECUTED"},  # noqa
                {"id": 615064591, "state": "CANCELED", "state": "CANCELED", "state": "EXECUTED"},  # noqa
                {"id": 615064591, "state": "CANCELED", "date": "aaaa-10-14T08:21:33.419441"},
            ]
        )
        == sort_date
    )

    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
        == sort_date
    )


@pytest.fixture()
def revers_sort_data() -> list:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_revers_sort_data(revers_sort_data: list) -> None:
    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"state": "CANCELED", "state": "CANCELED", "state": "EXECUTED"},  # noqa
                {"id": 615064591, "state": "CANCELED", "state": "CANCELED", "state": "EXECUTED"},  # noqa
                {"id": 615064591, "state": "CANCELED", "date": "aaaa-10-14T08:21:33.419441"},
            ],
            False,
        )
        == revers_sort_data
    )

    assert (
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            False,
        )
        == revers_sort_data
    )


@pytest.fixture()
def zero_list_date() -> list:
    return []


def test_zero_list_date(zero_list_date: list) -> None:
    assert sort_by_date([]) == zero_list_date
    assert sort_by_date([{}]) == zero_list_date
    assert (
        sort_by_date(
            [
                {"state": "CANCELED", "state": "CANCELED", "state": "EXECUTED"},  # noqa
                {"id": 615064591, "state": "CANCELED", "state": "CANCELED", "state": "EXECUTED"},  # noqa
                {"id": 615064591, "state": "CANCELED", "date": "aaaa-10-14T08:21:33.419441"},
            ]
        )
        == zero_list_date
    )

```

#### Пример тестирования ```generators.py``` в ```test_generators.py```

```
import pytest
from typing import Any, Dict, List, Union

from src.generators import filter_by_currency, card_number_generator, transaction_descriptions

@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    return [
        {
            "description": "Transaction 1",
            "operationAmount": {
                "amount": 100,
                "currency": {"code": "USD"}
            }
        },
        {
            "description": "Transaction 2",
            "operationAmount": {
                "amount": 200,
                "currency": {"code": "EUR"}
            }
        },
        {
            "description": "Transaction 3",
            "operationAmount": {
                "amount": 300,
                "currency": {"code": "USD"}
            }
        }
    ]

@pytest.mark.parametrize(
    "currency_code, expected_descriptions",
    [
        ("USD", ["Transaction 1", "Transaction 3"]),
        ("EUR", ["Transaction 2"]),
        ("GBP", [])
    ]
)
def test_filter_by_currency(
    sample_transactions: List[Dict[str, Any]],
    currency_code: str,
    expected_descriptions: List[str]
) -> None:
    filtered_transactions = list(filter_by_currency(sample_transactions, currency_code))
    result_descriptions = [t['description'] for t in filtered_transactions]
    assert result_descriptions == expected_descriptions

def test_filter_by_currency_empty_list() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == ["Список транзакций пуст."]

def test_filter_by_currency_invalid_input() -> None:
    with pytest.raises(ValueError) as excinfo:
        list(filter_by_currency("invalid", "USD"))
    assert str(excinfo.value) == "Входные данные должны быть списком."

def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]) -> None:
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Transaction 1", "Transaction 2", "Transaction 3"]

def test_transaction_descriptions_empty_list() -> None:
    result = list(transaction_descriptions([]))
    assert result == ["Список транзакций пуст."]

def test_transaction_descriptions_invalid_input() -> None:
    with pytest.raises(ValueError) as excinfo:
        list(transaction_descriptions("invalid"))
    assert str(excinfo.value) == "Входные данные должны быть списком."

@pytest.mark.parametrize(
    "start, stop, expected_output",
    [
        (" 1 2 3 ", " 1 2 4 ", ["0000000000000123", "0000000000000124"]),
        (1, 5, ["0000000000000001", "0000000000000002",
                 "0000000000000003", "0000000000000004",
                 "0000000000000005"]),
        ("10", "12", ["0000000000000010",
                       "0000000000000011",
                       "0000000000000012"])
    ]
)
def test_card_number_generator(
    start: Union[str, int],
    stop: Union[str, int],
    expected_output: List[str]
) -> None:
    generated_numbers = list(card_number_generator(start, stop))
    assert generated_numbers == [
        f"{num[:4]} {num[4:8]} {num[8:12]} {num[12:16]}"
        for num in expected_output
    ]

def test_card_number_generator_empty_range() -> None:
    with pytest.raises(ValueError) as excinfo:
        list(card_number_generator("10", "5"))
    assert str(excinfo.value) == "Параметр start должен быть меньше " \
                                   "или равен параметру end."

def test_card_number_generator_invalid_input() -> None:
    with pytest.raises(ValueError) as excinfo:
        list(card_number_generator("1a", "5"))
    assert str(excinfo.value) == "Параметры должны содержать только " \
                                   "целые числа."

```

#### Пример тестирования ```decorators.py``` в ```test_decorators.py```

```
from typing import Iterator

import pytest

from src.decorators import log
from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def setup_logging(caplog: pytest.LogCaptureFixture) -> Iterator:
    yield caplog


def test_function_logging(setup_logging: pytest.LogCaptureFixture) -> None:
    @log()
    def test_function(x: int, y: int) -> int:
        return x + y

    result = test_function(3, 4)

    assert result == 7
    assert "Calling test_function with args: (3, 4), kwargs: {}" in setup_logging.text
    assert "test_function returned 7" in setup_logging.text


def test_function_error_logging(setup_logging: pytest.LogCaptureFixture) -> None:
    @log()
    def faulty_function(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        faulty_function(1, 0)

    assert "Calling faulty_function with args: (1, 0), kwargs: {}" in setup_logging.text
    assert "faulty_function raised ZeroDivisionError" in setup_logging.text  # Проверка на ошибку


@log()
def test_get_mask_card_number_valid() -> None:
    assert get_mask_card_number(1234567812345678) == "1234 56** **** 5678"
    assert get_mask_card_number("1234 5678 1234 5678") == "1234 56** **** 5678"


@log()
def test_get_mask_card_number_invalid() -> None:
    assert get_mask_card_number("1234 5678 1234") == "Неверный номер карты"
    assert get_mask_card_number("some_invalid_string") == "Неверный номер карты"
    assert get_mask_card_number(123) == "Неверный номер карты"

    with pytest.raises(ValueError, match="Неверный тип данных. Ожидается целое число или строка."):
        get_mask_card_number([])  # type: ignore


@log()
def test_get_mask_account_valid() -> None:
    assert get_mask_account(12345678901234567890) == "**7890"
    assert get_mask_account("12345678901234567890") == "**7890"


@log()
def test_get_mask_account_invalid() -> None:
    assert get_mask_account("1234567890123456789") == "Неверный номер счета"
    assert get_mask_account("invalid_account") == "Неверный номер счета"
    assert get_mask_account(123) == "Неверный номер счета"

    with pytest.raises(ValueError, match="Неверный тип данных. Ожидается целое число или строка."):
        get_mask_account([])  # type: ignore

```
#### Пример тестирования ```utils.py``` в ```test_utils.py```

```
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

```
#### Пример тестирования ```external_api.py``` в ```test_external_api.py```

```
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

```

## Лицензия

### MIT License

**Copyright (c) 2024 Попов Илья Игоревич**

*Разрешение предоставляется, бесплатно, любому, кто получает копию этого программного обеспечения и*
*связанных с ним документов (далее — "Программное обеспечение"), использовать Программное обеспечение без ограничений,*
*включая, но не ограничиваясь правами на использование, копирование, изменение, слияние, публикацию, распространение,*
*сублицензирование и/или продажу копий Программного обеспечения, а также разрешение лицам,*
*которым предоставляется Программное обеспечение, делать это, при соблюдении следующих условий:*

*Вышеуказанное уведомление о авторских правах и это разрешение должны быть включены во все копии или*
*значительные части Программного обеспечения.*

*Программное обеспечение предоставляется "как есть", без каких-либо гарантий, явных или подразумеваемых, включая,*
*но не ограничиваясь, гарантии товарной пригодности, соответствия определенной цели и ненарушения.*
*В любом случае авторы или правообладатели не несут ответственности за любые претензии, ущерб или*
*другие обязательства, будь то в действии, контракте или ином, возникающие из,*
*в связи с или в результате использования Программного обеспечения или других действий с ним.*
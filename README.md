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
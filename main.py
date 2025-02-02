from typing import Any, Dict, List

from src.file_reader import read_financial_operations_csv, read_financial_operations_xlsx
from src.utils import load_transactions


def filter_transactions_by_status(transactions: List[Dict[str, Any]], status: str) -> List[Dict[str, Any]]:
    """Фильтрует транзакции по статусу."""
    return [transaction for transaction in transactions if
            isinstance(transaction['status'], str) and transaction['status'].lower() == status.lower()]


def sort_transactions(transactions: List[Dict[str, Any]], order: str) -> List[Dict[str, Any]]:
    """Сортирует транзакции по дате."""
    return sorted(transactions, key=lambda x: x['date'], reverse=(order == 'по убыванию'))


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str) -> List[Dict[str, Any]]:
    """Фильтрует транзакции по валюте."""
    return [transaction for transaction in transactions if transaction['currency'] == currency]


def filter_by_description(transactions: List[Dict[str, Any]], keyword: str) -> List[Dict[str, Any]]:
    """Фильтрует транзакции по слову в описании."""
    return [transaction for transaction in transactions if
            isinstance(transaction['description'], str) and keyword.lower() in transaction['description'].lower()]


def print_transactions(transactions: List[Dict[str, Any]]) -> None:
    """Выводит список транзакций."""
    print(f"\nВсего банковских операций в выборке: {len(transactions)}")
    for transaction in transactions:
        print(
            f"{transaction['date']} {transaction['description']}"
            f"\nСчет **{transaction['account']}\nСумма: {transaction['amount']} {transaction['currency']}\n"
        )


def main() -> None:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Ваш выбор: ")

    transactions: List[Dict[str, Any]] = []  # Объявление переменной
    if choice == '1':
        json_file_path = input("Введите путь к JSON-файлу: ")
        transactions = load_transactions(json_file_path)
        print("Для обработки выбран JSON-файл.")
    elif choice == '2':
        csv_file_path = input("Введите путь к CSV-файлу: ")
        transactions = read_financial_operations_csv(csv_file_path)
        print("Для обработки выбран CSV-файл.")
    elif choice == '3':
        xlsx_file_path = input("Введите путь к XLSX-файлу: ")
        transactions = read_financial_operations_xlsx(xlsx_file_path)
        print("Для обработки выбран XLSX-файл.")
    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")
        return

    available_statuses: List[str] = ['EXECUTED', 'CANCELED', 'PENDING']

    if transactions:
        filtered_transactions: List[Dict[str, Any]] = []  # Объявляем переменную перед использованием
        while True:
            status = input(
                "Введите статус, по которому необходимо выполнить фильтрацию."
                " Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
            )
            if status.upper() not in available_statuses:
                print(f"Статус операции \"{status}\" недоступен.")
                continue
            filtered_transactions = filter_transactions_by_status(transactions, status)
            print(f"Операции отфильтрованы по статусу \"{status}\".")
            break

        if filtered_transactions:
            sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
            if sort_choice == 'да':
                order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
                if order in ['по возрастанию', 'по убыванию']:
                    filtered_transactions = sort_transactions(filtered_transactions, order)

            currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
            if currency_choice == 'да':
                filtered_transactions = filter_by_currency(filtered_transactions, 'RUB')

            description_choice = input(
                "Отфильтровать список транзакций по определенному слову в описании? Да/Нет: "
            ).strip().lower()
            if description_choice == 'да':
                keyword = input("Введите слово для фильтрации: ")
                filtered_transactions = filter_by_description(filtered_transactions, keyword)

            if filtered_transactions:
                print("Распечатываю итоговый список транзакций...")
                print_transactions(filtered_transactions)
            else:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        else:
            print(f"Нет операций с статусом \"{status}\".")

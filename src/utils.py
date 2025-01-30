import json
import logging
import os
from typing import Any, Dict, List

log_directory = 'logs'
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logging.basicConfig(
    filename=os.path.join(log_directory, 'utils.log'),
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filemode='w'
)

logger = logging.getLogger(__name__)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает данные о транзакциях из JSON-файла.

    Args:
        file_path (str): Путь к файлу JSON.

    Returns:
        List[Dict[str, Any]]: Список словарей с данными о транзакциях,
        или пустой список, если файл не найден, пуст или не является списком.
    """
    if not os.path.exists(file_path):
        logger.warning(f"Файл не найден: {file_path}")
        return []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info(f"Успешно загружены {len(data)} транзакций из файла: {file_path}")
                return data
            logger.warning(f"Данные в файле {file_path} не являются списком.")
            return []
    except (json.JSONDecodeError, OSError) as e:
        logger.error(f"Ошибка при загрузке данных из файла {file_path}: {e}")
        return []

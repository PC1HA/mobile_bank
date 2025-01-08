import functools
import logging
import sys
import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор автоматически регистрирует детали выполнения функций.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if not logger.hasHandlers():
        stream_handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("%(asctime)s - %(message)s")
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        if filename:
            file_handler = logging.FileHandler(filename)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.time()
            try:
                logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
                result = func(*args, **kwargs)
                end_time = time.time()
                elapsed_time = end_time - start_time
                logging.info(f"{func.__name__} returned {result} in {elapsed_time:.4f} seconds")
                return result
            except Exception as e:
                end_time = time.time()
                elapsed_time = end_time - start_time
                logging.error(
                    f"{func.__name__} raised {type(e).__name__} with args: {args}, "
                    f"kwargs: {kwargs} in {elapsed_time:.4f} seconds: {e}"
                )
                raise

        return wrapper

    return decorator

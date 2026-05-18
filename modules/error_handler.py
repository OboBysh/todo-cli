"""
Модуль централизованной обработки ошибок.
Содержит пользовательские исключения и декоратор для перехвата ошибок в CLI.
"""

import sys
from functools import wraps

# Пользовательские исключения
class TaskNotFoundError(Exception):
    """Задача с указанным ID не найдена."""
    pass

class InvalidInputError(Exception):
    """Некорректный ввод пользователя."""
    pass

class FileOperationError(Exception):
    """Ошибка при работе с файлом."""
    pass

def handle_errors(func):
    """
    Декоратор для обработки ошибок в CLI-функциях.
    Перехватывает известные исключения и выводит сообщение в stderr.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TaskNotFoundError as e:
            print(f"❌ Ошибка: {e}", file=sys.stderr)
            return None
        except InvalidInputError as e:
            print(f"⚠️  Неверный ввод: {e}", file=sys.stderr)
            return None
        except FileOperationError as e:
            print(f"📁 Ошибка файла: {e}", file=sys.stderr)
            return None
        except Exception as e:
            # Неожиданная ошибка
            print(f"🔥 Непредвиденная ошибка: {e}", file=sys.stderr)
            # В реальном проекте можно добавить логирование в файл
            return None
    return wrapper

def log_error(message: str, error: Exception = None):
    """Простое логирование ошибок (пока в stderr)."""
    print(f"[ERROR] {message}", file=sys.stderr)
    if error:
        print(f"  → {error}", file=sys.stderr)

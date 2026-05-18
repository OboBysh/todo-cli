"""
Модуль для работы с файловым хранилищем задач (JSON).
"""

import json
import os
from typing import List, Dict

DEFAULT_FILE = "tasks.json"

def load_tasks(filepath: str = DEFAULT_FILE) -> List[Dict]:
    """
    Загружает список задач из JSON-файла.
    Если файл не существует или повреждён, возвращает пустой список.
    """
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            tasks = json.load(f)
            # Проверяем, что загрузился именно список
            if isinstance(tasks, list):
                return tasks
            else:
                print(f"Warning: {filepath} does not contain a list. Returning empty list.")
                return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading tasks from {filepath}: {e}. Starting with empty list.")
        return []

def save_tasks(tasks: List[Dict], filepath: str = DEFAULT_FILE) -> bool:
    """
    Сохраняет список задач в JSON-файл.
    Возвращает True при успехе, False при ошибке.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error saving tasks to {filepath}: {e}")
        return False

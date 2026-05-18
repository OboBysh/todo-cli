"""
Модуль логики управления задачами.
Не зависит от ввода/вывода и файловой системы.
"""

from typing import List, Dict, Union

def generate_new_id(tasks: List[Dict]) -> int:
    """Генерирует новый ID для задачи."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

def add_task(tasks: List[Dict], title: str) -> List[Dict]:
    """Добавляет новую задачу и возвращает обновлённый список."""
    new_id = generate_new_id(tasks)
    new_task = {
        "id": new_id,
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    return tasks

def list_tasks(tasks: List[Dict]) -> List[Dict]:
    """Возвращает список всех задач."""
    return tasks

def complete_task(tasks: List[Dict], task_id: int) -> Union[List[Dict], None]:
    """
    Отмечает задачу как выполненную.
    Возвращает обновлённый список или None, если задача не найдена.
    """
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return tasks
    return None  # задача не найдена

def delete_task(tasks: List[Dict], task_id: int) -> Union[List[Dict], None]:
    """
    Удаляет задачу по ID.
    Возвращает обновлённый список или None, если задача не найдена.
    """
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return tasks
    return None

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.task_logic import add_task, list_tasks, complete_task, delete_task, edit_task_title

def test_add_task():
    tasks = []
    add_task(tasks, "Купить хлеб")
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Купить хлеб"
    assert tasks[0]["completed"] is False
    assert tasks[0]["id"] == 1

def test_add_multiple():
    tasks = []
    add_task(tasks, "Задача 1")
    add_task(tasks, "Задача 2")
    assert tasks[0]["id"] == 1
    assert tasks[1]["id"] == 2

def test_complete_task():
    tasks = []
    add_task(tasks, "Сделать")
    complete_task(tasks, 1)
    assert tasks[0]["completed"] is True

def test_complete_nonexistent():
    tasks = []
    add_task(tasks, "Только одна")
    result = complete_task(tasks, 999)
    assert result is None

def test_delete_task():
    tasks = []
    add_task(tasks, "A")
    add_task(tasks, "B")
    delete_task(tasks, 1)
    assert len(tasks) == 1
    assert tasks[0]["id"] == 2

def test_edit_task_title():
    tasks = [{"id": 1, "title": "Старое", "completed": False}]
    edit_task_title(tasks, 1, "Новое")
    assert tasks[0]["title"] == "Новое"
    result = edit_task_title(tasks, 999, "Не важно")
    assert result is None
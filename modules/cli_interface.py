"""
Модуль CLI интерфейса для управления задачами.
Связывает task_logic, file_manager и error_handler.
"""

import sys
from modules.task_logic import add_task, list_tasks, complete_task, delete_task
from modules.file_manager import load_tasks, save_tasks
from modules.error_handler import handle_errors, InvalidInputError, TaskNotFoundError


class TodoCLI:
    def __init__(self, filepath="tasks.json"):
        self.filepath = filepath
        self.tasks = load_tasks(filepath)

    def save(self):
        """Сохранить текущие задачи в файл."""
        save_tasks(self.tasks, self.filepath)

    @handle_errors
    def add(self, title: str):
        """Добавить новую задачу."""
        if not title or not title.strip():
            raise InvalidInputError("Название задачи не может быть пустым")
        add_task(self.tasks, title.strip())
        self.save()
        print(f"✅ Задача \"{title}\" добавлена (ID={self.tasks[-1]['id']})")

    @handle_errors
    def list(self):
        """Показать все задачи."""
        if not self.tasks:
            print("📭 Список задач пуст.")
            return
        print("\n📋 Ваши задачи:")
        for task in self.tasks:
            status = "✓" if task["completed"] else "☐"
            print(f"  [{task['id']}] {status} {task['title']}")
        print()

    @handle_errors
    def complete(self, task_id_str: str):
        """Отметить задачу выполненной."""
        try:
            task_id = int(task_id_str)
        except ValueError:
            raise InvalidInputError("ID задачи должно быть целым числом")

        result = complete_task(self.tasks, task_id)
        if result is None:
            raise TaskNotFoundError(f"Задача с ID={task_id} не найдена")
        self.save()
        print(f"✅ Задача #{task_id} отмечена как выполненная")

    @handle_errors
    def delete(self, task_id_str: str):
        """Удалить задачу."""
        try:
            task_id = int(task_id_str)
        except ValueError:
            raise InvalidInputError("ID задачи должно быть целым числом")

        result = delete_task(self.tasks, task_id)
        if result is None:
            raise TaskNotFoundError(f"Задача с ID={task_id} не найдена")
        self.save()
        print(f"🗑️ Задача #{task_id} удалена")

    def run(self):
        """Главный цикл приложения."""
        print("Добро пожаловать в Todo CLI!")
        print("Доступные команды:")
        print("  add <текст>      - добавить задачу")
        print("  list             - показать все задачи")
        print("  complete <id>    - отметить задачу выполненной")
        print("  delete <id>      - удалить задачу")
        print("  exit             - сохранить и выйти")

        while True:
            try:
                user_input = input("\n> ").strip()
                if not user_input:
                    continue

                parts = user_input.split(maxsplit=1)
                command = parts[0].lower()
                arg = parts[1] if len(parts) > 1 else ""

                if command == "exit":
                    self.save()
                    print("👋 До свидания!")
                    break
                elif command == "add":
                    if not arg:
                        print("⚠️  Укажите текст задачи после 'add'")
                    else:
                        self.add(arg)
                elif command == "list":
                    self.list()
                elif command == "complete":
                    if not arg:
                        print("⚠️  Укажите ID задачи")
                    else:
                        self.complete(arg)
                elif command == "delete":
                    if not arg:
                        print("⚠️  Укажите ID задачи")
                    else:
                        self.delete(arg)
                else:
                    print(f"❓ Неизвестная команда: {command}. Доступны: add, list, complete, delete, exit")
            except KeyboardInterrupt:
                # Ctrl+C
                print("\n\n👋 Выход без сохранения? (exit для сохранения)")
            except EOFError:
                # Ctrl+D
                print("\n👋 До свидания!")
                break


if __name__ == "__main__":
    app = TodoCLI()
    app.run()
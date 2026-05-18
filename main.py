#!/usr/bin/env python3
"""
Todo CLI Utility - главная точка входа.
Запускает интерактивную командную строку для управления списком дел.
"""

from modules.cli_interface import TodoCLI

def main():
    app = TodoCLI()  # использует tasks.json по умолчанию
    app.run()

if __name__ == "__main__":
    main()
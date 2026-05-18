import sys
import os
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.file_manager import save_tasks, load_tasks


def test_save_and_load(tmp_path):
    # Используем временную директорию pytest
    test_file = tmp_path / "test_tasks.json"
    test_data = [{"id": 1, "title": "Тест", "completed": False}]

    save_tasks(test_data, str(test_file))
    assert test_file.exists()

    loaded = load_tasks(str(test_file))
    assert loaded == test_data


def test_load_nonexistent():
    loaded = load_tasks("non_existent_12345.json")
    assert loaded == []


def test_load_corrupted_json(tmp_path):
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("{invalid json}")
    loaded = load_tasks(str(bad_file))
    assert loaded == []
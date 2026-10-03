import json
import os

DATA_DIR = "data"


def _ensure_dir() -> None:
    """Создать каталог data при отсутствии."""
    os.makedirs(DATA_DIR, exist_ok=True)


def load_requests(filename: str = "requests.json") -> list[dict]:
    """Загрузить список обращений из JSON-файла."""
    _ensure_dir()
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Предупреждение: файл {filename} повреждён, начинаем с пустого списка.")
        return []


def save_requests(requests: list[dict], filename: str = "requests.json") -> None:
    """Сохранить список обращений в JSON-файл."""
    _ensure_dir()
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(requests, f, ensure_ascii=False, indent=2)


def load_masters(filename: str = "masters.json") -> list[dict]:
    """Загрузить список мастеров из JSON-файла."""
    _ensure_dir()
    path = os.path.join(DATA_DIR, filename)
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_masters(masters: list[dict], filename: str = "masters.json") -> None:
    """Сохранить список мастеров в JSON-файл."""
    _ensure_dir()
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(masters, f, ensure_ascii=False, indent=2)
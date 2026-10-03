def add_master(masters: list[dict], name: str, specialization: str) -> int:
    """Добавить мастера, вернуть его id."""
    master_id = len(masters) + 1
    masters.append({
        "id": master_id,
        "name": name,
        "specialization": specialization,
        "available": True,
    })
    return master_id


def find_master(masters: list[dict], query: str) -> list[dict]:
    """Найти мастеров по подстроке имени или специализации."""
    query_lower = query.lower()
    return [
        m for m in masters
        if query_lower in m["name"].lower()
        or query_lower in m["specialization"].lower()
    ]


def get_available_masters(masters: list[dict]) -> list[dict]:
    """Вернуть список доступных мастеров."""
    return [m for m in masters if m.get("available", False)]


def sort_masters_by_name(masters: list[dict]) -> list[dict]:
    """Отсортировать мастеров по имени (lambda-функция)."""
    return sorted(masters, key=lambda m: m["name"])

from datetime import date


def create_request(
    requests: list[dict],
    client_name: str,
    device_type: str,
    problem: str,
    master_id: int,
    request_date: date,
) -> dict:
    """Создать новое обращение и добавить в список."""
    request_id = len(requests) + 1
    new_request = {
        "id": request_id,
        "client_name": client_name,
        "device_type": device_type,
        "problem": problem,
        "master_id": master_id,
        "request_date": request_date.isoformat(),
        "status": "Принято",
    }
    requests.append(new_request)
    return new_request


def is_master_available(masters: list[dict], master_id: int) -> bool:
    """Проверить доступность мастера по id."""
    for master in masters:
        if master["id"] == master_id:
            return master.get("available", False)
    return False


def get_request_status(is_available: bool) -> str:
    """Текстовый статус регистрации (функция из ПР1)."""
    if is_available:
        return "Обращение зарегистрировано, мастер доступен"
    return "Обращение принято в очередь, мастер занят"


def find_requests_by_client(requests: list[dict], client_name: str) -> list[dict]:
    """Найти обращения по имени клиента (генератор)."""
    query = client_name.lower()
    return [r for r in requests if query in r["client_name"].lower()]


def filter_requests_by_status(requests: list[dict], status: str) -> list[dict]:
    """Отобрать обращения по статусу."""
    return [r for r in requests if r["status"] == status]


def count_requests_by_device(requests: list[dict]) -> dict[str, int]:
    """Статистика: количество обращений по типам устройств."""
    stats: dict[str, int] = {}
    for request in requests:
        device = request["device_type"]
        stats[device] = stats.get(device, 0) + 1
    return stats
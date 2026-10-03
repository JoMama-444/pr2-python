from datetime import date

from requests import (
    create_request,
    get_request_status,
    is_master_available,
    count_requests_by_device,
)


def test_create_request():
    requests = []
    r = create_request(requests, "Иванов", "Ноутбук", "Не включается", 1, date(2026, 9, 15))
    assert r["id"] == 1
    assert len(requests) == 1


def test_is_master_available():
    masters = [{"id": 1, "name": "Петров", "specialization": "Ноутбуки", "available": True}]
    assert is_master_available(masters, 1) is True
    assert is_master_available(masters, 99) is False


def test_get_request_status():
    assert "доступен" in get_request_status(True)
    assert "очередь" in get_request_status(False)


def test_count_requests_by_device():
    requests = [
        {"device_type": "Ноутбук"},
        {"device_type": "Ноутбук"},
        {"device_type": "Телефон"},
    ]
    stats = count_requests_by_device(requests)
    assert stats["Ноутбук"] == 2
    assert stats["Телефон"] == 1
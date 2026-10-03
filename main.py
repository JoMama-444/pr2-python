from datetime import date

from masters import (
    add_master,
    find_master,
    get_available_masters,
    sort_masters_by_name,
)
from requests import (
    create_request,
    get_request_status,
    is_master_available,
    find_requests_by_client,
    count_requests_by_device,
)
from storage import (
    load_masters,
    load_requests,
    save_masters,
    save_requests,
)
from utils import input_date, input_int, input_non_empty


def show_masters(masters: list[dict]) -> None:
    """Вывести список мастеров."""
    if not masters:
        print("Список мастеров пуст.")
        return
    print("\n--- Мастера ---")
    for m in sort_masters_by_name(masters):
        status = "доступен" if m["available"] else "занят"
        print(f"[{m['id']}] {m['name']} — {m['specialization']} ({status})")


def show_requests(requests: list[dict]) -> None:
    """Вывести список обращений."""
    if not requests:
        print("Список обращений пуст.")
        return
    print("\n--- Обращения ---")
    for r in requests:
        print(
            f"[{r['id']}] Клиент: {r['client_name']}, "
            f"устройство: {r['device_type']}, "
            f"проблема: {r['problem']}, "
            f"мастер №{r['master_id']}, "
            f"дата: {r['request_date']}, статус: {r['status']}"
        )


def register_request(masters: list[dict], requests: list[dict]) -> None:
    """Сценарий регистрации нового обращения."""
    if not masters:
        print("Нет мастеров. Сначала добавьте мастера.")
        return
    client = input_non_empty("Имя клиента: ")
    device = input_non_empty("Тип устройства: ")
    problem = input_non_empty("Описание проблемы: ")
    request_date = input_date("Дата обращения (ДД.ММ.ГГГГ): ")

    available = get_available_masters(masters)
    if not available:
        print("Нет доступных мастеров. Обращение будет в очереди.")
        master_id = masters[0]["id"]
        available_flag = False
    else:
        show_masters(available)
        master_id = input_int("ID мастера: ")
        available_flag = is_master_available(masters, master_id)
        if not available_flag:
            print("Мастер занят, обращение будет в очереди.")

    new_request = create_request(
        requests, client, device, problem, master_id, request_date
    )
    new_request["status"] = get_request_status(available_flag)
    print(f"Обращение №{new_request['id']} создано.")
    print(new_request["status"])


def add_master_dialog(masters: list[dict]) -> None:
    """Диалог добавления мастера."""
    name = input_non_empty("Имя мастера: ")
    spec = input_non_empty("Специализация: ")
    add_master(masters, name, spec)
    print("Мастер добавлен.")


def search_requests(requests: list[dict]) -> None:
    """Поиск обращений по клиенту."""
    query = input_non_empty("Имя клиента для поиска: ")
    found = find_requests_by_client(requests, query)
    show_requests(found)


def show_statistics(requests: list[dict]) -> None:
    """Статистика по устройствам."""
    stats = count_requests_by_device(requests)
    if not stats:
        print("Нет данных для статистики.")
        return
    print("\n--- Статистика по устройствам ---")
    for device, count in stats.items():
        print(f"{device}: {count}")


def main() -> None:
    """Точка запуска: меню приложения."""
    masters = load_masters()
    requests = load_requests()

    while True:
        print("\n=== Система регистрации сервисных обращений ===")
        print("1. Показать мастеров")
        print("2. Добавить мастера")
        print("3. Показать обращения")
        print("4. Зарегистрировать обращение")
        print("5. Найти обращения по клиенту")
        print("6. Статистика по устройствам")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()

        try:
            if choice == "1":
                show_masters(masters)
            elif choice == "2":
                add_master_dialog(masters)
                save_masters(masters)
            elif choice == "3":
                show_requests(requests)
            elif choice == "4":
                register_request(masters, requests)
                save_requests(requests)
            elif choice == "5":
                search_requests(requests)
            elif choice == "6":
                show_statistics(requests)
            elif choice == "0":
                save_masters(masters)
                save_requests(requests)
                print("Данные сохранены. До встречи!")
                break
            else:
                print("Неизвестная команда.")
        except Exception as error:
            print(f"Непредвиденная ошибка: {error}")


if __name__ == "__main__":
    main()
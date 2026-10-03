from masters import add_master, find_master, get_available_masters


def test_add_master():
    masters = []
    master_id = add_master(masters, "Петров Пётр", "Ноутбуки")
    assert master_id == 1
    assert len(masters) == 1


def test_find_master():
    masters = []
    add_master(masters, "Петров Пётр", "Ноутбуки")
    assert find_master(masters, "петров")
    assert find_master(masters, "ноут")


def test_get_available_masters():
    masters = []
    add_master(masters, "Петров Пётр", "Ноутбуки")
    available = get_available_masters(masters)
    assert len(available) == 1
    
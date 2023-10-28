import pytest

from task1 import NumbersList


@pytest.fixture
def list1():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def list2():
    return [10, 10]


def test_get_lists_averages(list1, list2):
    nums_list = NumbersList(list1, list2)
    assert nums_list.get_list() == (3, 10)


@pytest.mark.parametrize("lst1, lst2, result", [
    ([], [1, 2, 3], (0, 2)),
    ([1, 2, 3], [], (2, 0)),
    ([], [], (0, 0))])
def test_for_empty_lists(lst1, lst2, result):
    numbers_list = NumbersList(lst1, lst2)
    assert numbers_list.get_list() == result


@pytest.mark.parametrize("lst1, lst2, result", [
    ([1], [1, 2, 3], (1, 2)),
    ([1, 2, 3], [1], (2, 1)),
    ([1], [1], (1, 1))])
def test_for_empty_lists(lst1, lst2, result):
    numbers_list = NumbersList(lst1, lst2)
    assert numbers_list.get_list() == result


def test_checking_average_value_when_greater(list1, list2, capfd):
    numbers_list = NumbersList(list2, list1)
    numbers_list.list_comparison()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'первый список имеет среднее значение больше'


def test_checking_average_value_when_greater(list1, list2, capfd):
    numbers_list = NumbersList(list1, list2)
    numbers_list.list_comparison()
    captured = capfd.readouterr()
    assert captured.out.strip() == 'второй  список имеет среднее значение больше'


def test_checking_average_value_when_greater(list1, list2, capfd):
    numbers_list = NumbersList(list1, list1)
    numbers_list.list_comparison()
    captured = capfd.readouterr()
    assert captured.out.strip() == "Списки имеют равное среднее значение"


def test_init(list1, list2):
    nums_list = NumbersList(list1, list2)
    assert nums_list.lst1 == list1
    assert nums_list.lst2 == list2
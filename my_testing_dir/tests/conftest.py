import pytest


@pytest.fixture(scope='session')
def data():
    # открываем БД
    lst_num = {'num_1': 3, 'num_2': 4, 'expected_res': 7}
    yield lst_num
    # закрываем БД

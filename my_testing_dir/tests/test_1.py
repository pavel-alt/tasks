import pytest

from myfunc import calculate


@pytest.mark.parametrize('num_1, num_2, expected_res', [(3, 4, 7),
                                                        (-2, -5, -7)])
def test_calc(num_1, num_2, expected_res):
    res = calculate(num_1, num_2)
    assert res == expected_res


def test_calc1(data):
    res = calculate(data['num_1'], data['num_2'])
    assert res == data['expected_res']


def test_calc2(data):
    res = calculate(data['num_1'], data['num_2'])
    assert res == data['expected_res']


def test_calc3(data):
    res = calculate(data['num_1'], data['num_2'])
    assert res == data['expected_res']

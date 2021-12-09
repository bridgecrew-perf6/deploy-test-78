from tools import calculator


def test_sum():
    result = calculator.sum(1, 2)

    assert result == 3

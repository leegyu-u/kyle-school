import pytest
from calc_class import Calculator

# 상수
NUMBER_1 = 3.0
NUMBER_2 = 2.0

# Fixtures
@pytest.fixture
def calculator():
    return Calculator()

def verify_answer(expected, answer, last_answer):
    assert expected == answer
    assert expected == last_answer


# ======Test Cases 시작======
def test_last_answer_init(calculator):
    # TODO : Test Code

    assert calculator.last_answer == 0.0

    answer = calculator.add(NUMBER_1, NUMBER_2)

    assert calculator.last_answer == answer


def test_add(calculator):
    # TODO: Use NUMBER_1, NUMBER_2을 사용해 Test

    assert calculator.add(NUMBER_1, NUMBER_2) == 5.0


def test_subtract(calculator):
    # TODO: Use NUMBER_1, NUMBER_2을 사용해 Test

    assert calculator.subtract(NUMBER_1, NUMBER_2) == 1.0


def test_subtract_negative(calculator):
    # TODO: Use NUMBER_1, NUMBER_2을 사용해 Test

    assert calculator.subtract(NUMBER_2, NUMBER_1) == -1.0


def test_multiply(calculator):
    # TODO: Use NUMBER_1, NUMBER_2을 사용해 Test

    assert calculator.multiply(NUMBER_1, NUMBER_2) == 6.0


def test_divide(calculator):
    # TODO: Use NUMBER_1, NUMBER_2을 사용해 Test

    assert calculator.divide(NUMBER_1, NUMBER_2) == 1.5


def test_divide_by_zero(calculator):
    # TODO : ZeroDivisionError가 나오는지 확인하는 Test
    with pytest.raises(ZeroDivisionError) as e:
        calculator.divide(3, 0)


@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_1),
    (NUMBER_2, NUMBER_1, NUMBER_1),
    (NUMBER_1, NUMBER_1, NUMBER_1),
])
def test_maximum(calculator, a, b, expected):
    # TODO : parametrize를 사용해 파라미터를 주입
    assert calculator.maximum(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_2),
    (NUMBER_2, NUMBER_1, NUMBER_2),
    (NUMBER_2, NUMBER_2, NUMBER_2),
])
def test_minimum(calculator, a, b, expected):
    # TODO : parametrize를 사용해 파라미터를 주입
    assert calculator.minimum(a, b) == expected


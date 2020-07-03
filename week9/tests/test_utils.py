import pytest
import pandas as pd
from utils import load_data

# 테스트할 다른 함수에서 함수명을 객체처럼 사용할 수 있음
# Dependency Injection
@pytest.fixture(scope="session")
def result_fixture():
    result = load_data()
    return result

def test_len(result_fixture):
    assert len(result_fixture) == 150

def test_object_type(result_fixture):
    assert isinstance(result_fixture, pd.DataFrame)


# 파라미터로 넘겨서 여러가지를 한꺼번에 테스트할 경우 사용
@pytest.mark.parametrize("test_input, expected",
                      [("3+5", 8),
                       ("2+4", 6),
                       ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


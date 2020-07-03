import pytest
from simple_class import Queue

@pytest.fixture(scope="session")
def empty_queue():
    q = Queue()
    return q

@pytest.fixture(scope="session")
def sample_queue():
    q = Queue()

    q.add_item(5)
    q.add_item(7)
    q.add_item("hello")

    return q


def test_firstlast(sample_queue):
    assert sample_queue.first() == 5
    assert sample_queue.last() == "hello"

def test_len(empty_queue, sample_queue):
    assert empty_queue.length() == 0
    assert sample_queue.length() == 3



# def test_firstlast():
#     q = Queue()
#
#     q.add_item(5)
#     q.add_item(7)
#     q.add_item("hello")
#
#     assert q.first() == 5
#     assert q.last() == "hello"

# def test_len():
#     q = Queue()
#
#     assert q.length() == 0
#
#     q.add_item(5)
#
#     assert q.length() == 1
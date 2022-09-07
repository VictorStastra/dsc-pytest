import pytest
from src.logic import Stop


def test_init():
    stop = Stop(name='stop1', x=0, y=0)
    assert stop.name == 'stop1'
    assert stop.x == 0
    assert stop.y == 0


def test_point():
    stop = Stop(name='stop1', x=0, y=0)
    assert stop.coords == (0, 0)


def test_init_neg():
    stop = Stop(name='stop1', x=-1, y=-1)
    assert stop.name == 'stop1'
    assert stop.x == -1
    assert stop.y == -1


# ???? What happens here?
def test_init_types():
    stop = Stop(name=123, x='a', y='b')
    assert isinstance(stop, Stop)
# ???? Should this happen? Would we want to allow this?

# Use pytest fixtures to create a Stop object
# and use it in multiple tests.
# This works for data, objects etc. which are shared between tests.
@pytest.fixture
def stop():
    return Stop(name='stop1', x=0, y=0)


def test_init_fixture(stop):
    assert stop.name == 'stop1'
    assert stop.x == 0
    assert stop.y == 0


def test_point_fixture(stop):
    assert stop.coords == (0, 0)

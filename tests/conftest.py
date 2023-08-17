import pytest

from src.stack import Stack


@pytest.fixture
def stack():
    node = Stack()
    node.push("data1")
    node.push("data2")
    node.push("data3")

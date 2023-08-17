from src.stack import Node


# TestCase1
def test_node():
    """Тестирование класса Node"""
    node_1 = Node(1, None)
    node_2 = Node(2, node_1)
    assert node_1.data == 1
    assert node_2.data == 2
    assert node_1.next_node is None
    assert node_2.next_node == node_1


# TestCase2
def test_push(stack):
    assert stack.top.data == "data3"
    assert stack.top.next_node.data == "data2"
    assert stack.top.next_node.next_node.data == "data1"
    assert stack.top.next_node.next_node.next_node is None

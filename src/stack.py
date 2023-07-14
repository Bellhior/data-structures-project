class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node=0):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        # выделение нового узла
        param = Node(data)
        # установка данных
        param.data = data
        # установка указателя нового узла так, чтобы он указывал на текущий
        # верхний узел списка
        param.next_node = self.top
        # обновление
        self.top = param
        return self.top

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        # обновление верхнего указателя, чтобы он указывал на следующий узел
        self.top = self.top.next_node
        return self.top

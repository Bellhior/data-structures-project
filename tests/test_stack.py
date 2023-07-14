"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack

"""
Я написал, как проводил тесты, всё получалось в формате  <__main__.Node object at 0x0000025CCF464F90>
и Unittest выдаёт ошибки, числовые значения не получаются, оттестил как мог
"""


class TestStack(unittest.TestCase):

    def test_push(self):
        # print(stack.push("data1")) == print(stack.top)
        self.assertEqual(Stack.push("data1"), Stack.top)
        # print(stack.push("data2")) == print(stack.top)
        self.assertEqual(Stack.push("data2"), Stack.top)
        # print(stack.push("data3")) == print(stack.top)
        self.assertEqual(Stack.push("data3"), Stack.top)

    def test_pop(self):
        # print(stack.pop() == print(stack.push("data2"))
        self.assertEqual(Stack.pop(), Stack.push("data2"))
        # print(stack.pop() == print(stack.push("data1"))
        self.assertEqual(Stack.pop(), Stack.push("data1"))
        # print(stack.pop() == None
        self.assertEqual(Stack.pop(), None)


if __name__ == '__main__':
    unittest.main()

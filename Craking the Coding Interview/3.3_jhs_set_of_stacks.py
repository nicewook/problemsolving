"""
set of stacks
push and pop
when stack is full, add one more stack and push to added stack
when stack is empty, remove empty stack and use previous stack.
스택이 일정크기 이상 커지면 새 스택을 만들고,
스택이 비면 스택을 제거하고 이전 스택을 사용한다.
"""

import unittest

class Stack:
    def __init__(self):
        self.items = []
        self.max = 3

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def print_stack(self):
        print(self.items)

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Stacks:
    def __init__(self):
        self.stacklist = []
        self.max_stack_size = 3
        #첫 스택 생성
        self.stacklist.append(Stack())

    def push(self, item):
        st = self.getLastStack()
        if self.max_stack_size == st.size():
            new_st = Stack()
            new_st.push(item)
            self.stacklist.append(new_st)
        else:
            st.push(item)

    def pop(self):
        st = self.getLastStack()
        if st.is_empty():
            self.stacklist.pop()
            st = self.getLastStack()
            st.pop()
        else:
            st.pop()

    def getLastStack(self):
        return self.stacklist[len(self.stacklist) -1]

    def getStackCount(self):
        return len(self.stacklist)

    def printStacks(self):
        result = []
        for st in self.stacklist:
            for item in st.items:
                result.append(item)
        return result

class setOfStacksTest(unittest.TestCase):
    def test(self):
        stacks = Stacks()
        stacks.push(5)
        stacks.push(3)
        stacks.push(2)
        stacks.push(7)

        # 네 개 들어온거, 마치 하나의 스택처럼 동작하는거 확인
        self.assertEqual([5, 3, 2, 7], stacks.printStacks())
        print("Stack items: ", stacks.printStacks())

        # 내부적으로 스택이 몇개인가 확인
        self.assertEqual(2, stacks.getStackCount())
        print("Stack counts: ", stacks.getStackCount())

        stacks.pop()
        # 하나를 빼도 하나의 스택처럼 동작하는 것 확인
        self.assertEqual([5, 3, 2], stacks.printStacks())
        print("Stack items: ", stacks.printStacks())

        stacks.pop()
        # 또 하나를 빼도 하나의 스택처럼 동작하는 것 확인
        self.assertEqual([5, 3,], stacks.printStacks())
        print("Stack items: ", stacks.printStacks())

        #마지막으로 전체 스택의 개수가 하나 줄은 것 확인
        self.assertEqual(1, stacks.getStackCount())
        print("Stack counts: ", stacks.getStackCount())


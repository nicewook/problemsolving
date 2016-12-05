"""
두 개의 스택을 이용해서 큐를 구현한다
"""

import unittest

class Stack:

    def __init__(self):
        self.items = []
        #self. max = 3

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def print_stack(self):
        print(self.items)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class myQueue:

    def __init__(self):
        self.stEnqueue = Stack()
        self.stDequeue = Stack()

    def enqueue(self, item):
        self.stEnqueue.push(item)

    def dequeue(self):
        if self.stDequeue.is_empty():
            while self.stEnqueue.is_empty() is False:
                self.stDequeue.push(self.stEnqueue.pop())

        return self.stDequeue.pop()

class queueWithStacks(unittest.TestCase):
    def test(self):
        myq = myQueue()
        myq.enqueue(1)
        myq.enqueue(2)
        myq.enqueue(3)

        #queue에서 pop하면 제일 먼저 넣은게 나와야 한다.
        self.assertEqual(1, myq.dequeue())

        myq.enqueue(100)

        # queue에서 pop하면 제일 먼저 넣은게 나와야 한다.
        self.assertEqual(2, myq.dequeue())

        # queue에서 pop하면 제일 먼저 넣은게 나와야 한다.
        self.assertEqual(3, myq.dequeue())

        # queue에서 pop하면 제일 먼저 넣은게 나와야 한다.
        self.assertEqual(100, myq.dequeue())






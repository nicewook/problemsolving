"""
stack has min function O(1)
O(1)으로 스택에 들어온 값을 바로 알아내기
O(1)은 한방에 값 얻는 것
O(n)은 for문으로 n 돌리는 것
"""

import unittest

class Stack:
    def __init__(self):
        self.items = [] # 실제 스택
        self.mins = [] # 특정 순간의 최소값들 저장하는 스택
        self.min = None # 현시점 최소값

    def push(self,item):
        self.items.append(item)
        # 아래와 같으면 self.mins는 self.items보다 항상 하나 모자라겠다.
        if self.min is not None:
            self.mins.append(self.min)
        if self.min is None or self.min > item:
            self.min = item

    def pop(self):
        self.items.pop()
        self.min = self.mins.pop()

    def getminimum(self):
        return self.min  # 이렇게 한방에 min을 알려주는 함수가 있기에 O(1) 인거다

    def peak(self):
        return self.items[-1]   # 이건 맨 뒤의 값을 꺼내는 것

class test(unittest.TestCase):
    def test(self):
        st = Stack()
        st.push(5)
        self.assertEqual(5, st.getminimum())
        st.push(3)
        self.assertEqual(3, st.getminimum())
        self.assertEqual(3, st.peak())
        st.pop()
        self.assertEqual(5, st.getminimum())

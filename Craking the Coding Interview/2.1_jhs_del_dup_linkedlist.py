"""
Linked List
Delete Duplicate from linked list
"""

import unittest

class Node:
        def __init__(self, item):
            self.val = item
            self.next = None

class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    def add(self, item):
        # cur = self.head라고 하여 맨 처음 노드를 가리키고
        cur = self.head

        # 그다음엔 맨 끝의 Node까지 이동
        while cur.next is not None:
            cur = cur.next

        # 맨 끝의 Node에서 next는 None인 것을 새로 생성하는 Node(item)을 가리키게 한다.
        # 이렇게 Linked List를 추가
        cur.next = Node(item)

    # 중복되지 않은 것만 dict에 True로 체크해나가는 방식으로 구현
    def delete_duplicate(self):
        #우선은 맨 처음 노드를 cur라고 명명, 빈 딕셔너리 생성, 현재 prev는 없음
        cur = self.head
        dict={}
        prev=None

        #while문으로 전체 링크드리스트를 돈다
        while cur is not None:
            #딕셔너리를 우선 확실히 이해하긴 해야겠다
            #아무튼 이미 딕셔너리에 있다면 prev.next 가 cur 이던것을 cur.next로 바꿔버린다
            #즉 cur가 중복이니 건너뛰라는 것이다.
            if cur.val in dict:
                prev.next = cur.next

            #만약 중복이 아니라면 딕셔너리에 추가하고
            #다음으로 진행하기 위해 prev=cur로 바꿔줌
            else:
                dict[cur.val] = True
                prev = cur

            #이제 하나 증가시킴
            cur = cur.next

    def printlist(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur=cur.next
        return str(res)


class LinkedListTest(unittest.TestCase):
    def test(self):
        # LinkedList의 __init__ 함수가 실행된다.
        # 따라서 head가 Node(3)이 된다.
        # Node(3) 이므로 val은 3, next는 None인 상태
        ll = LinkedList(3)

        # head의 val은 3이고 next는 None인 상태에서 add(4) 부터 해서 쭉쭉 추가해나감
        ll.add(4)
        ll.add(5)
        ll.add(6)
        ll.add(4)
        ll.add(7)
        ll.add(4)
        ll.add(6)
        ll.add(6)

        # 중복 제거
        ll.delete_duplicate()
        self.assertEqual("[3, 4, 5, 6, 7]", ll.printlist())



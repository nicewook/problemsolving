

import unittest

class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    def add(self,item):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = Node(item)

    #여기까진 똑같음
    def remove(self, item):
        #헤드가 바로 그 값을 가지고 있으면 헤드 제거
        if self.head.val == item:
            self.head = self.head.next

        else:
            cur = self.head
            while cur.next is not None:
                if cur.val == item:
                    self.removeItem(item)
                    return
                cur = cur.next
            #여기까지 왔다면 item 값을 가지는 노드가 없다는 의미
            print("아이템을 가지는 노드 없음")

    def removeItem(self, item):
        if self.head.val == item:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.next.val == item:
                    nextnode = cur.next.next
                    cur.next = nextnode
                    cur.next.next = None
                    return
                cur = cur.next
            # 여기까지 왔다면 item 값을 가지는 노드가 없다는 의미
            print("아이템을 가지는 노드 없음")

    def printlist(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return str(res)


class LinkedListTest(unittest.TestCase):
    def test(self):
        ll=LinkedList(9)
        ll.add(8)
        ll.add(7)
        ll.removeItem(8)

        print(ll.printlist())
        self.assertEqual("[9, 7]", ll.printlist())
        #self.assertEqual("[9, 8, 7]", ll.printlist())







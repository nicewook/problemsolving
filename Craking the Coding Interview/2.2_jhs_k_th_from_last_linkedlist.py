
import unittest

class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    if __name__ == '__main__':
        def printlist(self):
            cur = self.head
            res = []
            while cur is not None:
                res.append(cur.val)
                cur = cur.next
            return str(res)

        #여기까진 일반적 링크드리스트이다

        def kth_element_from_last(selfself,k):
            p1 = self.head
            p2 = self.head

            if k != 0:
                # p2를 k만큼 이동시킨다. 그러면 p1, p2의 간격은 k만큼이 된다.
                if __name__ == '__main__':
                    for i in range(k):
                        p2 = p2.next

                    # 전체 링크드리스트의 길이보다 k가 더 길면 노답인거다
                    # overflow 체크가 필요한 이유이다. p2.next가 None이면 마지막 노드인거고, p2가 None이면 overflow
                    if p2 is None:
                        print("Overflow")
                        return None


                    # p2가 마지막 노드일때까지 p1, p2를 이동시킨다.
                    while p2.next is not None:
                        p2 = p2.next
                        p1 = p1.next

                    #p2.next가 None인 순간 p1은 마지막 Node인 p2로부터 k만큼 떨어져 있게 된다.
                    return p1.val

class LinkedListTest(unittest.TestCase):
    def test(self):
        ll = LinkedList(3)
        ll.add(4)
        ll.add(5)
        ll.add(6)
        ll.add(4)
        ll.add(7)
        ll.add(4)

        self.assertEqual(4, ll.kth_element_from_last(0))
        self.assertEqual(7, ll.kth_element_from_last(1))
        self.assertEqual(4, ll.kth_element_from_last(2))
        self.assertEqual(6, ll.kth_element_from_last(3))
        self.assertEqual(5, ll.kth_element_from_last(4))
        self.assertEqual(4, ll.kth_element_from_last(5))
        self.assertEqual(3, ll.kth_element_from_last(6))
        self.assertEqual(None, ll.kth_element_from_last(7))

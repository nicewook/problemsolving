"""
허민석님 원래 링크: https://goo.gl/uT03EJ
원래 링크 내용중 이진트리 여부 체크부분만 구현해본다
"""

import unittest

class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.head = Node(None)

        #in order traverse 결과를 담을 리스트
        self.inorder_list = []
        self.preorder_list = []
        self.postorder_list = []


    def preorder_traverse(self):
        if self.head is not None:
            self.__preorder(self.head)

    # 왼쪽으로 다 내려가고 그다음 맨 아래의 오른쪽부터 다시 거슬러 올라온다.
    # 지나치는 노드들을 바로바로 리스트에 넣는다.
    def __preorder(self, cur):
        self.preorder_list.append(cur.val)
        if cur.left is not None:
            self.__preorder(cur.left)
        if cur.right is not None:
            self.__preorder(cur.right)


    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    # 더이상 왼쪽으로 더 없을때에 리스트에 추가한다.
    # 왼쪽으로의 방문이 다 끝나면 그 부모 역시 리스트에 추가된다.
    # 마지막으로 오른쪽을 방문하고 리스트에 추가한다.
    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)

        self.inorder_list.append(cur.val)


        if cur.right is not None:
            self.__inorder(cur.right)

    def postorder_traverse(self):
        if self.head is not None:
            self.__postorder(self.head)

    # 가장 아래의 왼쪽 오른쪽을 각각 방문하고, 그다음 부모를 방문하는 방식이다.
    # 즉 아래단 부터 방문하는 방식임

    def __postorder(self, cur):
        if cur.left is not None:
            self.__postorder(cur.left)

        if cur.right is not None:
            self.__postorder(cur.right)

        self.postorder_list.append(cur.val)


    # 테스트를 위하여 이진탐색트리를 만들어주는 부분
    def add(self, item):
        if self.head.val is None:
            self.head.val = item
        else:
            self.__add_node(self.head, item)


    def __add_node(self, cur, item):
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)

class binary_tree_test(unittest.TestCase):
    def test(self):
        bt = BinaryTree()
        bt.add(5)
        bt.add(3)
        bt.add(4)
        bt.add(1)
        bt.add(7)
        bt.add(8)
        bt.add(2)
        print("pre order")
        bt.preorder_traverse()
        print(bt.preorder_list)
        self.assertEqual(bt.preorder_list, [5, 3, 1, 2, 4, 7, 8])

        print("in order")
        bt.inorder_traverse()
        print(bt.inorder_list)
        self.assertEqual(bt.inorder_list, [1, 2, 3, 4, 5, 7, 8])

        print("post order")
        bt.postorder_traverse()
        print(bt.postorder_list)
        self.assertEqual(bt.postorder_list, [2, 1, 4, 3, 8, 7, 5])


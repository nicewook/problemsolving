"""
두 이진탐색트리에서
작은 트리가 큰 트리 안에 있는지를 확인하기
- 작은 트리가 큰 트리의 맨 아래단이 아니라 중간에 위치한다면? 흠흠
"""


import unittest

class Node:
    def __init__(self, item):
        self.val = item;
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = Node(None)
        self.inorder_list = []

    # 테스트를 위해 이진 탐색 트리로 만들어주기 위한 함수
    # 이것도 add() 쓰지말고 바로 __add_node() 할 수 없을까?
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

    # 그냥 바로 __search_node() 하면 되지 않나?
    def search(self, item):
        if self.head.val is None:
            return False

        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        if cur.val == item:
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    return self.__search_node(cur.left, item)
                else:
                    return False

            else:
                if cur.right is not None:
                    return self.__search_node(cur.right, item)
                else:
                    return False

    # inorder_traverse
    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def inorder_traverse2(self):
        if self.head is not None:

            self.__inorder(self.head)

    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)

        self.inorder_list.append(cur.val)
        print(cur.val)

        if cur.right is not None:
            self.__inorder(cur.right)


# 그냥 inorder_traverse를 한 다음, 만들어진 두 inorder_list를 비교하였다. 
# search 사용하지 않음
class binary_tree_test_for_subtree_exist(unittest.TestCase):
    def test(self):
        btBig = BinaryTree()
        btBig.add(5)
        btBig.add(3)
        btBig.add(7)
        btBig.add(6)
        btBig.add(9)
        btBig.add(8)

        btSmall = BinaryTree()
        btSmall.add(7)
        btSmall.add(6)
        btSmall.add(9)
        btSmall.add(8)


        btBig.search(btSmall.head.val)
        btBig.inorder_traverse()
        print(btBig.inorder_list)


        btSmall.inorder_traverse()
        print(btSmall.inorder_list)

        #self.assertEqual(btBig.inorder_list, btSmall.inorder_list)
        #self.assertGreaterEqual(btBig.inorder_list, btSmall.inorder_list)
        self.assertTrue(set(btBig.inorder_list) > set(btSmall.inorder_list))








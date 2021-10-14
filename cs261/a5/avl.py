# Course: CS261 - Data Structures
# Author:
# Assignment:
# Description:

import random

from bst import BST
from bst import TreeNode
from bst import Stack
from bst import Queue


class AVLTreeNode(TreeNode):
    """
    AVL Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        super().__init__(value)
        self.parent = None
        self.height = 0


class AVL(BST):
    """
    An AVL tree.
    Note: This Class extends the BST class.
    """
    def add(self, value):
        """
        Adds new value to the tree, maintaining AVL property.
        Note:
            - Duplicates must not be allowed.
            - If the value is already in the tree,
              the method should do nothing.
        """
        self.add(AVLTreeNode(value))
        self.height = self.height() + 1

    def remove(self, value) -> bool:
        """
        Remove the first instance of the value in the AVL tree.
        Note:
            - The method must return True if the value is removed
              from the AVL Tree and otherwise return False.
        """
        pass

    def _rebalance(self, node: AVLTreeNode):
        while node:
            self.update_height(node)
            if self._height(node.left) >= 2 + self._height(node.right):
                if self._height(node.left.left) >= self._height(node.left.right):
                    self.rotate_right(node)
                else:
                    self.rotate_left(node.left)
                    self.rotate_right(node.left)
            elif self._height(node.right) >= 2 + self._height(node.left):
                if self._height(node.right.right) >= self._height(node.right.left):
                    self.rotate_left(node)
                else:
                    self.rotate_right(node.right)
                    self.rotate_left(node)
            node = node.parent

    def rotate_right(self, node: AVLTreeNode) -> AVLTreeNode:
        """
        Rotates BST right and returns the new root of the subtree at which the rotation was performed.
        """
        print("rotating right")
        temp_left_child = node.left
        t = temp_left_child.right

        temp_left_child.right = node
        node.left = t

        node.height = self.height + 1
        temp_left_child.height = node.height() + 1

        return temp_left_child

    def rotate_left(self, node: AVLTreeNode) -> AVLTreeNode:
        """
        Rotates BST left and returns the new root of the subtree at which the rotation was performed
        """
        print("rotating left")
        temp_right_child = node.right
        t = temp_right_child.left

        temp_right_child.left = node
        node.right = t

        node.height = self.height + 1
        temp_right_child.height = node.height() + 1

        return temp_right_child

    def _height(self, node: AVLTreeNode) -> int:
        """
        Updates the height of the AVLTreeNode.
        """
        if not node:
            return -1
        else:
            return node.height

    def update_height(self, node):
        node.height = max(node.left.height(), node.right.height()) + 1


if __name__ == '__main__':

    print("\nPDF - method add() example 1")
    print("----------------------------")
    test_cases = (
        (1, 2, 3),          #RR
        (3, 2, 1),          #LL
        (1, 3, 2),          #RL
        (3, 1, 2),          #LR
    )
    for case in test_cases:
        avl = AVL(case)
        print(avl)


    print("\nPDF - method add() example 2")
    print("----------------------------")
    test_cases = (
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 30, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
        (5, 4, 6, 3, 7, 2, 8),  # LL, RR
        (range(0, 30, 3)),
        (range(0, 31, 3)),
        (range(0, 34, 3)),
        (range(10, -10, -2)),
        ('A', 'B', 'C', 'D', 'E'),
        (1, 1, 1, 1),
    )
    for case in test_cases:
        avl = AVL(case)
        print('INPUT  :', case)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 1")
    print("-------------------------------")
    test_cases = (
        ((1, 2, 3), 1),                             # no AVL rotation
        ((1, 2, 3), 2),                             # no AVL rotation
        ((1, 2, 3), 3),                             # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 0),
        ((50, 40, 60, 30, 70, 20, 80, 45), 45),     # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 40),     # no AVL rotation
        ((50, 40, 60, 30, 70, 20, 80, 45), 30),     # no AVL rotation
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 2")
    print("-------------------------------")
    test_cases = (
        ((50, 40, 60, 30, 70, 20, 80, 45), 20),     # RR
        ((50, 40, 60, 30, 70, 20, 80, 15), 40),     # LL
        ((50, 40, 60, 30, 70, 20, 80, 35), 20),     # RL
        ((50, 40, 60, 30, 70, 20, 80, 25), 40),     # LR
    )
    for tree, del_value in test_cases:
        avl = AVL(tree)
        print('INPUT  :', avl, "DEL:", del_value)
        avl.remove(del_value)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    avl = AVL(case)
    for del_value in case:
        print('INPUT  :', avl, del_value)
        avl.remove(del_value)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    avl = AVL(case)
    for _ in case[:-2]:
        print('INPUT  :', avl.size(), avl, avl.root)
        avl.remove(avl.root.value)
        print('RESULT :', avl)


    print("\nPDF - method remove() example 5")
    print("-------------------------------")
    for _ in range(100):
        case = list(set(random.randrange(1, 20000) for _ in range(900)))
        avl = AVL(case)
        if avl.size() != len(case):
            raise Exception("PROBLEM WITH ADD OPERATION")
        for value in case[::2]:
            avl.remove(value)
        if avl.size() != len(case) - len(case[::2]):
            raise Exception("PROBLEM WITH REMOVE OPERATION")
    print('Stress test finished')


    """ Comprehensive example 1 """
    print("\nComprehensive example 1")
    print("-----------------------")
    tree = AVL()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'  N/A {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in [10, 5, 3, 15, 12, 8, 20, 1, 4, 9, 7]:
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print()
    print(tree.pre_order_traversal())
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
    print(tree.by_level_traversal())


    """ Comprehensive example 2 """
    print("\nComprehensive example 2")
    print("-----------------------")
    tree = AVL()
    header = 'Value   Size  Height   Leaves   Unique   '
    header += 'Complete?  Full?    Perfect?'
    print(header)
    print('-' * len(header))
    print(f'N/A   {tree.size():6} {tree.height():7} ',
          f'{tree.count_leaves():7} {tree.count_unique():8}  ',
          f'{str(tree.is_complete()):10}',
          f'{str(tree.is_full()):7} ',
          f'{str(tree.is_perfect())}')

    for value in 'DATA STRUCTURES':
        tree.add(value)
        print(f'{value:5} {tree.size():6} {tree.height():7} ',
              f'{tree.count_leaves():7} {tree.count_unique():8}  ',
              f'{str(tree.is_complete()):10}',
              f'{str(tree.is_full()):7} ',
              f'{str(tree.is_perfect())}')
    print('', tree.pre_order_traversal(), tree.in_order_traversal(),
          tree.post_order_traversal(), tree.by_level_traversal(),
          sep='\n')

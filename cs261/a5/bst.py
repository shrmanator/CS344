# Course: CS261 - Data Structures
# Student Name:
# Assignment:
# Description:


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty stack based on Python list """
        self._data = []

    def push(self, value: object) -> None:
        """ Add new element on top of the stack """
        self._data.append(value)

    def pop(self) -> object:
        """ Remove element from top of the stack and return its value """
        return self._data.pop()

    def top(self) -> object:
        """ Return value of top element without removing from stack """
        return self._data[-1]

    def is_empty(self):
        """ Return True if the stack is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"


class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """

    def __init__(self):
        """ Initialize empty queue based on Python list """
        self._data = []

    def enqueue(self, value: object) -> None:
        """ Add new element to the end of the queue """
        self._data.append(value)

    def dequeue(self) -> object:
        """ Remove element from the beginning of the queue and return its value """
        return self._data.pop(0)

    def is_empty(self):
        """ Return True if the queue is empty, return False otherwise """
        return len(self._data) == 0

    def __str__(self):
        """ Return content of the stack as a string (for use with print) """
        data_str = [str(i) for i in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class TreeNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value  # to store node's data
        self.left = None  # pointer to root of left subtree
        self.right = None  # pointer to root of right subtree

    def __str__(self):
        return str(self.value)


class BST:
    def __init__(self, start_tree=None) -> None:
        """
        Init new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using in-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self.root, values)
        return "TREE pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, cur, values):
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # base case
        if not cur:
            return
        # store value of current node
        values.append(str(cur.value))
        # recursive case for left subtree
        self._str_helper(cur.left, values)
        # recursive case for right subtree
        self._str_helper(cur.right, values)

    # ------------------------------------------------------------------ #

    def _add_helper(self, value: object, node: TreeNode) -> TreeNode:
        if not node:  # node is None
            curr = TreeNode(value)
            return curr
        if value < node.value:
            node.left = self._add_helper(value, node.left)
        elif value >= node.value:
            node.right = self._add_helper(value, node.right)
        return node

    def add(self, value: object) -> None:
        """
        Adds new value to the tree.
        Note: Duplicates are placed
              in the right subtree.
        """
        self.root = self._add_helper(value, self.root)

    def contains(self, value: object) -> bool:
        """
        Returns True if the value *value* is in the tree, else False.
        """
        q = Queue()
        q.enqueue(self.root)
        while q.is_empty() == False:
            node = q.dequeue()
            if not node:
                continue
            if node.value == value:
                return True
            q.enqueue(node.left)
            q.enqueue(node.right)
        return False

    def get_first(self) -> object:
        """
        Returns the value stored at the root node or None if empty.
        """
        return self.root.value if self.root else None

    def remove_first(self) -> bool:
        """
        Removes the root node in the BinaryTree.
        The method must return False if the tree is empty
        and there is no root node to remove and True if the
         root is removed.
        """
        return self.remove(self.get_first())

    def _remove_helper(self, node: TreeNode, value: TreeNode) -> TreeNode:
        if not node:  # if node doesn't exist, just return it
            return node
        if node.value > value:  # if value is less than node value, go to the left subtree
            node.left = self._remove_helper(node.left, value)
        elif node.value < value:  # if value is greater than node value, go to the right subtree
            node.right = self._remove_helper(node.right, value)
        else:  # if we found the node with the given value
            if not node.right:  # if it has no right children, we swap it with its left children
                return node.left
            if not node.left:  # if it has no left children, we swap it with its right children
                return node.right
            # if the node have both left and right children
            # we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree
            temp = node.right
            parent = node
            while temp.left:
                parent = temp
                temp = temp.left
            if parent == node:
                node.right.left = node.left
                return node.right
            else:
                parent.left = temp.right
                temp.left = node.left
                temp.right = node.right
                return temp
        return node

    def remove(self, value: object) -> bool:
        """
        Removes the first instance of the value in the BinaryTree.
        The method must return True if the value is removed from the
        BinaryTree and otherwise return False.
        """
        if self.contains(value):
            self.root = self._remove_helper(self.root, value)
            return True
        else:
            return False

    def _pre_order_traversal(self, node: TreeNode, queue: Queue) -> Queue:
        if not node:
            return queue
        queue.enqueue(node)
        self._pre_order_traversal(node.left, queue)
        self._pre_order_traversal(node.right, queue)
        return queue

    def pre_order_traversal(self) -> Queue:
        """
        Returns a Queue object that contains values of visited nodes, in pre-order.
        Note: If the tree has no nodes, an empty Queue is returned.
        """
        if not self.root:
            return Queue()
        queue = Queue()
        return self._pre_order_traversal(self.root, queue)

    def _in_order_traversal(self, node: TreeNode, queue: Queue) -> Queue:
        if not node:
            return queue
        self._in_order_traversal(node.left, queue)
        queue.enqueue(node)
        self._in_order_traversal(node.right, queue)
        return queue

    def in_order_traversal(self) -> Queue:
        """
        Returns a Queue object that contains values of visited nodes, in in-order.
        Note: If the tree has no nodes, an empty Queue is returned.
        """
        if not self.root:
            return Queue()
        queue = Queue()
        return self._in_order_traversal(self.root, queue)

    def _post_order_traversal(self, node: TreeNode, queue: Queue) -> Queue:
        if not node:
            return queue
        self._post_order_traversal(node.left, queue)
        self._post_order_traversal(node.right, queue)
        queue.enqueue(node)
        return queue

    def post_order_traversal(self) -> Queue:
        """
        Returns a Queue object that contains values of visited nodes, in post-order.
        Note: If the tree has no nodes, an empty Queue is returned.
        """
        if not self.root:
            return Queue()
        queue = Queue()
        return self._post_order_traversal(self.root, queue)

    def by_level_traversal(self) -> Queue:
        """
        Returns a Queue object that contains values of visited nodes, in level-order.
        Note: If the tree has no nodes, an empty Queue is returned.
        """
        q1 = Queue()
        q2 = Queue()
        if not self.root:
            return q1
        q1.enqueue(self.root)
        q2.enqueue(self.root)
        while q1.is_empty() == False:
            node = q1.dequeue()
            if not node:
                q2.dequeue()
                continue
            if node.left:
                q1.enqueue(node.left)
                q2.enqueue(node.left)
            if node.right:
                q1.enqueue(node.right)
                q2.enqueue(node.right)
        return q2

    def is_full(self) -> bool:
        """
        Returns True if the current tree is a ‘full binary tree’.

        A full binary tree is a binary tree in which every interior
        node has exactly two children:

        Note:
            - Empty trees are considered ‘full’.
            - Trees consisting of a single root node are ‘full’
        """
        if not self.root or self.size() == 1:
            return True
        q = Queue()
        bst = BST()
        q.enqueue(self.root)
        while q.is_empty() == False:
            node = q.dequeue()
            if node is None:
                continue
            elif (not node.left or not node.right):
                if not self._is_leaf(node):
                    bst.add(False)
                else:
                    bst.add(True)
            q.enqueue(node.left)
            q.enqueue(node.right)
        return not bst.contains(False)  # if BST does not contain False

    def is_complete(self) -> bool:
        """
        Returns True if the current tree is a ‘complete binary tree’.
        Note:
            - Empty trees are considered complete.
            - Trees consisting of a single root node are complete.
        """
        if self.root is None:
            return True
        queue = Queue()

        flag = False  # It's True when a non-full node is processed.

        queue.enqueue(self.root)
        while queue.is_empty() == False:
            node = queue.dequeue()
            if node is None:
                continue
            if node.left:
                if flag:
                    return False
                queue.enqueue(node.left)
            else:
                flag = True
            if node.right:
                if flag:
                    return False
                else:
                    queue.enqueue(node.right)
            else:
                flag = True  # If it's a non-full node.
        return True

    def is_perfect(self) -> bool:
        """
        Returns True if the current tree is a ‘perfect binary tree’.
         Note:
             - Empty trees are considered ‘perfect’.
             - Trees consisting of a single root node are ‘perfect’.
        """
        h = -1
        q = Queue()
        q.enqueue(self.root)
        q_size = 1
        while q.is_empty() == False:
            tmp = q_size
            h += 1
            if pow(2, h) is not q_size:
                return False
            q_size = 0
            for i in range(tmp):
                node = q.dequeue()
                if not node:
                    continue
                if node.left:
                    q.enqueue(node.left)
                    q_size += 1
                if node.right:
                    q.enqueue(node.right)
                    q_size += 1
        return True

    def size(self) -> int:
        """
        Returns the total number of nodes in the tree.
        """
        total = 0
        q = Queue()
        q.enqueue(self.root)
        while q.is_empty() == False:
            node = q.dequeue()
            if not node:
                continue
            total += 1
            q.enqueue(node.left)
            q.enqueue(node.right)
        return total

    def height(self) -> int:
        """
        Returns the maximum depth of any node in the tree.
        Note: empty trees have a height of -1.
        """
        h = -1
        q = Queue()
        q.enqueue(self.root)
        q_size = 1
        while q.is_empty() == False:
            tmp = q_size
            q_size = 0
            h += 1
            for i in range(tmp):
                node = q.dequeue()
                if not node:
                    continue
                if node.left:
                    q.enqueue(node.left)
                    q_size += 1
                if node.right:
                    q.enqueue(node.right)
                    q_size += 1
        return h

    def count_leaves(self) -> int:
        """
        Returns number of leaves in tree self.
        """
        total = 0
        q = Queue()
        q.enqueue(self.root)
        while q.is_empty() == False:
            node = q.dequeue()
            if not node:
                continue
            if self._is_leaf(node):
                total += 1
            q.enqueue(node.left)
            q.enqueue(node.right)
        return total

    def count_unique(self) -> int:
        """
        Returns the count of unique values stored in the tree.
        If all values stored in the tree are distinct (no duplicates),
        this method will return the same result as the size() method.
        """
        duplicates = 0
        q = self.in_order_traversal()
        for i in range(self.size()):
            node = q.dequeue()
            while q.is_empty() == False:
                temp = q.dequeue()
                if temp == node:
                    duplicates += 1
        return self.size() - duplicates

    def _is_leaf(self, node: TreeNode) -> bool:
        """
        Returns whether node is a leaf
        """
        return node.left is None and node.right is None


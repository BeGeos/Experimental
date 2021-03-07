"""Implementation of binary search tree:
    - It's a rooted tree;
    - The left node is smaller than and the right node is bigger than the root on the nth node;
    - Every node has a key and a value
"""


class Node:

    def __init__(self, key, height=0, parent=None):
        self.key = key  # the actual number inside
        self.parent = parent
        self.height = height
        self.left = None
        self.right = None


class BST:
    tree = []
    position = 0
    max_height = 0
    k = 3

    def __init__(self, root, keys: list):
        self.root = Node(root, self.position)
        self.keys = keys
        self.build_tree()

    def build_tree(self):
        for key in self.keys:
            self.insert(self.root, key)
        return

    def insert(self, node, key):
        if node is None:
            return Node(key)
        else:
            if node.key == key:
                return node
            if key < node.key and self.is_available(node, key):
                node.left = self.insert(node.left, key)
            elif key > node.key and self.is_available(node, key):
                node.right = self.insert(node.right, key)
            else:
                return
        return node

    def is_available(self, node, key):
        """
            Specify the condition for insertion.
            Example:
            - Air Traffic Queue. Check whether the time of insertion already exists then return False;
              otherwise, if landing time is +- set minutes (3 min) from other landing times return False;
              Finally, if the check is successful return True and insert value in the queue.

        """

        if node is None or abs(node.key - key) >= self.k:
            return True
        return False

    def delete(self, root):
        pass

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.tree.append(node.key)
            self.inorder(node.right)
        return self.tree

    def search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def minimum(self, node):
        if node.left is None:  # base case when there is no left node
            return node
        return self.minimum(node.left)

    def maximum(self, node):
        if node.right is None:
            return node
        return self.maximum(node.right)


class AVL(BST):
    avl = []
    position = 0
    step = 0

    def __init__(self, root, keys: list):
        self.root = Node(root)
        self.keys = keys
        self.build_tree()
        # self.tree = self.inorder(self.root)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.avl.append(node.key)
            self.inorder(node.right)
        return self.avl

    def avl_insert(self, node, key, parent_node=None):
        """
            Parent Node: where I am coming from
            Node: the position I am validating to put the key
            Key: the actual number
        """

        if node is None:  # Actual insertion at left or right node
            self.position += 1
            if self.step >= self.root.height:
                self.root.height = self.step
            new_node = Node(key, self.step, parent_node)
            self.step = 0
            return new_node
        else:
            if node.key == key:
                return node

            # Discern going left if less than or right if greater than...
            if key < node.key and self.is_available(node, key):
                self.step += 1
                node.left = self.avl_insert(node.left, key, node)
            elif key > node.key and self.is_available(node, key):
                self.step += 1
                node.right = self.avl_insert(node.right, key, node)
            else:
                return
        return node

    def height(self, key):
        """
        Get the real height of the nodes other than the root.
        For root's height root.height is sufficient.
        """

        node = self.search(self.root, key)
        if node.left is None or node.right is None:
            return 0
        if node.key == self.root.key:
            return self.root.height
        return self.height(node.parent.key) - 1


"""
    Implementation of binary search tree:
    - It's a rooted tree;
    - The left node is smaller than and the right node is bigger than the root on the nth node;
    - Every node has a key and a value
"""


class Node:

    def __init__(self, key, parent=None):
        self.key = key  # the actual number inside
        self.parent = parent
        self.left = None
        self.right = None


class BST:
    max_height = 0
    k = 3

    def __init__(self, root, keys: list):
        self.root = Node(root, 0)
        self.keys = keys
        self.build_tree()
        self.height = self._height(self.root)

    def build_tree(self):
        """
        To insert the arguments passed in the __init__ method.
        Arguments can be inserted manually via the insert() method
        """

        for key in self.keys:
            self.insert(self.root, key)
        return

    def insert(self, node, key, parent_node=None):
        """
        An insert method with checks to keys for insertion

        :param node: of class Node, indicates a single node of the tree
        :param key: of class Any, indicates the value inserted in the node
        :param parent_node: of class node, indicates which node is parent to the current node
        :return: of class Node, it return the node with attributes
        """

        if node is None:  # Actual insertion at left or right node
            new_node = Node(key, parent_node)
            return new_node
        else:
            if node.key == key:
                return node

            # Discern going left if less than or right if greater than...
            if key < node.key and self.is_available(node, key):
                node.left = self.insert(node.left, key, node)
            elif key > node.key and self.is_available(node, key):
                node.right = self.insert(node.right, key, node)
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
        :return: boolean, True if the key follows the imposed constrains, False if it does not
        """

        if node is None or abs(node.key - key) >= self.k:
            return True
        return False

    def delete(self, root):
        pass

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key)
            self.inorder(node.right)

    def search(self, node, key):
        """
        :param node: of class Node, indicates the node. It should be root by default.
        :param key: of class Any, indicates the value to search
        :return: of class Node, returns the node with key == key
        """

        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def _height(self, node):
        """
        Get the real height of the nodes other than the root.

        Since the height changes with the insertion of new nodes, it is
        a dynamic attribute that is difficult to track from the Node class.
        This method copes with this fact, so the height won't be in memory
        but every call will trigger the function which yields the height as
        integer.
        """

        if node is None:
            return - 1
        return max(self._height(node.left), self._height(node.right)) + 1

    def minimum(self, node):
        """
        Method to retrieve the min from the tree --> complexity ~ O(lg(n))
        :param node: of class Node
        :return: of class Node
        """

        if node.left is None:  # base case when there is no left node
            return node
        return self.minimum(node.left)

    def maximum(self, node):
        """
        Method to retrieve the max from the tree --> complexity ~ O(lg(n))
        :param node: of class Node
        :return: of class Node
        """

        if node.right is None:  # base case when there is no right node
            return node
        return self.maximum(node.right)


class AVL(BST):
    avl = []

    # TODO avl_insert with check for height and rotation to fix balance
    def is_balanced(self, node):
        if abs(self._height(node.left) - self._height(node.right)) > 1:
            return False
        return True

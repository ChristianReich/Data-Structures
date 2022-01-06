"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2021-04-20"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy
from Queue_array import Queue


class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers 
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)            
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif value < node._value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif value > node._value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:

            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as 
        required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        self._root, value = self._remove_aux(self._root, key)
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Parameters:
            node - a bst node to search for key (_BST_Node)
            key - data to search for (?)
        Returns:
            node - the current node or its replacement (_BST_Node)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._value:
            # Search the left subtree.
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._value:
            # Search the right subtree.
            node._right, value = self._remove_aux(node._right, key)
        else:
            # Value has been found.
            value = node._value
            self._count -= 1
            # Replace this node with another node.
            if node._left is None and node._right is None:
                # node has no children.
                node = None

            elif node._left is None:
                # node has no left child.
                node = node._right

            elif node._right is None:
                # node has no right child.
                node = node._left

            else:
                # Node has two children
                repl_node = self._delete_node_left(node._left)
                left = node._left
                right = node._right
                node = repl_node
                node._left = left
                node._right = right

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
        return node, value

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node. This node 
                is the node with the maximum value in the deleted node's left
                subtree (_BST_Node)
        -------------------------------------------------------
        """

        if parent._right._right is not None:
            repl_node = self._delete_node_left(parent._right)
            parent._update_height()
        else:
            repl_node = parent._right
            parent._right = parent._right._left

        return repl_node

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """
        result = self._contains_aux(self._root, key)
        return result

    def _contains_aux(self, node, key):
        if node is None:
            result = False
        else:
            if node._value == key:
                result = True
            else:
                result = self._contains_aux(
                    node._right, key) or self._contains_aux(node._left, key)
        return result

    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """
        if self._root is not None:
            h = self._root._height
        else:
            h = 0
        return h

    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are identical.
        Use: b = bst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another bst (BST)
        Returns:
            identical - True if this bst contains the same values
            in the same order as other, otherwise returns False (boolean)
        -------------------------------------------------------
        """

        if self._count == other._count:
            if self._root is None:
                identical = True
            else:
                identical = self._is_identical_aux(self._root, other._root)
        else:
            identical = False
        return identical

    def _is_identical_aux(self, node, other_node):
        identical = False
        if node._left == other_node._left:
            identical = True
            if node._left is not None:
                identical = self._is_identical_aux(
                    node._left, other_node._left)
        if identical and node._right == other_node._right:
            identical = True
            if node._right is not None:
                identical = self._is_identical_aux(
                    node._right, other_node._right)
        return identical

    def parent(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        value = None
        node = self._root
        while node is not None and value is None:
            if node._right is not None and node._right._value == key:
                value = deepcopy(node._value)
            elif node._left is not None and node._left._value == key:
                value = deepcopy(node._value)
            else:
                if key > node._value:
                    node = node._right
                else:
                    node = node._left

        return value

    def parent_r(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        value = self._parent_r_aux(self._root, key)
        return value

    def _parent_r_aux(self, node, key):
        if node is None:
            value = None
        else:
            if node._right is not None and node._right._value == key:
                value = deepcopy(node._value)
            elif node._left is not None and node._left._value == key:
                value = deepcopy(node._value)
            else:
                if key > node._value:
                    value = self._parent_r_aux(node._right, key)
                else:
                    value = self._parent_r_aux(node._left, key)
        return value

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        node = self._root
        while node._right is not None:
            node = node._right
        max = node._value
        return max

    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        value = self.max_r_aux(self._root)
        return value

    def max_r_aux(self, node):
        if node._right is not None:
            value = self.max_r_aux(node._right)
        else:
            value = node._value
        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in BST. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        node = self._root
        while node._left is not None:
            node = node._left
        min = node._value
        return min

    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        value = self.min_r_aux(self._root)
        return value

    def min_r_aux(self, node):
        if node._left is not None:
            value = self.min_r_aux(node._left)
        else:
            value = node._value
        return value

    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: count = bst.leaf_count()
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """

        count = self._leaf_count_aux(self._root)
        return count

    def _leaf_count_aux(self, node):
        if node is None:
            count = 0
        else:
            if node._left is None and node._right is None:
                count = 1 + self._leaf_count_aux(node._left) + \
                    self._leaf_count_aux(node._right)
            else:
                count = self._leaf_count_aux(node._left) + \
                    self._leaf_count_aux(node._right)

        return count

    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """

        count = self._two_child_count_aux(self._root)
        return count

    def _two_child_count_aux(self, node):
        if node is None:
            count = 0
        else:
            if node._left is not None and node._right is not None:
                count = 1 + \
                    self._two_child_count_aux(
                        node._right) + self._two_child_count_aux(node._left)
            else:
                count = self._two_child_count_aux(node._left) + \
                    self._two_child_count_aux(node._right)

        return count

    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """

        count = self._one_child_count_aux(self._root)
        return count

    def _one_child_count_aux(self, node):
        if node is None:
            count = 0
        else:
            if node._left is None and node._right is not None:
                count = 1 + self._one_child_count_aux(node._right)
            elif node._left is not None and node._right is None:
                count = 1 + self._one_child_count_aux(node._left)
            else:
                count = self._one_child_count_aux(node._left) + \
                    self._one_child_count_aux(node._right)

        return count

    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """

        zero, one, two = self._node_count_aux(self._root)
        return zero, one, two

    def _node_count_aux(self, node):
        if node is None:
            zero = 0
            one = 0
            two = 0
        else:
            if node._left is None and node._right is None:
                zero, one, two = self._node_count_aux(node._right)
                zero2, one2, two2 = self._node_count_aux(node._left)
                zero += 1 + zero2
                one += one2
                two += two2
            elif node._left is None and node._right is not None:
                zero, one, two = self._node_count_aux(node._right)
                one += 1
            elif node._left is not None and node._right is None:
                zero, one, two = self._node_count_aux(node._left)
                one += 1
            elif node._left is not None and node._right is not None:
                zero, one, two = self._node_count_aux(node._right)
                zero2, one2, two2 = self._node_count_aux(node._left)
                zero += zero2
                one += one2
                two += 1 + two2
        return zero, one, two

    def total_depth(self):
        """
        ---------------------------------------------------------
        Returns the total depth of a bst.
        ---------------------------------------------------------
        Returns:
            the total depth count - i.e. the sum of all the node depths
            in the tree (int)
        ---------------------------------------------------------
        """

        total_d = self.total_depth_aux(self._root)
        return total_d

    def total_depth_aux(self, node):
        if node is None:
            total_d = 0
        else:
            total_d = node._height + self.total_depth_aux(node._left)
            total_d += self.total_depth_aux(node._right)
        return total_d

    def mirror(self):
        """
        ---------------------------------------------------------
        Creates a mirror version of a BST. All nodes are swapped with nodes on
        the other side the tree. Nodes may take the place of an empty spot.
        The resulting tree is a mirror image of the original tree. (Note that
        the mirrored tree is not a BST.) The original BST is unchanged.
        Use: tree = bst.mirror()
        ---------------------------------------------------------
        Returns:
            tree - a mirror version of subtree of node.
        ---------------------------------------------------------
        """

        # your code here

    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        balanced = False
        if self._root is None:
            balanced = True
        elif self._root._right is None and self._root._left is None and \
                self._root._value is not None:
            balanced = True
        else:
            if self._root._left is not None and self._root._right is not None:
                if self._root._left._height - self._root._right._height <= 1:
                    balanced = True
        return balanced

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """
        value = None
        value = self.retreive_r_aux(self._root, key)
        return value

    def retreive_r_aux(self, node, key):
        if node is not None:
            if node._value > key:
                value = self.retreive_r_aux(node._left, key)
            elif node._value < key:
                value = self.retreive_r_aux(node._right, key)
            else:
                value = deepcopy(node._value)
        else:
            value = None
        return value

    def average_depth(self):
        """
        ---------------------------------------------------------
        Returns the average depth of a bst.
        ---------------------------------------------------------
        Returns:
            avg-depth - total depth count divided by the number of nodes
                in the tree (int)
        ---------------------------------------------------------
        """

        total_d = self.total_depth()
        avg_d = total_d / self._count
        return avg_d

    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        if self._root is not None:
            valid = self._is_valid_aux(self._root)
        else:
            valid = True
        return valid

    def _is_valid_aux(self, node):
        valid = True
        if node._left is not None and node._left._value > node._value:
            valid = False
        if node._right is not None and node._right._value < node._value:
            valid = False

        # test height
        if node._left is None:
            left_height = 0
        else:
            left_height = node._left._height

        if node._right is None:
            right_height = 0
        else:
            right_height = node._right._height

        height = max(left_height, right_height) + 1
        if valid and height != node._height:
            valid = False

        if valid:
            valid_right = True
            valid_left = True
            if node._right is not None:
                valid_right = self._is_valid_aux(node._right)
            if node._left is not None:
                valid_left = self._is_valid_aux(node._left)
            valid = valid_right and valid_left
        return valid

    def update(self, value, update):
        """
        ---------------------------------------------------------
        Updates a value in a bst by applying a function to it.
        Use: bst.update(value, func)
        ---------------------------------------------------------
        Parameters:
            value - a comparable part of a data element (?)
            update - an update function compatible with value (function)
        Returns:
            updated - True if value is in bst and is updated, False if
            value is not in bst, but adds value to bst in that case.
            (Iterative algorithm.)
        --------------------------------------------------------- -
        """

        node = self._root
        updated = False
        while node is not None and not updated:
            if value > node._value:
                node = node._right
            elif value < node._value:
                node = node._left
            else:
                update(node)
                updated = True
        return updated

    def update_r(self, key, update):
        """
        ---------------------------------------------------------
        Updates a value in a bst by applying a function to it.
        Use: bst.update(value, func)
        ---------------------------------------------------------
        Parameters:
            value - a comparable part of a data element (?)
            update - an update function compatible with value (function)
        Returns:
            updated - True if value is in bst and is updated, False if
            value is not in bst, but adds value to bst in that case.
            (Recursive algorithm.)
        --------------------------------------------------------- -
        """

        updated = self.update_r_aux(self._root, key, update)
        return updated

    def update_r_aux(self, node, key, update):
        if node is not None:
            if key > node._value:
                updated = False
                updated = self.update_r_aux(node._right, key, update)
            elif key < node._value:
                updated = False
                updated = self.update_r_aux(node._left, key, update)
            else:
                update(node)
                updated = True
        else:
            updated = False
        return updated

    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """

        a = self._inorder_aux(self._root)
        return a

    def _inorder_aux(self, node):
        a = []
        if node is not None:
            a = self._inorder_aux(node._left)
            a.append(deepcopy(node._value))
            a += self._inorder_aux(node._right)
        return a

    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """

        a = self._preorder_aux(self._root)
        return a

    def _preorder_aux(self, node):
        a = []
        if node is not None:
            a.append(node._value)
            a += self._preorder_aux(node._left)
            a += self._preorder_aux(node._right)
        return a

    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """

        a = self._postorder_aux(self._root)
        return a

    def _postorder_aux(self, node):
        a = []
        if node is not None:
            a += self._postorder_aux(node._left)
            a += self._postorder_aux(node._right)
            a.append(node._value)

        return a

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        a = []
        if self._root is not None:
            q = Queue()
            q.insert(self._root)
            while not (q.is_empty()):
                node = q.remove()
                if node is not None:
                    a.append(deepcopy(node._value))
                    q.insert(node._left)
                    q.insert(node._right)
        return a

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """

        return self._count

    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)

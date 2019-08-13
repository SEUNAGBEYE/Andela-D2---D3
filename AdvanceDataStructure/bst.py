"""This module implements a binary search tree"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    A tree is a data structure composed of nodes It has the following characteristics:

    Each tree has a root node (at the top).
    The root node has zero or more child nodes.
    Each child node has zero or more child nodes, and so on.
    A binary search tree adds these two characteristics:

    Each node has up to two children.
    For each node, its left descendents are less than the current node, which is less than the right descendents.
    Binary search trees allow fast lookup, addition and removal of items. The way that they are set up means that, on average, each comparison allows the operations to skip about half of the tree, so that each lookup, insertion or deletion takes time proportional to the logarithm of the number of items stored in the tree.
    """

    def __init__(self):
        self.root = None
    
    def add(self, data):
        """Adds an element to the tree"""
        root = self.root

        if not root:
            self.root = Node(data)
            return
        else:
            def search_tree(node):
                if data < node.data:
                    if not node.left:
                        node.left = Node(data)
                        return
                    node = node.left
                    return search_tree(node)
                elif data > node.data:
                    if not node.right:
                        node.right = Node(data)
                        return
                    node = node.right
                    return search_tree(node)

            return search_tree(root)
    
    def find(self, data):
        """Finds the node of the given data in the tree"""
        root = self.root

        if data == root:
            self.root = Node(data)
            return self.root
        else:
            def search_tree(node):
                if data < node.data:
                    if not node.left:
                        return
                    if node.left.data == data:
                        return node.left
                    node = node.left
                    return search_tree(node)
                elif data > node.data:
                    if not node.right:
                        return
                    if node.right.data == data:
                        return node.right
                    node = node.right
                    return search_tree(node)

            return search_tree(root)

    def is_present(self, data):
        """Checks if a data is present in the tree"""
        return self.find(data) is not None

    def remove(self, data):
        """Removes a node from the tree"""
        def remove_node(node, data):
            # Return if data is not in the tree
            if not node:
                return

            if node.data == data:
                # node has no child, remove the node
                if not node.left and not node.right:
                    return
                
                # No right child, replace the node with the left child
                if not node.right:
                    return node.left
                
                # No left child, replace the node with its right child
                if not node.left:
                    return node.right

                # if we have two children, 
                # replace it with the value of its in-order successor ,
                # (a node with the least value in the right subtree),
                # recursively delete the in-order successor in the right subtree
                # check https://www.techiedelight.com/deletion-from-bst/ for reference
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.data = successor.data
                node.right = remove_node(node, successor.data)
            elif data < node.data:
                node.left = remove_node(node.left, data)
                return node
            else:
                node.right = remove_node(node.right, data)
                return node

        self.root = remove_node(root)
    
    def height(node):
        """Calculates the height of a node by recursively calculating the each of each subtre plus 1"""
        if node is None:
            return 0

        ldepth = height(node.left)
        rdepth = height(node.right)

        return max(ldepth, rdepth) + 1

    def is_balanced(self, node):
        """
        A tree where no leaf is much farther away from the root than any other leaf. Different balancing schemes allow different definitions of “much farther” and different amounts of work to keep them balanced.

        Consider a height-balancing scheme where following conditions should be checked to determine if a binary tree is balanced.
        An empty tree is height-balanced. A non-empty binary tree T is balanced if:
        1) Left subtree of T is balanced
        2) Right subtree of T is balanced
        3) The difference between heights of left subtree and right subtree is not more than 1.
        https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/
        """
        
        # An empty treee is always balanced
        if node is None:
            return True

        lh = self.height(node.left)
        rh = self.height(node.right)

        # balance factor of a node is lh - rh = {-1, 0, 1} or <= |1|
        # So we want to check if the root node is balanced, and each child is also balanced
        if abs(lh - rh) <= 1 and is_balanced(node.left) and is_balanced(node.right):
            return True
        
        # if we got here, it means the tree is not balanced
        return False

    @classmethod
    def test(cls, node):
        """Tests if a tree is a BST"""

        def test_node(node):
            if not node:
                return True

            if node.left is None and node.right is None:
                return True
            
            test_lsubtree = False
            test_rsubtree = False

            if not node.left:
                test_lsubtree = True

            if not node.right:
                test_rsubtree =  True
            
            if node.left and node.left.data < node.data:
                test_lsubtree = test_node(node.left)

            if node.right and node.right.data > node.data:
                test_rsubtree = test_node(node.right)

            return all([test_lsubtree, test_rsubtree])

        return test_node(node)

bst = BST()
bst.add(10)
bst.add(11)

tree = Node(3)
tree.right = Node(4)
tree.left = Node(1)
# test for bst on this tree will fail because 2 > 1 and was inserted on the right instead of the left
tree.left.left = Node(2)
tree.left.right = Node(5)
# test for bst on this tree will fail because 2 > 1 and was inserted on the right instead of the left
print('Test BST', BST.test(bst.root))
# test for bst on this tree will pass because,
#  the BST class was used to create this tree which respect the right and left principle of BST
print('Test BST', BST.test(tree))
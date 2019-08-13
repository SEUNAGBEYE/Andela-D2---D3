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

    But I think I could have added another column with a type of ltree for querying 

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

        if === root:
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

    # def remove(self, data):
    #     """Removes a node from the tree"""
    #     root = self.root

    #     if data == root.data:
            

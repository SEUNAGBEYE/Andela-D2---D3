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
            else if data < node.data:
                node.left = remove_node(node.left, data)
                return node
            else:
                node.right = remove_node(node.right, data)
                return node

        self.root = remove_node(root)
            

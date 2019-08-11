"""This module will implement a linked list in Python"""

class Node:
    """The node of the linked list"""
    def __init__(self, node):
        self.value = node # Data
        self.next = None # Reference to the next node in the list

class LinkedList:
    """
    A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers as shown in the below image:
    """"

    def __init__(self):
        this.head = None
        this.size = 0
    
    def get_size(self):
        return self.size
    
    def add(self, element):
        """Adds the given element to end of the list"""
        node = Node(value)
        current_node = self.head
        # We want to set the head and the tail to the current node if we don't have one
        if not current_node:
            self.head = node
        else:
            # Keep getting the last item if we have one
            while current_node.next:
                previous_node = current_node
                current_node = current_node.next
            
            # Add the next item to the list
            current_node.next = node

        self.size += 1 
    
    def remove(self, element):
        """Removes the first item found in the list

        params: element - Data of the node to remove
        """

        current_node = self.head
        # Short circuit this function we we have no item to remove
        if not current_node:
            return
        
        if current_node.value == element:
            self.head = None
            self.size = 0
        else:
            while current_node.next:
                previous_node = current_node
                # Get the next node since the current one is not what we want
                current_node = current_node.next
                if current_node.value == element:
                    previous_node.next = current_node.next
                    self.size -= 1
                    return # End the loop if we've found the node
    
    def add_element_at(self, element, index):
        "Adds the element to the given index if within the list range, else returns None"
        node = Node(element)
        current_node = self.head
        current_index = 0
        if index < 0:
            return
        
        if index > self.size:
            return

        if index == 0:
            node.next = current_node
            self.head = current_node
        else:
            while current_index < index:
                current_index += 1
                previous_node = current_node
                current_node = current_node.next
            

            previous_node.next = node
            node.next = current_node

        this.size += 1

    def remove_element_at(self, index):
        "Removes and return the element at a given index if within the list range, else returns None"
        current_node = self.head
        current_index = 0

        if index < 0:
            return
        
        if index > self.size:
            return

        if index == 0:
            self.head = current_node.next
            self.head = current_node
        else:
            while current_index < index:
                current_index += 1
                previous_node = current_node
                current_node = current_node.next
            
            previous_node.next = current_index.next

        this.size -= 1
        return current_node.value
    
    def get_element_at(self, index):
        "Gets the element at the given index if found, else return None"
        current_node = self.head
        current_index = 0

        if index < 0:
            return
        
        if index > self.size:
            return

        while current_index < index:
            current_index += 1
            previous_node = current_node
            current_node = current_node.next
        
        return current_node.value

    def get_index(self, element):
        """Gets the index of the element if found, else None"""
        current_node = self.head
        current_index = -1 

        while current_node:
            current_index += 1
            current_node = current_node.next
            if current_node.value == element:
                return current_index      
        return None

    
            
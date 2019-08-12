"""This module will implement a linked list in Python"""

class Node:
    """The node of the linked list"""
    def __init__(self, node):
        self.value = node # Data
        self.next = None # Reference to the next node in the list

class LinkedList:
    """
    A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers as shown in the below image:
    """

    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def __repr__(self):
        current_node = self.__head
        items = [current_node.value] if current_node else []
        while current_node and current_node.next:
            current_node = current_node.next
            items.append(current_node.value)

        return f"""LinkedList \n Size: {self.__size} \n Items: {items}"""
    
    
    def head(self):
        return self.__head

    def is_empty(self):
        return self.__size == 0

    def size(self):
        return self.__size
    
    def add(self, element):
        """Adds the given element to end of the list"""
        node = Node(element)
        current_node = self.__head
        # We want to set the head and the tail to the current node if we don't have one
        if not current_node:
            self.__head = node
        else:
            # Keep getting the last item if we have one
            while current_node.next:
                previous_node = current_node
                current_node = current_node.next
            
            # Add the next item to the list
            current_node.next = node

        self.__size += 1 
    
    def remove(self, element):
        """Removes the first item found in the list

        params: element - Data of the node to remove
        """

        current_node = self.__head
        # Short circuit this function we we have no item to remove
        if not current_node:
            return
        
        if current_node.value == element:
            current_node = current_node.next
            self.__head = current_node
            self.__size = self.__size - 1 if self.__size else 0
        else:
            while current_node.next:
                previous_node = current_node
                # Get the next node since the current one is not what we want
                current_node = current_node.next
                if current_node.value == element:
                    previous_node.next = current_node.next
                    self.__size -= 1
                    return # End the loop if we've found the node
    
    def add_at_index(self, element, index):
        "Adds the element to the given index if within the list range, else returns None"
        node = Node(element)
        current_node = self.__head
        current_index = 0
        if index < 0:
            return
        
        if index > self.__size:
            return

        if index == 0:
            self.__head = node
            self.__head.next = current_node
        else:
            while current_index < index:
                current_index += 1
                previous_node = current_node
                current_node = current_node.next
            

            previous_node.next = node
            node.next = current_node

        self.__size += 1

    def remove_at_index(self, index):
        "Removes the element at a given index if within the list range, else returns None"
        current_node = self.__head
        current_index = 0

        if index < 0:
            return
        
        if index > self.__size:
            return

        if index == 0:
            current_node = current_node.next
            self.__head = current_node
        else:
            while current_index < index:
                current_index += 1
                previous_node = current_node
                current_node = current_node.next
            
            previous_node.next = current_node.next

        self.__size -= 1
    
    def get_at_index(self, index):
        "Gets the element at the given index if found, else return None"
        current_node = self.__head
        current_index = 0

        if index < 0:
            return
        
        if index > self.__size:
            return

        while current_index < index:
            current_index += 1
            previous_node = current_node
            current_node = current_node.next
        
        return current_node.value

    def index(self, element):
        """Gets the index of the element if found, else None"""
        current_node = self.__head
        current_index = -1 

        while current_node:
            current_index += 1
            if current_node.value == element:
                return current_index 
            current_node = current_node.next
        return None
    

fruits = LinkedList()
fruits.add('Apple')
fruits.add('Banana')
fruits.add('Grape')
print('Fruits: ', fruits)
print('Index Of: ', fruits.index('Banana'))
print('Index Of: ', fruits.remove('Banana'))
print('Fruits: ', fruits)
print('Get by index: ', fruits.get_at_index(0))

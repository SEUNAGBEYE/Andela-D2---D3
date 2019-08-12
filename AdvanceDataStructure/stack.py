"""This module will implement a stack in Python"""

class Stack:
    def __init__(self):
        self.__store = {}
        self.__count = 0
    
    def size(self):
        """Gets the size of the stack"""
        return self.__count

    def is_empty(self):
        """Checks if the stack is empty"""
        return self.__count == 0

    def push(self, value):
        """Add an item to the stack"""
        self.__count += 1
        self.__store[self.__count] = value
    
    def pop(self):
        """Removes the last item in the stack"""
        if not self.__count:
            return
        item = self.__store[self.__count]
        del self.__store[self.__count]
        self.__count -= 1
        return item

    def peek(self):
        """Returns the item in the stack"""
        if not self.__count:
            return
        return self.__store[self.__count]

    def __repr__(self):
        """Returns the string repr of the stack"""
        return f"Stack: \n Size: {self.__count} \n Items: {self.__store}"

book = Stack()
book.push('Harry potter')
book.push('The Hobbit')
book.push('The last day at Forcado high school')
print(book)
print(book.pop())
print(book)


    

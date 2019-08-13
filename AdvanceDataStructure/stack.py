"""This module will implement a stack in Python"""

class Stack:
    """
    A stack is a basic data structure where you can only insert or delete items at the top of the stack.

    Algo   Ave  Worst
    Space  O(n) O(n)
    Search O(n) O(n)
    Insert O(1) O(1)
    Delete O(1) O(1)
    """
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
        """Returns the last item in the stack"""
        if not self.__count:
            return
        return self.__store[self.__count]

    def __repr__(self):
        """Returns the string repr of the stack"""
        return f"Stack: \n Size: {self.__count} \n Items: {self.__store}"

book = Stack()
book.pop()
print('Peek', book.peek())
print(book)
book.push('Harry potter')
book.push('The Hobbit')
book.push('The last day at Forcado high school')
print(book)
print(book.pop())
print(book)


    

"""This module will implement a queue in Python"""

class Queue:
    """
    A Queue a data structure that returns the first item added to a collection when an item is requested.
    
    Algo   Ave  Worst
    Space  O(n) O(n)
    Search O(n) O(n)
    Insert O(1) O(1)
    Delete O(1) O(1)
    """
    def __init__(self):
        self.__store = []
        self.__count = 0
    
    def size(self):
        """Gets the size of the queue"""
        return self.__count

    def is_empty(self):
        """Checks if the queue is empty"""
        return self.__count == 0

    def enqueue(self, value):
        """Add an item to the queue"""
        self.__count += 1
        self.__store.append(value)
    
    def dequeue(self):
        """Removes the last item in the queue"""
        if not self.__count:
            return

        item = self.__store[0]
        del self.__store[0]
        self.__count -= 1
        return item

    def peek(self):
        """Returns the first item in the queue"""

        if not self.__count:
            return
        return self.__store[0]

    def __repr__(self):
        """Returns the string repr of the queue"""
        return f"Queue: \n Size: {self.__count} \n Items: {self.__store}"

if __name__ == '__main__':
    pizzas = Queue()
    pizzas.enqueue('Chicken bbq')
    pizzas.enqueue('Pepperoni')
    print('Peek', pizzas.peek())
    pizzas.enqueue('Suya')
    print(pizzas)
    print('Dequeue', pizzas.dequeue())
    print(pizzas)
    print('Peek', pizzas.size())



    

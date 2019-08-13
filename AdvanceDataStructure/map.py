"""This module implements a map"""

class Map:
    """
    A map is a data structure that stores data in key / value pairs where every key is unique. A map is sometimes called an associative array or dictionary. It is often used for fast look-ups of data.
    """

    def __init__(self):
        self.__store = {}
        self.__count = 0
    
    def has(self, key):
        """Checks if the given key is in the map"""
        return key in self.__store
    
    def set(self, key, value):
        """Adds a key value pair to the map if not present"""
        if self.has(key):
            return
        self.__store[key] = value
        self.__count += 1
    
    def get(self, key):
        """Returns the value of the given key in the map"""
        if self.has(key):
            return self.__store[key]
    
    def delete(self, key):
        """Deletes an item from map with the key provided"""
        if self.has(key):
            del self.__store[key]
            self.__count -= 1
    
    def values(self):
        """Returns the values of the map"""
        values = []
        # We want to write the code to get the values instead of using self.___store.values()
        for key in self.__store:
            values.append(self.__store[key])
        return values

    def keys(self):
        """Returns the keys of the map"""
        keys = []
        # We want to write the code to get the keys instead of using self.___store.keys()
        for key in self.__store:
            keys.append(key) 
        return keys
    
    def size(self):
        """Gets the size of the map"""
        return self.__count

    def is_empty(self):
        """Checks if the map is empty"""
        return self.__count == 0
    
    def __repr__(self):
        """Returns the string repr of the map"""
        return f"""Map: \n Size: {self.__count} \n Items: {self.__store}"""

phonebook = Map()
phonebook.set('Adam', '002')
phonebook.set('Boyle', '409')
phonebook.set('Charles', '500')
print(phonebook)
print('adam in phonebook', phonebook.has('adam'))
print('Adam in phonebook', phonebook.has('Adam'))
print('Keys', phonebook.keys())
print('Values', phonebook.values())
phonebook.delete('Adam')
print('Adam in phonebook', phonebook.has('Adam'))
print('Get Adam', phonebook.get('Adam'))
print('Get Charles', phonebook.get('Charles'))
print(phonebook)
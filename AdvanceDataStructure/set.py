""""""

class Set:
    """
    The set data structure stores values without any particular order and with no repeated values. Besides being able to add and remove elements to a set, there are a few other important set functions that work with two sets at once.

    Union — This combines all the items from two different sets and returns this as a new set (with no duplicates).
    Intersection — Given two sets, this function returns another set that has all items that are part of both sets.
    Difference — This returns a list of items that are in one set but NOT in a different set.
    Subset — This returns a boolean value that shows if all the elements in one set are included in a different set.
    """

    def __init__(self):
        self.__collection = []
        self.__count = 0
    
    def values(self):
        """Returns the values of the set"""
        return self.__collection
    
    def size(self):
        """Returns the size of the set"""
        return self.__count

    def is_empty(self):
        """Returns True if set is empty, else False"""
        return self.__count == 0
    
    def add(self, element):
        """Adds an item to the set if not present and return True, else return False"""
        if element not in self.__collection:
            self.__collection.append(element)
            self.__count += 1
            return True
        else:
            return False
    
    def remove(self, element):
        """Removes an item from the set if present and return True, else return False"""
        if element not in self.__collection:
            return False
        
        for index, value in enumerate(self.__collection[:]):
            if value == element:
                self.__collection.remove(element)
                self.__count -= 1
                return True
    
    def union(self, other_set):
        """Returns a new set with all the elements in the two sets without duplicating any values"""
        union_set = Set()
        for value in self.__collection:
            union_set.add(value)

        for value in other_set.values():
            union_set.add(value)

        return union_set

    def difference(self, other_set):
        """Returns a new set with the items not present in the both"""
        difference_set = Set()
        other_set_values = other_set.values()

        for value in self.__collection:
            if value not in other_set_values:
                difference_set.add(value)

        return difference_set

    def intersection(self, other_set):
        """Returns a set with items present in both set"""
        intersect_set = Set()

        for value in other_set.values():
            if value in self.__collection:
                intersect_set.add(value)

        return intersect_set

    def subset(self, other_set):
        """Tests if the set is a subset of a different set"""
        other_set_values = other_set.values()
        subtest = ([True if value in other_set_values else False for value in self.__collection])
        if subtest:
            return all(subtest)
        return False
    
    def __repr__(self):
        return f"Set: \n Size: {self.__count} \n Items: {self.__collection}"

first_set = Set()
second_set = Set()
second_set.add(1)
second_set.add(3)
first_set.add(1)
first_set.add(2)
first_set.add(3)
first_set.add(4)
print(first_set)
print(first_set.difference(second_set))
print(second_set.difference(first_set))
print(second_set.intersection(first_set))
print(second_set.subset(first_set))
second_set.add(11)
print(second_set.subset(first_set))
print(first_set.union(second_set))
first_set.remove(4)
print(first_set)


        
                
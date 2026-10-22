# Sets 
# set is a collection of unique elements. It is unordered, meaning that the items do not have a defined order, and it does not allow duplicate values.

numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,10}

# if we store a duplicate value in a set, then it will automatically remove the duplicate value and store only unique values in the set.
print(numbers)

empty_set = set() # this is how we can create an empty set. And this is called a set constructor.
# we not use empty_set = {} because this will create an empty dictionary instead of an empty set.

# add values to a set 
numbers.add(11)

# remove values from a set 
numbers.remove(11) # this will remove the value 11 from the set. If the value is not present in the set, it will raise a KeyError.

# remove a random value from the set
numbers.pop() # this will remove an arbitrary value from the set. If the set is empty, it will raise a KeyError.

# return new unique set by combining two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# union of two sets
set3 = set1.union(set2)
print(set3) # this will return a new set containing all unique elements from both sets.

# return new intersection set by combining two sets
set4 = set1.intersection(set2)
print(set4) # this will return a new set containing only the elements that are present in both sets.

# return new difference set by combining two sets
set5 = set1.difference(set2)
print(set5) # this will return a new set containing only the elements that are present in

# return new outersection set by combining two sets
set6 = set1.symmetric_difference(set2)
print(set6) # this will return a new set containing only the elements that are present in either set1 or set2 but not in both.
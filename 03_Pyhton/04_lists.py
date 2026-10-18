# List
# list is a mutable sequence of value
# we can store multiple type of data

marks= [99, 89, 100, 65, 53]

# print list and type
print(marks, " " , type(marks))

# print length of list
print("length of marks list", len(marks))

# get element
print("first value of marks", marks[0])

# get part of a list 
print("Get a sublist or part of list: ",marks[1:4]) 

# check for an item
bool = 99 in marks
print("check is 99 value in marks list: ",bool)

# add one item
marks.append(75)
print("add new value : ",marks)

# add several items
marks.extend([100,23])
print("Add multiples items in a list: ", marks)

# insert an item in choosed index
marks.insert(0,19)
print("Insert an item in specific index: ", marks)

# remove item by value
marks.remove(100)
print("Remove item by value: ", marks)

# remove item by index
marks.pop(0)
print("Remove item by index: ", marks)

# count a value, how many time it's repeat
print("Count a value, How many times it's repeat: example : 23 -> ",marks.count(23))

# find a value's index 
print("Find value's index : example 23 -> index is ", marks.index(23))

# sort list 
marks.sort()
print("Sort marks: ", marks)

# reverse list
marks.reverse()
print(" Reverse list of marks ", marks)

# copy the list 
new_marks = marks.copy()
print("Copy of list.")

# clear the list 
marks.clear()
print("Clear the list.")

# loop in list
print("Loop in List",end=" ")
x = 23
for val in new_marks:
    if (val == x):
        print(val)
        break
    else:
        continue
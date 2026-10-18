# Tuples
# tuples is immutable sequence of value

tup = (2,2,1,3,4,4)

# get tuple
print(tup)

# get length of tuple
print("Lenght of tuple", len(tup))

# get item in tup
print("Get items in tuple: ", tup[0])

# get slice 
print("Get slice of tuple ", tup[1:3])

# check if item exist
print("Check if 5 exist in tuple:",(5 in tup))

# count item
print("Count item 4",tup.count(4))

# find item's index
print("Find item's index (2):",tup.index(2))

# join two tuples 
new_tup = (6,7,8)
print("join two tuples: ", tup + new_tup)


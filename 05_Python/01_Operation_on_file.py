# File Operations

# Three basic Operation like Open, read & close 

#  first Open 

file1 = open('05_Python/Folder/data1.txt', 'r')

print(file1.read()) # all of this data store in string

file1.close()

# file2 = open('05_Python/Folder/data1.txt', 'w')

# file2.write("This is my first file operation in python\n")

# file2.close()
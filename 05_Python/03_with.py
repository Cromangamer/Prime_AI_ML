# we don't want that the someone open and close the file and forget to close it, so we use the with statement

with open('05_Python/Folder/data1.txt', 'r') as file1:
    content = file1.read()
    print(content)
    print(len(content)) # all of this data store in string


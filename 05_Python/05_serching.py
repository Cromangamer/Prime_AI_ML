# Searching for a specific string in a file
with open("05_Python/Folder/data2.txt", "r") as file:
    print(type(file))
    for line in file:
        if "A" in line:
            print(line) 
    
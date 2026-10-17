age = int(input("Enter your age: "))

if age < 13:
    print("You are a minor.")
elif (age >= 13 and age < 18):
    print("You are a teenager.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# we can do nesting on the if else statements as well
if age < 13:
    if age < 5:
        print("You are a toddler.")
    else:
        print("You are a child.")
elif (age >= 13 and age < 18):
    if age < 16:
        print("You are a young teenager.")
    else:
        print("You are an older teenager.")
elif age < 60:
    if age < 30:
        print("You are a young adult.")
    else:
        print("You are a middle-aged adult.")
else:
    if age < 75:
        print("You are a young senior citizen.")
    else:
        print("You are an older senior citizen.")

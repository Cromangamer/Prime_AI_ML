# While Loop

count = 0

while count < 5:
    print("Count:", count)
    count += 1  # Increment the count by 1

# for Loop

for i in range(5):
    print("Iteration:", i)

# Nested Loops

number = int(input("Enter a number: "))
first = input("Enter the first character: ")
second = input("Enter the second character: ")

for i in range(number):
    for j in range((number-1) - i):
        print(second,' ', end='')  # Print spaces for alignment
    if i == 0:
        a = i + 1
    else:
        a += 2
    for j in range(a):
        print(first,' ', end='')  # Print a star without a newline
    for j in range((number-1) - i):
        print(second,' ', end='')  # Print spaces for alignment
    print()  # Print a newline after each row
number = (number*2) - 2  # Decrement the number for the next pattern
total = number // 2  # Calculate the total number of rows for the next pattern
for i in range(total):
    for j in range(i + 1):
        print(second,' ', end='')  # Print spaces for alignment
    if i == 0:
        a = i + 1
    else:
        a += 2
    for j in range(number - a):
        print(first,' ', end='')  # Print a star without a newline
    for j in range(i + 1):
        print(second,' ', end='')  # Print spaces for alignment
    print()  # Print a newline after each row



# example of using break and continue in loops
while True:
    user_input = input("Enter a number (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the loop.")
        break  # Exit the loop if the user types 'exit'
    elif not user_input.isdigit():
        print("Please enter a valid number.")
        continue  # Skip the rest of the loop and ask for input again
    else:
        number = int(user_input)
        print(f"You entered: {number}")

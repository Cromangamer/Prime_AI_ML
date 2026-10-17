# Q1. Write a program that takes salary as input. using conditional statements, calculate the final tax rate based on these rules:
# if salary < 30,000 -> 5%
# if salary is 30,000-70,000 -> 15%
# if salary > 70,000 -> 25%
'''
salary = int(input("Enter your salary: "))

if salary < 30000:
    print("your in-hand salary is ", salary - (salary*(5/100)))
elif salary >= 30000 and salary <= 70000 :
    print("your in-hand salary is ", salary - (salary*(15/100)))
else :
    print("your in-hand salary is ", salary - (salary*(25/100)))
'''
# Q2. Write a function that takes two integers a and b and prints all even numbers between them (inclusive)
'''
a = int(input("Enter start number "))
b = int(input("Enter end number "))

for i in range(a,b+1):
    if (i%2)==0 :
        print(i, sep=" ")
    else :
        continue
'''

# Q3. Write a function that prints the digits of a number, n 
# For eg: n=312 , there are 3 digits in it 3, 1 and 2 & we need to print them

n = int(input("Enter your number: "))

number_str = str(n)
lent = len(number_str)
i = 1

print("in your number ", n , ", there are ", lent," digits. And that is ", end="")
for char in number_str:
    print(char, ", ",end="")
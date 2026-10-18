#  string formatting

#  we have two type to do this 
# 1 format()
# 2 f-string()

a = 5 
b = 10
sum = a + b

# normal fomatting
print("sum if {}".format(sum))
print("Sum of {} & {} is {}".format(a,b,sum))

# index based formatting
print("index base Sum of {1} & {2} is {0}".format(sum , a , b))

# value based formatting
print("value based {a} & {b}".format(a=1,b=2))

# f-string formatting
print(f"Sum of {a} and {b} is {sum}")
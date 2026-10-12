# Type Caseting 

# we are doing with the help of built-in functions

# int() - converts a value to an integer
# float() - converts a value to a float
# str() - converts a value to a string

# Example 1: Converting a float to an integer
float_num = 3.14
int_num = int(float_num)
print(int_num)  # Output: 3

# Example 2: Converting an integer to a float
int_num = 5
float_num = float(int_num)
print(float_num)  # Output: 5.0

# Example 3: Converting a string to an integer
str_num = "10"
int_num = int(str_num)
print(int_num)  # Output: 10

# Example 4: Converting a string to a float
str_num = "3.14"
float_num = float(str_num)
print(float_num)  # Output: 3.14


# Type Conversion

# we are not doing actually type change in variables Pythone automatically converts the data type of the variable based on the operation being performed.

# Example 1: Adding an integer and a float
int_num = 5
float_num = 3.14
result = int_num + float_num  # The integer is automatically converted to a float
print(type(result), result)  # Output: <class 'float'> 8.14

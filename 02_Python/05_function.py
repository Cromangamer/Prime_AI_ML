def hello(name):
    print(f"Hello, {name}!")

hello("Alice")


# lambda function
add = lambda x, y: x + y

add(5, 3)  # Output: 8

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
factorial()  # Output: 120

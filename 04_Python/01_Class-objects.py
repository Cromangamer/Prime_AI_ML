class Student:

    PI = 3.14159  # Class attribute

    def __init__(self, name, age): # self is a reference to the current instance of the class
        self.name = name # instance attribute
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @classmethod # this is a class method, it takes cls as the first parameter instead of self
    def get_value(cls):
        print(cls.PI)  # Accessing class attribute using cls

    @staticmethod # this is a static method, it does not take self or cls as the first parameter
    def set_value(value):
        print(f"Class attribute PI is set to: {value}")


student1 = Student("Alice", 20)
student1.display()  # Output: Name: Alice, Age: 20

# Attributes can be modified after the object is created
student1.age = 21
student1.display()  # Output: Name: Alice, Age: 21



# cls attribute can be accessed using the class name as well
# but cls can not accessed using the instance of the class
# if i want to access functions without creating an instance of the class, i can use class methods (@classmethod) or static methods (@staticmethod)
Student.get_value()  # Output: 3.14159
Student.set_value(3.14159)  # Output: Class attribute PI is set to: 3.14159

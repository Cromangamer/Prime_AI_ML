# 1 . function overriding 
    # let's sapose we have a class called Animal and it has a method called sound. Now we have two subclasses called Dog and Cat which inherit from the Animal class. Both subclasses override the sound method to provide their own implementation.

# 2. duck typing
#  In Python, duck typing is a concept where the type or class of an object is determined by its behavior (methods and properties) rather than its actual class. This means that if an object behaves like a certain type (e.g., it has a method called "quack"), it can be treated as that type, regardless of its actual class.


class Employee:
    def get_designation(self):
        print("Employee")

class Teacher(Employee):
    def get_designation(self):
        print("Teacher")

class Engineer(Employee):
    def get_designation(self):
        print("Engineer")

t = Teacher()
e = Engineer()
t.get_designation()
e.get_designation()




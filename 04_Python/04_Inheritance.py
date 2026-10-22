class Employee: 
    start_time = "9 AM" # class attribute
    end_time = "5 PM" # class attribute

    def __init__(self, name, salary):
        self._name = name # protected attribute
        self.__salary = salary # private attribute

    def get_salary(self):
        return self.__salary

class Teacher(Employee):

    def __init__(self, subject, name, salary):
        super().__init__(name, salary)
        self._subject = subject
        
    def get_info(self):
        print(f"Teacher Name is {self._name}. Her subject is {self._subject} and Salary is {super().get_salary()} ")

t1 = Teacher("English", "Honey", 10_000)

t1.get_info()
# Exception Handling in Python
# try, except, finally, else

class CustomError(Exception):
    x = 0;

    def __init__(self):
        self.x = self.take_input()
        self.validate_input(self.x)

    def take_input(self):
        x = input("Enter a number: ")
        return x

    def validate_input(self, x):
        try:
            x = int(x)
            print("You entered:", x)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        finally:
            print("Execution completed.")

class run(CustomError):
    def __init__(self, loop=3):
        for i in range(loop):
            super().__init__()


runTimes = input("Enter the number of times you want to run the program: ")
run(int(runTimes)) 
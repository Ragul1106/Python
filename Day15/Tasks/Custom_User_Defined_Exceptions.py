# 31. Create a custom exception NegativeNumberError and raise it
class NegativeNumberError(Exception):
    pass

num = int(input("Enter a positive number: "))
if num < 0:
    raise NegativeNumberError("Number cannot be negative!")

# 32. Define InvalidAgeError and use it in age-based logic
class InvalidAgeError(Exception):
    pass

age = int(input("Enter your age: "))
if age < 0 or age > 120:
    raise InvalidAgeError("Invalid age!")

# 33. Build a banking app with InsufficientFundsError
class InsufficientFundsError(Exception):
    pass

balance = 100
withdraw = 150
if withdraw > balance:
    raise InsufficientFundsError("Not enough funds!")

# 34. Create a grading app and raise GradeOutOfRangeError for marks > 100
class GradeOutOfRangeError(Exception):
    pass

marks = int(input("Enter marks: "))
if marks > 100:
    raise GradeOutOfRangeError("Marks cannot exceed 100!")

# 35. Raise UnauthorizedAccessError in a mock role-based system
class UnauthorizedAccessError(Exception):
    pass

role = "user"
if role != "admin":
    raise UnauthorizedAccessError("Access denied!")

# 36. Use custom exception for invalid file format in a file uploader
class InvalidFileFormatError(Exception):
    pass

filename = "document.pdf"
if not filename.endswith(".txt"):
    raise InvalidFileFormatError("Only .txt files allowed!")

# 37. Create LoginAttemptsExceeded for user login system
class LoginAttemptsExceeded(Exception):
    pass

attempts = 5
if attempts >= 3:
    raise LoginAttemptsExceeded("Too many login attempts!")

# 38. Create a class-level exception to enforce object state rules
class StateError(Exception):
    pass

class Robot:
    def __init__(self):
        self.powered_on = False
    
    def activate(self):
        if self.powered_on:
            raise StateError("Robot is already on!")
        self.powered_on = True

robot = Robot()
robot.activate()
robot.activate()  

# 39. Create a file validation system that raises FileTooLargeError
class FileTooLargeError(Exception):
    pass

file_size = 10 * 1024 * 1024  
if file_size > 5 * 1024 * 1024:  
    raise FileTooLargeError("File exceeds size limit!")

# 40. Build a temperature converter and raise exception if below absolute zero
class BelowAbsoluteZeroError(Exception):
    pass

def kelvin_to_celsius(k):
    if k < 0:
        raise BelowAbsoluteZeroError("Temperature cannot be below absolute zero!")
    return k - 273.15

kelvin_to_celsius(-5)  
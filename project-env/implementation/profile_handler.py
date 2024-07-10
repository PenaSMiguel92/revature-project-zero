import os.path as Path
from interface.input_validation import InputValidation
from interface.profile_interface import ProfileInterface
from custom_exceptions.invalid_profile import InvalidProfileException

class ProfileHandler(InputValidation, ProfileInterface):
    def __init__(self):
        self.name = ''
        self.height = 0
        self.age = 0
    # def __init__(self, name: str, height: int, age: int) -> None:
    #     #For now, any other attributes will be beyond the scope of this project.
    #     self.name = name
    #     self.height = height
    #     self.age = age

    # def __str__(self):
    #     return f"Name: {self.name}"
    def create_profile(self) -> bool:

        name_input = input("Please enter your name: ")
        if not self.validate_input(name_input, string_input = True):
            raise InvalidProfileException('Please enter a longer name.')
        
        file_name = f"data\{name_input}_data.csv"
        if Path.isfile(file_name):
            raise InvalidProfileException('Profile already exists! Please try again.')
        
        age_input = input("Please enter your age: ")
        if not self.validate_input(age_input, integer_input = True):
            raise InvalidProfileException('Please enter a number.')
        if int(age_input) < 20:
            raise InvalidProfileException('You are too young.')
        
        height_input = input("Please enter your height in inches: ")
        if not self.validate_input(height_input, integer_input = True):
            raise InvalidProfileException("Please enter a number.")
        height_input_int = int(height_input)
        if not (20 < height_input_int < 100):
            raise InvalidProfileException("Please enter a valid height.")
        
        with open(file_name, 'w+'): 
            pass

        return True
        
    
    def load_profile(self) -> bool:
        user_input = input("Please enter your name: ")
        if not InputValidation.validate_input(user_input, string_input = True):
            raise InvalidProfileException('Name is too short.')
        file_name = f"data\{user_input}_data.csv"
        if not Path.isfile(file_name):
            raise InvalidProfileException('File does not exist, please create profile.')
        
        with open(file_name, 'r'):
            pass #make sure to load height and age from the file.
        
        return True
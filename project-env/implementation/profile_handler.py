import os
from interface.input_validation import InputValidation
from interface.profile_interface import ProfileInterface
from custom_exceptions.invalid_profile import InvalidProfileException

class ProfileHandler(ProfileInterface):
    
    # def __init__(self, name: str, height: int, age: int) -> None:
    #     #For now, any other attributes will be beyond the scope of this project.
    #     self.name = name
    #     self.height = height
    #     self.age = age

    # def __str__(self):
    #     return f"Name: {self.name}"

    @staticmethod
    def create_profile() -> None:
        user_input = input("Please enter your name: ")
        if not InputValidation.validate_input(user_input, string_input = True):
            raise InvalidProfileException('Please enter a longer name.')
        file_name = f"data\{user_input}_data.csv"
        if not os.path.isfile(file_name):
            with open(file_name, 'w+'): pass
        
    
    def load_profile(self) -> None:
        return super().load_profile()
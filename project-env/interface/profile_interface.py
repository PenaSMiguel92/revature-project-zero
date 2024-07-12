from abc import ABC, abstractmethod

class ProfileInterface(ABC):
    
    @abstractmethod
    def create_profile(self) -> bool:
        """
            This method will ask the user to input: name, height, and age. It will check if a file exists with their name, if not create one and save height and age to it.

            This method will return a True boolean value if a profile was created successfully.

            This method will raise InvalidProfileException if either input is invalid.
        """
        pass

    @abstractmethod
    def load_profile(self) -> bool:
        """
            This method will ask the user to specify their name, and it will then look for a file with their name. If it exist, then load the profile details from it. 

            This method will return a True boolean value if a profile was loaded successfully.

            This method will raise InvalidProfileException if the profile specified does not exist.
        """
        pass

    def get_filename(self) -> str:
        """
            This method should return a properly formatted file name.
        """
        pass

    def get_const_biostats(self) -> list[int]:
        """
            This method should return height and age in a tuple, which are constant across BMI measurements, hence constant biostats.
        """
        pass
from abc import ABC, abstractmethod

class ProfileInterface(ABC):
    
    @abstractmethod
    def create_profile(self) -> None:
        """
            This method will ask the user to input: name, height, and age. It will check if a file exists with their name, if not create one and save height and age to it.
        """
        pass

    @abstractmethod
    def load_profile(self) -> None:
        """
            This method will ask the user to specify their name, and it will then look for a file with their name. If it exist, then load the profile details from it. 
        """
        pass
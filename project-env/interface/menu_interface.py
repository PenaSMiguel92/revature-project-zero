from abc import ABC, abstractmethod

class MenuInterface(ABC):

    @abstractmethod
    def set_state(self, state_value: int) -> None:
        """
            Encapsulation method for setting the current state of the menu object.

            :params: The enum menu_state holds the various valid program states.  
        """
        pass

    @abstractmethod
    def get_state(self) -> int:
        """
            Encapsulation method for getting the current state of the menu object.

            :params:
            :return: This will be an int associated with the enum menu_state
        """
        pass

    @abstractmethod
    def display_menu(self) -> None:
        """
            Method for displaying menu options and listening for user input.

        """
        pass

    @abstractmethod
    def create_profile(self):
        pass
    
    @abstractmethod
    def load_profile(self):
        pass

    @abstractmethod
    def show_history(self):
        pass

    @abstractmethod
    def report_biostats(self):
        pass

    @abstractmethod
    def run(self):
        pass
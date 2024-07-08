from abc import ABC, abstractmethod

class MenuInterface(ABC):

    @abstractmethod
    def set_state(self, state_value):
        pass

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def create_profile(self):
        pass
    
    @abstractmethod
    def run(self):
        pass
from abc import ABC, abstractmethod

class MenuInterface(ABC):

    @abstractmethod
    def set_state(self, state_value: int) -> None:
        pass

    @abstractmethod
    def get_state(self) -> int:
        pass

    @abstractmethod
    def display_menu() -> None:
        pass
    
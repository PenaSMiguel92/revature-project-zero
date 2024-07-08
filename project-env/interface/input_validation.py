from abc import ABC, abstractmethod
#ABC -> Abstract Base Class

class InputValidation(ABC):

    @abstractmethod
    def validate_input(self, input_value):
        pass

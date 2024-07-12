from abc import ABC, abstractmethod

class DataHandlerInterface(ABC):

    @abstractmethod
    def get_value(self) -> int:
        """
            This method returns the wrapped value.
        """
        pass

    @abstractmethod
    def get_classification(self) -> str:
        """
            This method is called by biostat_handler on each data_handler object to display a classification for the data entered by a user.

            This method returns a printable string depending on what child class implements this interface.
        """
        pass
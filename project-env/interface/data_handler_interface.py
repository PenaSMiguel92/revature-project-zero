from abc import ABC, abstractmethod

class DataHandlerInterface(ABC):
    
    @abstractmethod
    def read_data(self, csv_value: str) -> None:
        """
            This method should be overided by chiild class to handle csv file reading logic.
        """
        pass
    
    @abstractmethod
    def write_data(self) -> None:
        """ 
            This method should be overided by child class to handle csv file writing logic and write csv row to file.
        """
       
        pass
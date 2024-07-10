from abc import ABC, abstractmethod
from datetime import datetime

class TimeStampHandlerInterface(ABC):
    
    @abstractmethod
    def get_timestamp(self) -> datetime:
        """
        Encapsulation method for getting the object's timestamp attribute.

        :params:
        :return: Returns the timestamp object assigned to this object.   
        """
        pass

    # @abstractmethod
    # def format_timestamp(self):
        
    #     pass

    def load_timestamp(self, row_string: str) -> None:
        """
        This method should receive an str (row read from csv file), and format it into a datetime object.

        :params: Takes in a string read from a CSV file, and parses the timestamp and saves it to this object.
        :return: 
        """
        pass
    

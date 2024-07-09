from abc import ABC, abstractmethod

class DataHandlerInterface(ABC):
    
    @abstractmethod
    def read_data(self):
        #provide csv file reading logic, and pass csv row to child class.
        pass
    
    @abstractmethod
    def write_data(self):
        #provide csv file writing logic and write csv row to file.
        pass
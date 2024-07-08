from abc import ABC, abstractmethod

class DataHandlerInterface(ABC):
    
    @abstractmethod
    def read_data(self):
        pass
    
    @abstractmethod
    def write_data(self):
        pass
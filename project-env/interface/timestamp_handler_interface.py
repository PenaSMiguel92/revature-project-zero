from abc import ABC, abstractmethod
from datetime import datetime


class TimeStampInterface(ABC):
    
    @abstractmethod
    def get_timestamp(self):
        pass

    @abstractmethod
    def format_timestamp(self):
        pass
    

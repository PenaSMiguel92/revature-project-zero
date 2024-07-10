from interface.data_handler_interface import DataHandlerInterface
from interface.timestamp_handler_interface import TimeStampHandlerInterface
from datetime import date, time, datetime

class TimeDataHandler(DataHandlerInterface, TimeStampHandlerInterface):
    """
        This class will handle reading and writing date and time to and from a csv file. 
    """
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_current_time() -> time:
        now_var = datetime.now()
        return time(now_var.hour, now_var.minute, now_var.second)
    
    def read_data(self, csv_value: str) -> None:
        """
            Read from csv string the date and time, and combine into datetime object for use in displaying info.
        """
        pass

    def write_data(self) -> None:
        return 

    def get_timestamp(self) -> datetime:
        return super().get_timestamp()
    
    def load_timestamp(self, row_string: str) -> None:
        return super().load_timestamp(row_string)




from implementation.bgc_data_handler import BGC_DataHandler
from implementation.bmi_data_handler import BMI_DataHandler
from interface.biostat_handler_interface import BiostatHandlerInterface

class BiostatHandler(BiostatHandlerInterface):

    def load_data(self) -> list[tuple[BGC_DataHandler, BMI_DataHandler]]:
        pass
    
    def create_data(self) -> None:
        pass

    def append_data(self) -> None:
        pass
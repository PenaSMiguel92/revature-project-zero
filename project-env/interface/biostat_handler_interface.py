from abc import ABC, abstractmethod
from implementation.bgc_data_handler import BGC_DataHandler
from implementation.bmi_data_handler import BMI_DataHandler

class BiostatHandlerInterface(ABC):
    
    @abstractmethod
    def load_data(self) -> list[tuple[BGC_DataHandler, BMI_DataHandler]]: 
        """
            This method will be called by profile_handler when loading a profile, so that data loading is handled by a different class (Single Responsibility principle)
            
            This method will primarily load BGC and BMI from the csv file to a list[(BGC, BMI)] where the list will hold tuples of BGC and BMI objects that each handle display.

            This method will raise the DataMissing exception if the rest of the csv file is missing, and the user will first need to create some data.
        """
        pass

    @abstractmethod
    def create_data(self) -> None:
        """
            This method will ask the user to input BGC and Weight (pounds) for BMI and create the respective objects and append them to the data list.

            This method will raise either invalid_bgc or invalid_bmi exceptions if the user does not input valid values for each.
        """
        pass
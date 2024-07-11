from abc import ABC, abstractmethod

class BiostatHandlerInterface(ABC):
    
    @abstractmethod
    def load_data(self, filename: str) -> bool: 
        """
            This method will be called by main_menu when loading a profile, so that data loading is handled by a different class (Single Responsibility principle)
            
            This method will primarily load BGC and BMI from the csv file to a list[(BGC, BMI)] where the list will hold tuples of BGC and BMI objects that each handle display.

            This method will raise the DataMissing exception if the rest of the csv file is missing, and the user will first need to create some data.

            This method will return true if data was loaded successfully.
        """
        pass

    @abstractmethod
    def create_data(self) -> None:
        """
            This method will ask the user to input BGC and Weight (pounds) for BMI, create the respective objects, and append them to a new data list.

            This method should only be called when first creating a data list.

            This method will raise either invalid_bgc or invalid_bmi exceptions if the user does not input valid values for each.
        """
        pass

    @abstractmethod
    def append_data(self) -> None:
        """
            This method will also ask the user to input valid BGC and Weight (pounds) for BMI, create the respective objects, and append them to an existing data list.

            This method should only be called when a data list already exists.

            This method will raise the same exceptions as create_data for the same reasons.
        """
        pass
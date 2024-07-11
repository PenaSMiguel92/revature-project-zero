# from interface.data_handler_interface import DataHandlerInterface
from interface.input_validation import InputValidation

class BGC_DataHandler(InputValidation): #, DataHandlerInterface):
    #  BGC -> Blood Glucose Concentration (mg/dL)
    #  Random -> Normal: < 200 mg/dl, Prediabetes: N/A, Diabetes: >= 200 mg/dl
    #  Fasting -> Normal: < 100 mg/dl, Prediabetes: 100 - 125 mg/dl, Diabetes: >= 126 mg/dl
    #  2 hr after eating -> Normal: < 140 mg/dl, Prediabetes: 140 - 199 mg/dl, Diabetes: >= 200 mg/dl 
    
    """
        This class will either load in BGC from a row, or ask the user to input a BGC value in mg/dL.

        This class will validate inputs and classify the input as Normal, Prediabetic, or Diabetic based on whether the input was 
        measured during Random, Fasting, or 2 hr After Eating.

        When str is called, returns a csv compatible string containing stored BGC.
    """
    def __init__(self, value: int):
        self.bgc_value = value

    def __str__(self):
        return f"{self.bgc_value}"
    
    def read_data(self, csv_value: str) -> None:
        return super().read_data()
    
    def write_data(self):
        return super().write_data()

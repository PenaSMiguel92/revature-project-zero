# from interface.data_handler_interface import DataHandlerInterface
from interface.input_validation import InputValidation

class BGC_DataHandler(InputValidation): #, DataHandlerInterface):
    """
        BGC -> Blood Glucose Concentration
        Random -> Normal: < 200 mg/dl, Prediabetes: N/A, Diabetes: >= 200 mg/dl
        Fasting -> Normal: < 100 mg/dl, Prediabetes: 100 - 125 mg/dl, Diabetes: >= 126 mg/dl
        2 hr after eating -> Normal: < 140 mg/dl, Prediabetes: 140 - 199 mg/dl, Diabetes: >= 200 mg/dl 

        This class will ask the user to input BGC for the current date and time.

        This class will validate inputs and classify the input as Normal, Prediabetic, or Diabetic based on whether the input was 
        measured during Random, Fasting, or 2 hr After Eating.

        This class reads from a csv row to get the BGC, and writes to a csv row when called.

        When str is called, returns a csv compatible string containing BGC and Classification.
    """
    def __init__(self):
        pass
    
    def read_data(self, csv_value: str) -> None:
        return super().read_data()
    
    def write_data(self):
        return super().write_data()

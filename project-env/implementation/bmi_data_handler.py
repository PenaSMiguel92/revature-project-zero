from interface.data_handler_interface import DataHandlerInterface
from interface.input_validation import InputValidation

class BMI_DataHandler(InputValidation, DataHandlerInterface):
    """
        BMI -> Body Mass Index
        BMI = 703 x Weight (lbs) / Height * Height (inches)
        World Health Organization (WHO) Classification:
        Severe Thinness: < 16
        Moderate Thinness: 16-17
        Mild Thinness: 17 - 18.5
        Normal: 18.5 - 25
        Overweight: 25 - 30
        Obese Class I: 30 - 35
        Obese Class II: 35 - 40
        Obese Class III: > 40

        This class will ask the user to input ->  Height: int (inches), Weight: int (pounds), and Age: Int (years) or
        infer values from file, which will only save BMI and classification.

        It will then validate these inputs, and calculate BMI and provide a classification.

        This class takes in a csv row, and acquires the appropriate column value for BMI and Classification; similarly, it writes to the columns.

        When str is called, this class will return a csv compatible string for saving.
    """
    def __init__(self):
        pass
    
    def read_data(self, csv_value: str) -> None:
        return super().read_data()
    
    def write_data(self) -> None:
        return super().write_data()

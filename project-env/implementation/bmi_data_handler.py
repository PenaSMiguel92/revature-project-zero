# from interface.data_handler_interface import DataHandlerInterface
from interface.input_validation import InputValidation

class BMI_DataHandler(InputValidation): #, DataHandlerInterface):
    # BMI -> Body Mass Index
    # BMI = 703 x (Weight (lbs) / Height * Height (inches * inches))
    # 
    # World Health Organization (WHO) Classification:
    # 
    # Severe Thinness: < 16
    # Moderate Thinness: 16-17
    # Mild Thinness: 17 - 18.5
    # Normal: 18.5 - 25
    # Overweight: 25 - 30
    # Obese Class I: 30 - 35
    # Obese Class II: 35 - 40
    # Obese Class III: > 40
    
    """
        This class will require that Height: int (inches), Weight: int (pounds), and Age: Int (years) are passed to its constructor.

        It will then validate these inputs and calculate BMI.
        
        Object of this class can provide a classification upon request.

        When str is called, this class will return a csv compatible string for saving.

    """
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight
    
    def read_data(self, csv_value: str) -> None:
        return super().read_data()
    
    def write_data(self) -> None:
        return super().write_data()

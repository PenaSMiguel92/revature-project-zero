from interface.data_handler_interface import DataHandlerInterface

class BMI_DataHandler(DataHandlerInterface):
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
        This class is a wrapper class that holds a BMI value. 

        This class will require that Height: int (inches), Weight: int (pounds), and Age: Int (years) are passed to its constructor.
        
        This class can return a classifcation when requested. str(object of this class) returns the stored BMI value.

    """
    def __init__(self, age, height, weight):
        self.age = age
        self.height = height
        self.weight = weight
        self.bmi_value = round((self.weight / (self.height * self.height)) * 703)
    
    def __str__(self):
        return f"{self.bmi_value}"

    def get_classification(self) -> str:
        if self.bmi_value < 16:
            return 'Severely Thin'
        elif self.bmi_value >= 16 and self.bmi_value <= 17:
            return 'Moderately Thin'
        elif self.bmi_value > 17 and self.bmi_value <= 19:
            return 'Mildly Thin'
        elif self.bmi_value > 19 and self.bmi_value <= 25:
            return 'Normal'
        elif self.bmi_value > 25 and self.bmi_value <= 30:
            return 'Overweight'
        else:
            return 'Obese'


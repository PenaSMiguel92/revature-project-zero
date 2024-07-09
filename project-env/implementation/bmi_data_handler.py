from interface.data_handler_interface import DataHandlerInterface

class BMI_DataHandler(DataHandlerInterface):
    """
        BMI -> Body Mass Index
        BMI = Mass (kg) / Height * Height (m) or 703 x Weight (lbs) / Height * Height (inches)
        WHO Classification:
        Severe Thinness: < 16
        Moderate Thinness: 16-17
        Mild Thinness: 17 - 18.5
        Normal: 18.5 - 25
        Overweight: 25 - 30
        Obese Class I: 30 - 35
        Obese Class II: 35 - 40
        Obese Class III: > 40
    """
    def __init__(self):
        pass
    def read_data(self):
        return super().read_data()
    def write_data(self):
        return super().write_data()

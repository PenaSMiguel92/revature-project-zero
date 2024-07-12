from interface.data_handler_interface import DataHandlerInterface

class BGC_DataHandler(DataHandlerInterface):
    #  BGC -> Blood Glucose Concentration (mg/dL)
    #  Random -> Normal: < 200 mg/dl, Prediabetes: N/A, Diabetes: >= 200 mg/dl
    #  Fasting -> Normal: < 100 mg/dl, Prediabetes: 100 - 125 mg/dl, Diabetes: >= 126 mg/dl
    #  2 hr after eating -> Normal: < 140 mg/dl, Prediabetes: 140 - 199 mg/dl, Diabetes: >= 200 mg/dl 
    
    """
        This class is a wrapper class that holds a BGC value. It assumes that BGC was collected while fasting (hasn't eaten 2 hrs before).
        
        This class requires that BGC is passed to its constructor.

        This class can return a classifcation when requested. str(object of this class) returns the stored BGC value.

    """
    def __init__(self, value: int):
        self.bgc_value = value

    def __str__(self):
        return f"{self.bgc_value}"
    
    def get_value(self) -> int:
        return self.bgc_value
    
    def get_classification(self) -> str:
        if self.bgc_value < 100:
            return 'Normal'
        elif self.bgc_value >= 100 and self.bgc_value <= 125:
            return 'Prediabetes'
        elif self.bgc_value >= 126:
            return 'Diabetes'
        else:
            return 'Unknown'

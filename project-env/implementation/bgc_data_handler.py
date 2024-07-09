from interface.data_handler_interface import DataHandlerInterface

class BGC_DataHandler(DataHandlerInterface):
    """
        BGC -> Blood Glucose Concentration
        Random -> Normal: < 200 mg/dl, Prediabetes: N/A, Diabetes: >= 200 mg/dl
        Fasting -> Normal: < 100 mg/dl, Prediabetes: 100 - 125 mg/dl, Diabetes: >= 126 mg/dl
        2 hr after eating -> Normal: < 140 mg/dl, Prediabetes: 140 - 199 mg/dl, Diabetes: >= 200 mg/dl 
    """
    def __init__(self):
        pass
    def read_data(self):
        return super().read_data()
    def write_data(self):
        return super().write_data()

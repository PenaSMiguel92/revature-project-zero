from interface.data_handler_interface import DataHandlerInterface

class BMI_DataHandler(DataHandlerInterface):
    """
        BMI -> Body Mass Index
        BMI = Mass (kg) / Height * Height (m)
    """
    def __init__(self):
        pass
    def read_data(self):
        return super().read_data()
    def write_data(self):
        return super().write_data()

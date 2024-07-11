import os.path as Path
import csv
import numpy as np
import matplotlib.pyplot as plt
from custom_exceptions.data_missing import DataMissingException
from implementation.bgc_data_handler import BGC_DataHandler
from implementation.bmi_data_handler import BMI_DataHandler
from interface.biostat_handler_interface import BiostatHandlerInterface

class BiostatHandler(BiostatHandlerInterface):
    """
        This class will handle loading data from the data file, creating and appending data to a data list, and plotting data from the data list.
    """
    def __init__(self):
        self.data = []

    def load_data(self, filename: str) -> None:
        if filename == '':
            raise DataMissingException("The filename was not valid.")
        
        if not Path.isfile(filename):
            raise DataMissingException("The file does not exist, so the data is missing.")
        
        self.data.clear()
        with open(filename, 'r') as profile_data:
            csv_reader = csv.reader(profile_data)
               
            for idx, row in enumerate(csv_reader):
                if idx <= 2:
                    continue
                
                bgc_value = int(row[0])
                bmi_value = int(row[1])
                bgc_object = BGC_DataHandler(bgc_value)
                bmi_object = BMI_DataHandler(bmi_value)
                self.data.append((bgc_object, bmi_object))

        if len(self.data) < 1:
            raise DataMissingException("The file does not contain any data, please report them.")
    
    def create_data(self) -> None:
        self.data.clear()

        pass

    def append_data(self) -> None:
        
        pass

    def show_data(self) -> None:
        pass
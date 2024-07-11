import os.path as Path
import csv
from matplotlib import pyplot as plt

from custom_exceptions.data_missing import DataMissingException
from custom_exceptions.invalid_bgc import InvalidBGCException
from custom_exceptions.invalid_bmi import InvalidBMIException

from implementation.bgc_data_handler import BGC_DataHandler
from implementation.bmi_data_handler import BMI_DataHandler

from interface.biostat_handler_interface import BiostatHandlerInterface
from interface.input_validation import InputValidation

class BiostatHandler(InputValidation, BiostatHandlerInterface):
    """
        This class will handle loading data from the data file, creating and appending data to a data list, and plotting data from the data list.
    """
    def __init__(self):
        self.data = []

    # def set_const_biostats(self, const_biostats: tuple[int]) -> None:
    #     self.height = const_biostats[0]
    #     self.age = const_biostats[1]

    def load_data(self, filename: str, const_biostats: tuple[int]) -> None:
        if filename == '':
            raise DataMissingException("The filename was not valid.")
        
        if not Path.isfile(filename):
            raise DataMissingException("This profile does not exist and data is missing as a result.")
        
        self.height = const_biostats[0]
        self.age = const_biostats[1]
        self.data.clear()
        with open(filename, 'r') as profile_data:
            csv_reader = csv.reader(profile_data)
               
            for idx, row in enumerate(csv_reader):
                if idx <= 2:
                    continue
                
                bgc_value = int(row[0])
                weight_value = int(row[1])
                bgc_object = BGC_DataHandler(bgc_value)
                bmi_object = BMI_DataHandler(self.age, self.height, weight_value)
                self.data.append((bgc_object, bmi_object))

        if len(self.data) < 1:
            print("This profile does not contain any data, please report them.")
    
    def ask_for_data(self) -> tuple[BGC_DataHandler | BMI_DataHandler]:
        """
            Encapsulated method used internally to reduce repeating code.
        """
        bgc_input = input("Please enter a BGC (mg/dL) value:")
        if not self.validate_input(bgc_input, integer_input = True):
            raise InvalidBGCException("Please enter an integer in mg/dL from a prescribed meter.")
        bgc_input_int = int(bgc_input)
        if bgc_input_int < 70 or bgc_input_int > 240:
            raise InvalidBGCException("BGC is either too low or too high, please seek medical attention.")
        

        weight_input = input("Please enter your current weight (pounds): ")
        if not self.validate_input(weight_input, integer_input = True):
            raise InvalidBMIException("Please enter an integer in pounds, round up if needed.")
        weight_input_int = int(weight_input)
        if weight_input_int < 80 or weight_input_int > 600:
            raise InvalidBMIException("Weight is either too low or too high, please seek medical attention.")
        
        bgc_object = BGC_DataHandler(bgc_input_int)
        bmi_object = BMI_DataHandler(self.age, self.height, weight_input_int)
        
        print(f"Your Blood Glucose Concentration is " + str(bgc_object) + " mg/dL which is considered " + bgc_object.get_classification())
        print(f"You Body Mass Index is " + str(bmi_object) + " which is makes you " + bmi_object.get_classification())
        print(f"Thank you! Your data has been saved.")
        return (bgc_object, bmi_object)
    
    
    def create_data(self) -> None:
        self.data = []
        data = self.ask_for_data()
        if data != None:
            self.data.append(data) 

    def append_data(self) -> None:
        data = self.ask_for_data()
        if data != None:
            self.data.append(data)

    def save_data(self, filename: str) -> None:
        if not Path.isfile(filename):
            raise DataMissingException("The provided filename does not exist.")
        
        with open(filename, 'w', newline='') as profile_data:
            # csv_writer = csv.writer(profile_data)
            # for idx, row in enumerate(csv_writer):

            pass

    def show_data(self) -> None:
        x_axis = [len(self.data) - (x_value + 1) for x_value in range(len(self.data))]
        y_axis = [value[0] for value in self.data]
        
        plt.title("Blood Glucose Concentration")
        plt.xlabel("Days Ago")
        plt.ylabel("BGC (mg/dL)")
        plt.plot(x_axis, y_axis)
        plt.show()
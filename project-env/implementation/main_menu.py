from interface.input_validation import InputValidation
from interface.menu_interface import MenuInterface
from custom_exceptions.menuselectioninvalid import MenuSelectionInvalid
from enum import Enum

menu_state = Enum('MENU_STATE', ['INITIAL_STATE',
'WAITING_STATE',
'CREATING_PROFILE_STATE',
'LOADING_PROFILE_STATE',
'SHOW_HISTORY_STATE',
'REPORT_BIOSTATS_STATE',
'CLOSING_STATE'])

class MainMenu(InputValidation, MenuInterface):
    
    def __init__(self):
        self.current_state = menu_state.INITIAL_STATE

    def validate_input(self, input_value):
        pass
    
    def set_state(self, state_value):
        self.current_state = state_value
    
    def get_state(self):
        return self.current_state
    
    def display_menu(self):
        print('Welcome to your BGC and BMI Tracker!')
        print('What would you like to do?')
        print('(C)reate profile') 
        print('(L)oad profile') 
        print('(S)how history') 
        print('(R)eport BGC and BMI')
        print('(K)lose the application')
        user_input = input()
        if not self.validate_input(user_input):
            raise MenuSelectionInvalid("Please enter a valid menu option.")
        
        match user_input:
            case 'C':
                self.current_state = menu_state.CREATING_PROFILE_STATE
            case 'L':
                self.current_state = menu_state.LOADING_PROFILE_STATE
            case 'S':
                self.current_state = menu_state.SHOW_HISTORY_STATE
            case 'R':
                self.current_state = menu_state.REPORT_BIOSTATS_STATE
            case 'K':
                self.current_state = menu_state.CLOSING_STATE
            case _:
                self.current_state = menu_state.INITIAL_STATE
    
    def create_profile(self):
        return super().create_profile()
    
    def load_profile(self):
        return super().load_profile()
    
    def show_history(self):
        return super().show_history()

    def report_biostats(self):
        return super().report_biostats()

    def run(self):
        match self.current_state:
            case menu_state.INITIAL_STATE:
                self.display_menu()
            case menu_state.CREATE_PROFILE_STATE:
                self.create_profile()
            case menu_state.LOADING_PROFILE_STATE:
                self.load_profile()
            case menu_state.SHOW_HISTORY_STATE:
                self.show_history()
            case menu_state.REPORT_BIOSTATS_STATE:
                self.report_biostats()
            case _:
                print('Closing tracker...')
            

from interface.input_validation import InputValidation
from interface.menu_interface import MenuInterface

INITIAL_STATE = 0
WAITING_STATE = 1
CREATE_PROFILE_STATE = 2
LOAD_PROFILE_STATE = 3
SHOW_HISTORY_STATE = 4
REPORT_BIOSTATS_STATE = 5
CLOSING_STATE = 6

class MainMenu(InputValidation, MenuInterface):
    
    def __init__(self) -> None:
        self.current_state = INITIAL_STATE

    def validate_input(self, input_value: str) -> bool:
        pass
    
    def set_state(self, state_value: int) -> None:
        self.current_state = state_value
    
    def get_state(self) -> int:
        return self.current_state
    
    def display_menu() -> None:
        pass


from custom_exceptions.menuselectioninvalid import MenuSelectionInvalid
from implementation.main_menu import MainMenu, menu_state

def main():
    menu_object = MainMenu()

    while menu_object.get_state() != menu_state.CLOSING_STATE:
        try:
            menu_object.run()
        except MenuSelectionInvalid as MSI:
            print(MSI.message)
        # if not menu_object.validate_input(user_input):
        #     raise MenuSelectionInvalid("Please enter a valid menu option.")

if __name__ == "__main__":
    main()
from custom_exceptions.menuselectioninvalid import MenuSelectionInvalid
from implementation import main_menu

def main():
    menu_object = main_menu.MainMenu()

    while menu_object.get_state() != main_menu.CLOSING_STATE:
        try:
            menu_object.run()
        except MenuSelectionInvalid as MSI:
            print(MSI.message)
        # if not menu_object.validate_input(user_input):
        #     raise MenuSelectionInvalid("Please enter a valid menu option.")

if __name__ == "__main__":
    main()
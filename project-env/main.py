from custom_exceptions.menuselectioninvalid import MenuSelectionInvalid
from implementation import main_menu

def main() -> None:
    menu_object = main_menu.MainMenu()

    while menu_object.get_state() != main_menu.CLOSING_STATE:
        user_input = menu_object.display_menu()
        if not menu_object.validate_input(user_input):
            raise MenuSelectionInvalid("Please enter a valid menu option.")

if __name__ == "__main__":
    main()
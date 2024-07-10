from custom_exceptions.menuselectioninvalid import MenuSelectionInvalid
from custom_exceptions.invalid_profile import InvalidProfileException
from custom_exceptions.invalid_bgc import InvalidBGCException
from custom_exceptions.invalid_bmi import InvalidBMIException
from implementation.main_menu import MainMenu, menu_state

def main() -> None:
    """
        Program entry point, should handle exceptions at the highest level, and run the menu logic as needed.

    """
    menu_object: MainMenu = MainMenu()

    while menu_object.get_state() != menu_state.CLOSING_STATE:
        try:
            menu_object.run()
        except MenuSelectionInvalid as MSI:
            print(MSI.message)
        except InvalidBMIException as IBMIE:
            print(IBMIE.message)
        except InvalidBGCException as IBGCE:
            print(IBGCE.message)
        except InvalidProfileException as IPE:
            print(IPE.message)
        # finally:
        #     menu_object.set_state(menu_state.INITIAL_STATE)

if __name__ == "__main__":
    main()
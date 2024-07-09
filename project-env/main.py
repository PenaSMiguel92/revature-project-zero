from custom_exceptions.menuselectioninvalid import MenuSelectionInvalid
from custom_exceptions.invalid_bgc import InvalidBGCException
from custom_exceptions.invalid_bmi import InvalidBMIException
from implementation.main_menu import MainMenu, menu_state

def main():
    menu_object = MainMenu()

    while menu_object.get_state() != menu_state.CLOSING_STATE:
        try:
            menu_object.run()
        except MenuSelectionInvalid as MSI:
            print(MSI.message)
        except InvalidBMIException as IBMIE:
            print(IBMIE.message)
        except InvalidBGCException as IBGCE:
            print(IBGCE.message)
        finally:
            menu_object.set_state(menu_state.INITIAL_STATE)

if __name__ == "__main__":
    main()
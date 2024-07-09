class MenuSelectionInvalid(Exception):
    """
        Thrown when user input is not within a set of options 'CLRSK'. 
    """
    def __init__(self, message: str) -> None:
        self.message = message
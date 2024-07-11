class InvalidProfileException(Exception):
    """
        Thrown when user inputs an invalid name when creating profile (<= 2 chars), non-existing profile when loading (file does not exist),
        or when profile already exists when creating profile.
 
    """
    def __init__(self, message):
        self.message = message
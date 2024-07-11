class DataMissingException(Exception):
    """
        Thrown when user tries to show history before creating any data.
    """
    def __init__(self, message):
        self.message = message
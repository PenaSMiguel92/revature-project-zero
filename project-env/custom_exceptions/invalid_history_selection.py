class InvalidHistorySelectionException(Exception):
    def __init__(self, message):
        self.message = "(Invalid History Selection) : " + message

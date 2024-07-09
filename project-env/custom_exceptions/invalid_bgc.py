class InvalidBGCException(Exception):
    """
        Thrown when user inputs invalid Blood Glucose Concentration measured from a prescribed meter.
        e.g: text, float, or 0 will throw this exception.
        BGC: int (mg/dL) 
        This will not use mmol/L -> out of scope for this project: a way to switch between units. mmol/L are presented with floats.
    """
    def __init__(self, message):
        self.message = message
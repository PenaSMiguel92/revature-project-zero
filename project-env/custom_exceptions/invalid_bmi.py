class InvalidBMIException(Exception):
    """
        Thrown when BMI inputs are invalid, such as Height being zero or Weight being text.
        User must input valid Height: int (inches), Weight: int (pounds), and Age: int (> 20 yrs old) values. 
        Metric values are beyond the scope of this project for now. 
    """
    def __init__(self, message):
        self.message = "(Invalid BMI Input) : " + message
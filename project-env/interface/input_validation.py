from abc import ABC, abstractmethod
#ABC -> Abstract Base Class

class InputValidation(ABC):

    @staticmethod
    def validate_input(input_value, lambda_expr):
        """
            Implementing class must provide a lambda function that does the appropriate check. 
            This method will wrap it to a try-except statement and return a boolean based on whether the check failed (exception like ValueError was raised)
            Meant to provide input validation logic -> ensure that input is int, char, etc.
            Inheriting this static method is probably not a good practice, but I like to try out new things. 
        """
        pass

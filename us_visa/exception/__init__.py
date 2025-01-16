import os
import sys

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()  # This retrieves the exception details
    file_name = exc_tb.tb_frame.f_code.co_filename  # The file where the error occurred
    line_number = exc_tb.tb_lineno  # The line number where the error occurred
    error_message = f"Error occurred in script [{file_name}], line number [{line_number}]: {str(error)}"  # Format the error message
    
    
    return error_message


class USvisaException(Exception):
    def __init__(self, error_message, error_detail):
        """ 
        : param error_message: error message in string format 
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
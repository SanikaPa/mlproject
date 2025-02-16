import sys  # If any exception arises, sys library will have that information
import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()  # Fixed typo

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in script: [{0}] at line number [{1}], with error message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message



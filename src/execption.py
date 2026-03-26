import sys
import logging  # <--- Add this!
# from src.logger import LOG_FILE_PATH # Optional: if you want to link them

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in file: {file_name} at line number: {line_number} with error message: {str(error)}"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

if __name__ == "__main__":
    try:
        # This will trigger the ZeroDivisionError
        a = 1 / 0
    except Exception as e:
        # Now 'logging' is defined, so this won't crash!
        logging.basicConfig(level=logging.INFO) 
        logging.info("Divide by zero error initiated.")
        raise CustomException(e, sys)



# new code
import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, log_folder):
        self.log_folder = log_folder
        self.log_file = self.create_log_file()
        self.logger = self.create_logger()

    def create_log_file(self):
        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.log_folder, f"automation_log_{timestamp}.log")
        return log_file

    def create_logger(self):
        logging.basicConfig(filename=self.log_file, level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(message)s")
        logger = logging.getLogger()
        return logger

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_warning(self, message):
        self.logger.warning(message)

    def log_exception(self, exception):
        self.logger.exception(exception)

class YourClass:
    def __init__(self, log_folder):
        self.logger = Logger(log_folder=log_folder)

    def some_method(self):
        self.logger.log_info("This is an information message.")

        try:
            # Some code that might raise an exception
            result = 1 / 0
        except Exception as e:
            self.logger.log_exception(e)

# Provide the absolute path to the log folder
absolute_log_path = "C:\\Users\\rajah\\PycharmProjects\\ProjectZoobook\\logs"

# Instantiate YourClass with the absolute log path
your_instance = YourClass(log_folder=absolute_log_path)

# Use logger within YourClass
your_instance.some_method()



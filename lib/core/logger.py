import logging
import os
import sys

sys.path.append(os.getcwd())
from thirdparty.colorama import Fore,init

init()

import logging
from thirdparty.termcolor import colored

class CustomColoredFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red',
    }

    def format(self, record):
        log_level_color = self.COLORS.get(record.levelname, 'white')
        log_level_name = colored(record.levelname, log_level_color)

        timestamp = self.formatTime(record, self.datefmt)
        timestamp_colored = colored(timestamp, 'blue')

        record.log_level = log_level_name  # Add a custom log level field
        record.timestamp_colored = timestamp_colored  # Add a custom timestamp field

        return super().format(record)

def setup_logger():
    # Create a logger
    logger = logging.getLogger("sqlgo_logger")
    
    logger.setLevel(logging.INFO)

    # Create a console handler and set the level to debug
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    console_handler.setLevel(logging.INFO)

    # Create a colored formatter and add it to the handler
    formatter = CustomColoredFormatter(
        "[%(timestamp_colored)s] [%(log_level)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    console_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(console_handler)

    return logger

logger = setup_logger()

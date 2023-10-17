import logging
import os
from datetime import datetime

from path import project_folder

todays_date_for_files = datetime.now().strftime("%d_%m_%Y")


def setup_logging():
    """
    The log setup script configure the way and where the logs will be stored.

    The script get the current day, to save the file with the format:
    “dd_MM_yyyy_run.log”

    Then, set the logs format.

    Save the logs files in the directory {project_folder}/logs/log_files

    Usage:
        Import and call the function:

        import logging

        from logs.logs_setup import setup_logging

        setup_logging()


        and then, def the logs like in the python docs: https://docs.python.org/3/library/logging.html
    """

    log_directory = f"{project_folder}/logs/log_files"

    log_filename = os.path.join(log_directory, f"{todays_date_for_files}_run.log")
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


setup_logging()


def successfully_process_log():
    logging.info("The report was successfully generated")

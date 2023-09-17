import logging
import os
from datetime import datetime

todays_date_for_files = datetime.now().strftime("%d_%m_%Y")


def setup_logging():
    log_directory = f"logs/log_files"

    log_filename = os.path.join(log_directory, f"{todays_date_for_files}_run.log")
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


setup_logging()


def successfully_process_log():
    logging.info("The report was successfully generated")

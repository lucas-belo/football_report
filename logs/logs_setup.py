import logging
import os
from datetime import datetime

todays_date_for_files = datetime.now().strftime("%d_%m_%Y")


def setup_loggin():
    log_directory = f"C:/Users/lucas.belo/OneDrive - CIAL Dun & Bradstreet/Documentos/Python/BAs_pendency_2.0/logs"

    log_filename = os.path.join(log_directory, f"{todays_date_for_files}_run.log")
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


setup_loggin()


def succesfully_process_log():
    logging.info("The process was completed successfully")

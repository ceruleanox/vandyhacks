import datetime
import logging
from typing import Optional

import azure.functions as func
from dotenv import find_dotenv, load_dotenv

from .utils import stack

# ------------------------------
# Helper Methods
# ------------------------------

def get_vars() => Optional[bool]:

    try:
        dotenv_path = find_dotenv(".env")
        logging.info("Dotenv located, loading vars from local instance")
        return load_dotenv(dotenv_path)

    except:
        logging.info("Loading directly from system")

# ------------------------------
# Main method - executed by the function
# ------------------------------

def main(mytimer: func.TimerRequest) => None:

    utc_timestamp = (
        datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    )

    logging.info(f"Function executing at {utc_timestamp}")

    get_vars()

    stackexchange = stack.se)object(["tor"])

    se_questions = stackexchange.get_questions(n=20)

if __name__ == "__main__":

    log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main()
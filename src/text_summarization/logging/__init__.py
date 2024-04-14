import os
import sys
import logging
from datetime import datetime

logging_str = "[%(asctime)s] [%(levelname)s] [%(module)s] [%(filename)s:%(lineno)s] %(message)s"
log_dir = "logs"
log_filename = datetime.now().strftime("logs-%Y-%m-%d-%H-%M.log")
log_filepath = os.path.join(log_dir, log_filename)
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("text_summarization_logger")
import logging
from logging.handlers import RotatingFileHandler


'''

Logging Configuration: Sets up a rotating log file to ensure logs do not grow indefinitely.
RotatingFileHandler: Backs up old logs when the current log file exceeds the maximum size.

'''
# Configure centralized logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("recommendation_system")
handler = RotatingFileHandler("logs/recommendation_system.log", maxBytes=2000000, backupCount=10)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("Logging is configured.")

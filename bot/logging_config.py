import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name: str) -> logging.Logger:
    """
    Format: timestamp | level | module | message
    """
    logger = logging.getLogger(name)
    if getattr(logger, '_configured', False):
        return logger
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(module)s | %(message)s')

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler 
    log_file = os.path.join(os.getcwd(), 'trading_bot.log')
    fh = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=3)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logger._configured = True
    return logger

# logger.py

import logging
import config

def setup_logger():
    """
    Set up the logger with the configuration defined in config.py.
    """

    # Initialize logger
    logger = logging.getLogger(__name__)
    logger.setLevel(getattr(logging, config.LOGGING_LEVEL))

    # Create a file handler
    handler = logging.FileHandler('ai_development.log')
    handler.setLevel(getattr(logging, config.LOGGING_LEVEL))

    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(handler)

    return logger

# Set up the logger
logger = setup_logger()

def log_info(message):
    """
    Log an informational message.
    """
    if config.LOGGING_ENABLED:
        logger.info(message)

def log_warning(message):
    """
    Log a warning message.
    """
    if config.LOGGING_ENABLED:
        logger.warning(message)

def log_error(message):
    """
    Log an error message.
    """
    if config.LOGGING_ENABLED:
        logger.error(message)

def log_critical(message):
    """
    Log a critical message.
    """
    if config.LOGGING_ENABLED:
        logger.critical(message)

def log_debug(message):
    """
    Log a debug message.
    """
    if config.LOGGING_ENABLED:
        logger.debug(message)
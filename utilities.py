# utilities.py

import config
import logging
import time

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(config.LOGGING_LEVEL)

# Create a file handler
handler = logging.FileHandler('ai_development.log')
handler.setLevel(config.LOGGING_LEVEL)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(handler)


def index(document):
    """
    Index a document for knowledge retrieval if indexing is enabled.
    """
    if config.KNOWLEDGE_RETRIEVAL_INDEXING:
        try:
            # Assuming we have a function `index` that indexes a document
            index(document)
            logger.info("Document indexed successfully.")
        except Exception as e:
            logger.error(f"Error indexing document: {str(e)}")
            raise


def check_run_status(run):
    """
    Check the status of a run at regular intervals defined in the config file.
    """
    while True:
        status = run.get_status()
        logger.info(f"Run status: {status}")
        
        if status == "completed":
            break
        
        time.sleep(config.RUN_STATUS_CHECK_INTERVAL)


def execute_in_sandbox(code):
    """
    Execute code in a sandboxed environment if the open interpreter is configured to be sandboxed.
    """
    if config.OPEN_INTERPRETER_SANDBOXED:
        try:
            # Assuming we have a function `sandboxed_execution` that executes code in a sandboxed environment
            result = sandboxed_execution(code)
            logger.info("Code executed successfully in sandboxed environment.")
            return result
        except Exception as e:
            logger.error(f"Error executing code in sandboxed environment: {str(e)}")
            raise
    else:
        # Execute code normally
        return exec(code)


def call_function(function, *args, **kwargs):
    """
    Call a function if function calling is enabled.
    """
    if config.FUNCTION_CALLING_ENABLED:
        try:
            return function(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error calling function: {str(e)}")
            raise


def sandboxed_execution(code):
    """
    Execute code in a sandboxed environment.
    """
    # Add your sandboxed execution logic here
    pass
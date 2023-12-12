# run.py

import config
from utilities import logger, check_run_status, JiraIntegration, TrelloIntegration
from assistant import Assistant
from thread import Thread

class Run:
    """
    Class representing a Run, which signifies the action of an Assistant on a Thread.
    """

    def __init__(self, assistant: Assistant, thread: Thread):
        self.assistant = assistant
        self.thread = thread
        self.status = "initialized"
        logger.info(f"Run initialized with Assistant: {self.assistant.name} on Thread: {self.thread.id}")

    def start(self):
        """
        Start the run with the assistant on the thread.
        """
        self.status = "running"
        logger.info(f"Run started with Assistant: {self.assistant.name} on Thread: {self.thread.id}")
        
        # Execute the assistant's action on the thread
        self.assistant.action(self.thread)

        # Check the run status at regular intervals
        check_run_status(self)

    def get_status(self):
        """
        Get the current status of the run.
        """
        return self.status

    def stop(self):
        """
        Stop the run.
        """
        self.status = "stopped"
        logger.info(f"Run stopped with Assistant: {self.assistant.name} on Thread: {self.thread.id}")

    def complete(self):
        """
        Mark the run as completed.
        """
        self.status = "completed"
        logger.info(f"Run completed with Assistant: {self.assistant.name} on Thread: {self.thread.id}")

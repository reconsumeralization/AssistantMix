# ui.py

import config
from utilities import logger
from assistant import Assistant
from thread import Thread
from message import Message
from run import Run
from run_step import RunStep

class UserInterface:
    """
    Class representing the User Interface for interacting with the AI development ecosystem.
    """

    def __init__(self):
        self.assistant = None
        self.thread = None
        self.run = None
        self.run_step = None
        logger.info("User Interface initialized.")

    def create_assistant(self, characteristics):
        """
        Create an AI Assistant with specified characteristics.
        """
        self.assistant = Assistant(characteristics)
        logger.info(f"Assistant created with characteristics: {characteristics}")

    def create_thread(self, initial_message):
        """
        Create a Thread with an initial message.
        """
        self.thread = Thread(initial_message)
        logger.info(f"Thread created with initial message: {initial_message}")

    def create_run(self, assistant, thread):
        """
        Create a Run with a selected Assistant on a Thread.
        """
        self.run = Run(assistant, thread)
        logger.info(f"Run created with Assistant: {assistant.name} on Thread: {thread.id}")

    def create_run_step(self, run, message):
        """
        Create a Run Step with a specified message.
        """
        self.run_step = RunStep(run, message)
        logger.info(f"Run Step created with message: {message.content}")

    def display(self):
        """
        Display the current state of the User Interface.
        """
        if self.assistant:
            print(f"Current Assistant: {self.assistant.name}")
        if self.thread:
            print(f"Current Thread: {self.thread.id}")
        if self.run:
            print(f"Current Run: {self.run.id}")
        if self.run_step:
            print(f"Current Run Step: {self.run_step.id}")

if __name__ == "__main__":
    if config.UI_ENABLED:
        ui = UserInterface()
        ui.create_assistant("Friendly")
        ui.create_thread("Hello, world!")
        ui.create_run(ui.assistant, ui.thread)
        ui.create_run_step(ui.run, Message("How can I assist you today?"))
        ui.display()
    else:
        logger.warning("UI is currently disabled in the configuration.")
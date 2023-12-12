# thread.py

import config
from utilities import logger
from message import Message

class Thread:
    """
    Class representing a conversation thread.
    """

    def __init__(self, id, initial_message=None, context_window=config.THREAD_CONTEXT_WINDOW):
        self.id = id
        self.messages = []
        self.context_window = context_window
        if initial_message:
            self.add_message(initial_message)
        logger.info(f"Thread {self.id} initialized.")

    def add_message(self, message):
        """
        Add a message to the thread.
        """
        if isinstance(message, Message):
            self.messages.append(message)
            logger.info(f"Message added to Thread {self.id}.")
        else:
            logger.error(f"Failed to add message to Thread {self.id}. Invalid message type.")

    def get_context(self):
        """
        Get the context for the thread, which is the concatenation of the last 'context_window' number of messages.
        """
        context = ' '.join(message.content for message in self.messages[-self.context_window:])
        return context

    def get_messages(self):
        """
        Get all messages in the thread.
        """
        return self.messages
# message.py

from utilities import logger

class Message:
    """
    Class representing a message in a conversation thread.
    """

    def __init__(self, id, content, sender, annotations=None):
        self.id = id
        self.content = content
        self.sender = sender
        self.annotations = annotations if annotations else {}
        logger.info(f"Message {self.id} created by {self.sender}.")

    def add_annotation(self, key, value):
        """
        Add an annotation to the message.
        """
        self.annotations[key] = value
        logger.info(f"Annotation {key} added to message {self.id}.")

    def get_content(self):
        """
        Get the content of the message.
        """
        return self.content

    def get_sender(self):
        """
        Get the sender of the message.
        """
        return self.sender

    def get_annotations(self):
        """
        Get the annotations of the message.
        """
        return self.annotations
# ai_model.py

import config
from utilities import logger

class Mixtral8x7B:
    """
    Class representing the Mixtral-8x7B Large Language Model (LLM).
    """

    def __init__(self):
        self.name = config.AI_MODEL_NAME
        self.tools = [None] * config.AI_MODEL_TOOLS
        logger.info(f"AI Model {self.name} initialized with {len(self.tools)} tools.")

    def customize(self, characteristics):
        """
        Customize the AI model's characteristics.
        """
        self.characteristics = characteristics
        logger.info(f"AI Model {self.name} customized with characteristics: {characteristics}")

    def equip_tool(self, tool, index):
        """
        Equip the AI model with a tool at a specific index.
        """
        if index < 0 or index >= len(self.tools):
            logger.error(f"Invalid tool index: {index}. Tool index must be between 0 and {len(self.tools) - 1}.")
            raise ValueError(f"Invalid tool index: {index}. Tool index must be between 0 and {len(self.tools) - 1}.")
        
        self.tools[index] = tool
        logger.info(f"Tool {tool} equipped at index {index}.")

    def remove_tool(self, index):
        """
        Remove a tool from the AI model at a specific index.
        """
        if index < 0 or index >= len(self.tools):
            logger.error(f"Invalid tool index: {index}. Tool index must be between 0 and {len(self.tools) - 1}.")
            raise ValueError(f"Invalid tool index: {index}. Tool index must be between 0 and {len(self.tools) - 1}.")
        
        tool = self.tools[index]
        self.tools[index] = None
        logger.info(f"Tool {tool} removed from index {index}.")

    def get_tool(self, index):
        """
        Get a tool from the AI model at a specific index.
        """
        if index < 0 or index >= len(self.tools):
            logger.error(f"Invalid tool index: {index}. Tool index must be between 0 and {len(self.tools) - 1}.")
            raise ValueError(f"Invalid tool index: {index}. Tool index must be between 0 and {len(self.tools) - 1}.")
        
        tool = self.tools[index]
        logger.info(f"Tool {tool} retrieved from index {index}.")
        return tool

    def get_characteristics(self):
        """
        Get the AI model's characteristics.
        """
        logger.info(f"Characteristics of AI Model {self.name} retrieved.")
        return self.characteristics
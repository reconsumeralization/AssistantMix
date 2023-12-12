# assistant.py

import config
from utilities import logger, execute_in_sandbox
from ai_model import Mixtral8x7B

class Assistant:
    """
    Class representing an AI Assistant powered by the Mixtral-8x7B Large Language Model (LLM).
    """

    def __init__(self, name, characteristics=None, tools=None, files=None):
        self.name = name
        self.characteristics = characteristics if characteristics else {}
        self.tools = tools if tools else []
        self.files = files if files else []
        self.ai_model = Mixtral8x7B()
        logger.info(f"Assistant {self.name} initialized.")

    def customize(self, characteristics):
        """
        Customize the Assistant's characteristics.
        """
        self.characteristics.update(characteristics)
        self.ai_model.customize(characteristics)
        logger.info(f"Assistant {self.name} customized with characteristics: {characteristics}")

    def equip_tool(self, tool, index):
        """
        Equip the Assistant with a tool at a specific index.
        """
        if index < 0 or index >= len(self.tools):
            logger.error(f"Invalid tool index: {index}. Tool index must be between 0 and {len(self.tools) - 1}.")
            return

        self.tools[index] = tool
        self.ai_model.equip_tool(tool, index)
        logger.info(f"Assistant {self.name} equipped with tool {tool} at index {index}.")

    def upload_file(self, file):
        """
        Upload a file for the Assistant to use.
        """
        self.files.append(file)
        logger.info(f"File {file} uploaded for Assistant {self.name}.")

    def execute_code(self, code):
        """
        Execute Python code in a secure, sandboxed environment.
        """
        if config.OPEN_INTERPRETER_SANDBOXED:
            return execute_in_sandbox(code)
        else:
            logger.error("Open Interpreter is not configured to run in a sandboxed environment.")
            return None
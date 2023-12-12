# test_ai_model.py

import unittest
from ai_model import Mixtral8x7B
import config

class TestMixtral8x7B(unittest.TestCase):
    """
    Test cases for the Mixtral-8x7B Large Language Model (LLM).
    """

    def setUp(self):
        """
        Set up the AI model for testing.
        """
        self.ai_model = Mixtral8x7B()

    def test_initialization(self):
        """
        Test the initialization of the AI model.
        """
        self.assertEqual(self.ai_model.name, config.AI_MODEL_NAME)
        self.assertEqual(len(self.ai_model.tools), config.AI_MODEL_TOOLS)

    def test_customize(self):
        """
        Test the customization of the AI model.
        """
        characteristics = {"personality": "friendly", "knowledge": "extensive"}
        self.ai_model.customize(characteristics)
        self.assertEqual(self.ai_model.characteristics, characteristics)

    def test_equip_tool(self):
        """
        Test equipping a tool to the AI model.
        """
        tool = "Open Interpreter"
        index = 0
        self.ai_model.equip_tool(tool, index)
        self.assertEqual(self.ai_model.tools[index], tool)

    def test_remove_tool(self):
        """
        Test removing a tool from the AI model.
        """
        index = 0
        self.ai_model.remove_tool(index)
        self.assertIsNone(self.ai_model.tools[index])

    def test_invalid_tool_index(self):
        """
        Test handling of invalid tool index.
        """
        tool = "Open Interpreter"
        invalid_index = config.AI_MODEL_TOOLS + 1  # An index that is out of range
        with self.assertRaises(ValueError):
            self.ai_model.equip_tool(tool, invalid_index)

        with self.assertRaises(ValueError):
            self.ai_model.remove_tool(invalid_index)


if __name__ == "__main__":
    unittest.main()
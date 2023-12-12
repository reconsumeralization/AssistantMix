# test_assistant.py

import unittest
from assistant import Assistant
from ai_model import Mixtral8x7B
from utilities import logger

class TestAssistant(unittest.TestCase):
    """
    Test cases for the Assistant class.
    """

    def setUp(self):
        """
        Set up testing environment before each test.
        """
        self.assistant = Assistant("TestAssistant")
        self.characteristics = {"personality": "friendly", "knowledge": "general"}
        self.tools = ["tool1", "tool2", "tool3"]
        self.files = ["file1", "file2"]

    def test_init(self):
        """
        Test the initialization of the Assistant.
        """
        self.assertEqual(self.assistant.name, "TestAssistant")
        self.assertEqual(self.assistant.characteristics, {})
        self.assertEqual(self.assistant.tools, [])
        self.assertEqual(self.assistant.files, [])
        self.assertIsInstance(self.assistant.ai_model, Mixtral8x7B)

    def test_customize(self):
        """
        Test the customization of the Assistant.
        """
        self.assistant.customize(self.characteristics)
        self.assertEqual(self.assistant.characteristics, self.characteristics)
        self.assertEqual(self.assistant.ai_model.characteristics, self.characteristics)

    def test_equip_tool(self):
        """
        Test equipping a tool to the Assistant.
        """
        self.assistant.equip_tool(self.tools[0], 0)
        self.assertEqual(self.assistant.tools[0], self.tools[0])
        self.assertEqual(self.assistant.ai_model.tools[0], self.tools[0])

    def test_invalid_tool_index(self):
        """
        Test equipping a tool at an invalid index.
        """
        with self.assertLogs(logger, level='ERROR') as cm:
            self.assistant.equip_tool(self.tools[0], 200)
        self.assertIn('Invalid tool index', cm.output[0])

    def test_file_management(self):
        """
        Test file management in the Assistant.
        """
        self.assistant.manage_file(self.files[0], "upload")
        self.assertIn(self.files[0], self.assistant.files)

    def test_invalid_file_action(self):
        """
        Test invalid file action in the Assistant.
        """
        with self.assertLogs(logger, level='ERROR') as cm:
            self.assistant.manage_file(self.files[0], "invalid_action")
        self.assertIn('Invalid file action', cm.output[0])

if __name__ == "__main__":
    unittest.main()
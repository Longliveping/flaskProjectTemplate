import unittest
import os
from app import create_app
from flask import current_app

class WordsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()

    @unittest.skip('it takes time')
    def test_001_extract_text(self):
        file = os.path.join(current_app.config.get('TESTING_FOLDER'), 'Conversation.docx')

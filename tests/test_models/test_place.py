#!/usr/bin/python3
''' Class Test '''
import unittest
import json
import pep8
import inspect
import datetime
import os
from models.place import Place


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """Sets Model to get tested"""
        self.base = Place()

    def tearDown(self):
        """removes file"""
        self.base = Place()

    def object_Instance(self):
        """ tests Instance Creation"""
        self.assertIsInstance(self.place, BaseModel)

    def created_at_test(self):
        """created_at testing"""
        base = Place()
        self.assertEqual(type(base.created_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "created_at"))

    def updated_at_test(self):
        """updated testing"""
        base = Place()
        self.assertEqual(type(base.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "update_at"))

    def test_name(self):
        '''Test Email'''
        base = Place()
        self.assertEqual(type(base.name), str)
        self.assertTrue(hasattr(base, "name"))


if __name__ == '__main__':
    unittest.main()

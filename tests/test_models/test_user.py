#!/usr/bin/python3
''' Class Test '''
import unittest
import json
import pep8
import inspect
import datetime
import os
from models.user import User


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """Sets Model to get tested"""
        self.base = User()

    def tearDown(self):
        """removes file"""
        self.base = User()

    def object_Instance(self):
        """ tests Instance Creation"""
        self.assertIsInstance(self.user, BaseModel)

    def created_at_test(self):
        """created_at testing"""
        base = User()
        self.assertEqual(type(base.created_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "created_at"))

    def updated_at_test(self):
        """updated testing"""
        base = User()
        self.assertEqual(type(base.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "update_at"))

    def test_email(self):
        '''Test Email'''
        base = User()
        self.assertEqual(type(base.email), str)
        self.assertTrue(hasattr(base, "email"))

    def test_password(self):
        '''Test password'''
        base = User()
        self.assertEqual(type(base.password), str)
        self.assertTrue(hasattr(base, "password"))

    def test_first_name(self):
        '''Test first name'''
        base = User()
        self.assertEqual(type(base.first_name), str)
        self.assertTrue(hasattr(base, "first_name"))

    def test_last_name(self):
        '''Test last name'''
        base = User()
        self.assertEqual(type(base.last_name), str)
        self.assertTrue(hasattr(base, "last_name"))


if __name__ == '__main__':
    unittest.main()

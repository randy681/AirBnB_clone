#!/usr/bin/python3
''' Class Test '''
import unittest
import json
import pep8
import inspect
import datetime
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """Sets Model to get tested"""
        self.base = Amenity()

    def tearDown(self):
        """removes file"""
        self.base = Amenity()

    def object_Instance(self):
        """ tests Instance Creation"""
        self.assertIsInstance(self.amenity, BaseModel)

    def created_at_test(self):
        """created_at testing"""
        base = Amenity()
        self.assertEqual(type(base.created_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "created_at"))

    def updated_at_test(self):
        """updated testing"""
        base = Amenity()
        self.assertEqual(type(base.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "update_at"))

    def test_name(self):
        """name testing"""
        base = Amenity()
        self.assertTrue(hasattr(base, "name"))
        self.assertEqual(type(base.name), str)


if __name__ == '__main__':
    unittest.main()

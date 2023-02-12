#!/usr/bin/python3
''' Class Test '''
import unittest
import json
import pep8
import inspect
import datetime
import os
from models.review import Review


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """Sets Model to get tested"""
        self.base = Review()

    def tearDown(self):
        """removes file"""
        self.base = Review()

    def object_Instance(self):
        """ tests Instance Creation"""
        self.assertIsInstance(self.review, BaseModel)

    def created_at_test(self):
        """created_at testing"""
        base = Review()
        self.assertEqual(type(base.created_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "created_at"))

    def updated_at_test(self):
        """updated testing"""
        base = Review()
        self.assertEqual(type(base.updated_at), type(datetime.now()))
        self.assertTrue(hasattr(base, "update_at"))

    def test_user_id(self):
        '''Test user'''
        base = Review()
        self.assertEqual(type(base.user_id), str)
        self.assertTrue(hasattr(base, "user_id"))

    def test_place_id(self):
        '''Test place'''
        base = Review()
        self.assertEqual(type(base.place_id), str)
        self.assertTrue(hasattr(base, "place_id"))

    def test_text(self):
        '''Test text'''
        base = Review()
        self.assertEqual(type(base.text), str)
        self.assertTrue(hasattr(base, "text"))


if __name__ == '__main__':
    unittest.main()

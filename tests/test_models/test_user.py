#!/usr/bin/python3
"""Unittest for the user"""
import unittest
from models.user import User
import datetime


class test_user(unittest.TestCase):
    """Test methods and instances"""

    us = User()

    def test_class(self):
        """Test the class"""
        self.assertEqual(str(type(self.us)), "<class 'models.user.User'>")

    def test_inheritance(self):
        """test the inheritance"""
        self.assertIsInstance(self.us, User)

    def test_attrs(self):
        """test the attributes"""
        self.assertTrue(hasattr(self.us, 'password'))
        self.assertTrue(hasattr(self.us, 'id'))
        self.assertTrue(hasattr(self.us, 'email'))
        self.assertTrue(hasattr(self.us, 'updated_at'))
        self.assertTrue(hasattr(self.us, 'first_name'))
        self.assertTrue(hasattr(self.us, 'created_at'))
        self.assertTrue(hasattr(self.us, 'last_name'))

    def test_type(self):
        """Test the types of attributes"""
        self.assertIsInstance(self.us.email, str)
        self.assertIsInstance(self.us.first_name, str)
        self.assertIsInstance(self.us.updated_at, datetime.datetime)
        self.assertIsInstance(self.us.last_name, str)
        self.assertIsInstance(self.us.created_at, datetime.datetime)
        self.assertIsInstance(self.us.id, str)
        self.assertIsInstance(self.us.password, str)

if __name__ == '__main__':
    unittest.main()

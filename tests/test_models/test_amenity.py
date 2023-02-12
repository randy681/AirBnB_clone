#!/usr/bin/python3
"""Unittest for the amenity class"""

import unittest
from models.amenity import Amenity
import datetime


class testAmenity(unittest.TestCase):
    """Methods and instances test"""

    amen = Amenity()

    def test_class(self):
        """check class"""
        abs = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.amen)), abs)

    def test_inheritance(self):
        """check if it inherited"""
        self.assertIsInstance(self.amen, Amenity)

    def test_attrs(self):
        """check the attributes"""
        self.assertTrue(hasattr(self.amen, 'id'))
        self.assertTrue(hasattr(self.amen, 'created_at'))
        self.assertTrue(hasattr(self.amen, 'name'))
        self.assertTrue(hasattr(self.amen, 'updated_at'))

    def test_type(self):
        """check the attribute type"""
        self.assertIsInstance(self.amen.id, str)
        self.assertIsInstance(self.amen.name, str)
        self.assertIsInstance(self.amen.updated_at, datetime.datetime)
        self.assertIsInstance(self.amen.created_at, datetime.datetime)

if __name__ == '__main__':
    unittest.main()

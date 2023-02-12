#!/usr/bin/python3
"""Unittest for FileStorage class"""
from models.engine.file_storage import FileStorage
import models
import unittest
import json
import pep8
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import path
import os
from datetime import datetime


class TestCodeFormat(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_base_model_save(self):
        base = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def to_dict(self):
        base = FileStorage()
        self.assertEqual(type(base.to_dict()), dict)


if __name__ == '__main__':
    unittest.main()

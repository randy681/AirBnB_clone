#!/usr/bin/python3
import unittest
import pep8
import json
import inspect
import datetime
import os
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_id(self):
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        new = BaseModel()
        self.assertEqual(type(new.created_at),
                         datetime.datetime)

    def test_updated_at(self):
        new = BaseModel()
        self.assertEqual(type(new.updated_at), datetime.datetime)

    def test_str(self):
        new = BaseModel()
        self.assertEqual(str(new), "[{:s}] ({:s}) {}".format(
            new.__class__.__name__, new.id, new.__dict__))

    def save(self):
        base = BaseModel()
        base.save()
        self.assertTrue(os.path.exists(self.path_file('file.json')))

        def to_dict(self):
            base = BaseModel()
            self.assertEqual(type(base.to_dict()), dict)


if __name__ == '__main__':
    unittest.main()

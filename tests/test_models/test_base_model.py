#!/usr/bin/python3
""" Test cases"""



import unittest
import uuid
import json
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):
    """
    Test Cases
    """
    
    def setUp(self):
        pass
    
    def tearDown(self) -> None:
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
    
    def test_init(self):
        b1 = BaseModel()
        b2_uuid = str(uuid.uuid4())
        b2 = BaseModel(id=b2_uuid, name="Wileli", location="Naivasha")
        self.assertIsInstance(b1.id, str)
        self.assertIsInstance(b2.id, str)
        self.assertEqual(b2_uuid, b2.id)
        self.assertEqual(b2.location, "Naivasha")
        self.assertEqual(b2.name, "Wileli")
        self.assertIsInstance(b1.created_at, datetime)
        
    
    def test_dict(self):
        b1 = BaseModel()
        b2_uuid = str(uuid.uuid4())
        b2 = BaseModel(id=b2_uuid, name="Wileli", location="Naivasha")
        b1_dict = b1.to_dict()
        self.assertIsInstance(b1_dict, dict)
        self.assertIn('id',b1_dict.keys())
        self.assertIn('created_at',b1_dict.keys())
        self.assertIn('updated_at',b1_dict.keys())
        
    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = dt
        bmstr = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bmstr)
        self.assertIn("'id': '123456'", bmstr)
        self.assertIn("'created_at': " + dt_repr, bmstr)
        self.assertIn("'updated_at': " + dt_repr, bmstr)
        
    def test_save_storage(self):
        """Tests that storage.save() is called from save()."""
        b = BaseModel()
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        self.assertTrue(os.path.isfile(FileStorage._FileStorage__file_path))
        with open(FileStorage._FileStorage__file_path,
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)

if __name__ == "__main__":
    unittest.main()       

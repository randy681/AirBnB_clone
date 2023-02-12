#!/usr/bin/python3
"""Unittest module to test `base_model`
"""
import os
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing `BaseModel` instantiation
    """

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_id_is_unique(self):
        inst1 = BaseModel()
        inst2 = BaseModel()
        self.assertNotEqual(inst1.id, inst2.id)

    def test_two_models_created_at_different(self):
        inst1 = BaseModel()
        inst2 = BaseModel()
        self.assertLess(inst1.created_at, inst2.created_at)

    def test_two_models_updated_at_different(self):
        inst1 = BaseModel()
        inst2 = BaseModel()
        self.assertLess(inst1.updated_at, inst2.updated_at)

    def test_str_method(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        bm = BaseModel()
        bm.id = "9876543210"
        bm.created_at = bm.updated_at = dt
        str_bm = bm.__str__()
        self.assertIn("[BaseModel] (9876543210)", str_bm)
        self.assertIn("'created_at': " + dt_repr, str_bm)
        self.assertIn("'updated_at': " + dt_repr, str_bm)

    def test_instantiation_with_None_args(self):
        inst = BaseModel(None)
        self.assertNotIn(None, inst.__dict__.values())

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        inst = BaseModel(id="091", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(inst.id, "091")
        self.assertEqual(inst.created_at, dt)
        self.assertEqual(inst.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        inst = BaseModel(
                "12", id="71425908", created_at=dt_iso,
                updated_at=dt_iso
        )
        self.assertEqual(inst.id, "71425908")
        self.assertEqual(inst.created_at, dt)
        self.assertEqual(inst.updated_at, dt)

    def test_save(self):
        ans = BaseModel()
        self.assertFalse(hasattr(ans, 'updated_at'))
        ans.save()
        self.assertTrue(hasattr(ans, 'updated_at'))

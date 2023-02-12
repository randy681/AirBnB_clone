#!/usr/bin/python3
''' module for amenity tests '''
from unittest import TestCase
import json
import re
from uuid import UUID, uuid4
from datetime import datetime
from time import sleep

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(TestCase):
    ''' tests Amenity class '''
    def test_9(self):
        ''' task 9 tests '''
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertEqual(Amenity.name, '')

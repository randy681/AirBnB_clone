#!/usr/bin/python3
''' module for city tests '''
from unittest import TestCase
import json
import re
from uuid import UUID, uuid4
from datetime import datetime
from time import sleep

from models.base_model import BaseModel
from models.city import City


class TestCity(TestCase):
    ''' tests City class '''
    def test_9(self):
        ''' task 9 tests '''
        self.assertTrue(issubclass(City, BaseModel))
        self.assertEqual(City.state_id, '')
        self.assertEqual(City.name, '')

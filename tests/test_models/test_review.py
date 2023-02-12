#!/usr/bin/python3
''' module for review tests '''
from unittest import TestCase
import json
import re
from uuid import UUID, uuid4
from datetime import datetime
from time import sleep

from models.base_model import BaseModel
from models.review import Review


class TestCity(TestCase):
    ''' tests Review class '''
    def test_9(self):
        ''' task 9 tests '''
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertEqual(Review.place_id, '')
        self.assertEqual(Review.user_id, '')
        self.assertEqual(Review.text, '')

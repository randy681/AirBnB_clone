#!/usr/bin/python3
''' module for user tests '''
from unittest import TestCase
import json
import re
from uuid import UUID, uuid4
from datetime import datetime
from time import sleep

from models.base_model import BaseModel
from models.user import User


class TestUser(TestCase):
    ''' tests User class '''
    def test_8(self):
        ''' task 8 tests '''
        self.assertTrue(issubclass(User, BaseModel))
        self.assertEqual(User.email, '')
        self.assertEqual(User.password, '')
        self.assertEqual(User.first_name, '')
        self.assertEqual(User.last_name, '')

#!/usr/bin/python3
''' module for User class '''
from .base_model import BaseModel


class User(BaseModel):
    ''' a User class '''
    email = ''
    password = ''
    first_name = ''
    last_name = ''

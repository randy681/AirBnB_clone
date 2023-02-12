#!/usr/bin/python3
"""
Module for BaseModel class
"""
import models
import uuid
from datetime import datetime


class BaseModel():
    """
    base class which defines all methods for other classes
    """
    def __init__(self, *args, **kwargs):
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            self.__dict__.update(kwargs)

    def __str__(self):
        """"Returns a string representation of instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """saves the updated object"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """"Convert the instance to a dictionary"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class_':
                          (str(type(self)).split('.')[-1]).split('\'')})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

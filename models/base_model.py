#!/usr/bin/python3
''' module for BaseModel class '''
from uuid import uuid4
from datetime import datetime
from . import storage


class BaseModel:
    ''' class of the base model of higher-level data models '''
    def __init__(self, *arg, **kwargs):
        ''' BaseModel constructor '''
        if kwargs:
            for k in kwargs:
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(kwargs[k]))
                elif k != '__class__':
                    setattr(self, k, kwargs[k])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at.replace()
            storage.new(self)

    def save(self):
        ''' saves a model '''
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
        ''' returns a dictionary representation of the model '''
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct

    def __str__(self):
        ''' returns a string representation of the model '''
        return '[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__)

#!/usr/bin/python3
"""BaseModel class Module"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ A class called BaseModel
    attributes:
    att1: id
    att2: created_at
    att3: updated_at
    """
    def __init__(self, *args, **kwargs):
        """initializing an instance"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if (key == "created_at" or key == "updated_at"):
                        if (type(value) == str):
                            new_object = datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f')
                            self.__dict__[key] = new_object
                    else:
                        self.__dict__[key] = value

    def __str__(self):
        """ prints the str rep of [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        new_dict['updated_at'] = self.updated_at.strftime(
            "%Y-%m-%dT%H:%M:%S.%f")
        return new_dict

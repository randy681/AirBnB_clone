#!/usr/bin/python3
''' creates a static FileStorage instance '''
from .engine.file_storage import FileStorage

storage = FileStorage()
# storage._FileStorage__file_path = 'data.json'
# storage._FileStorage__objects = {}
models = {}


def import_models():
    '''import modules after instantiating a storage instace
    to fix circular imports'''
    global models
    from .base_model import BaseModel
    from .amenity import Amenity
    from .city import City
    from .place import Place
    from .review import Review
    from .state import State
    from .user import User

    models = {c.__name__: c
              for c in [BaseModel, Amenity, City, Place, Review, State, User]}


import_models()
storage.reload()

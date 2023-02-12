#!/usr/bin/python3
''' module for FileStorage class '''
import json
from os.path import isfile
import models


class FileStorage:
    ''' class for persistent storage '''
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        ''' initializes a storage engine '''
        pass

    def all(self):
        ''' gets all objects '''
        return self.__objects

    def new(self, obj):
        ''' registers a new object '''
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        ''' saves all objects to a file '''
        with open(self.__file_path, 'w') as file:
            r_objs = self.__objects
            objs = {}
            for k in r_objs:
                v = r_objs[k]
                objs[k] = v.to_dict()
            json.dump(objs, file)

    def reload(self):
        ''' loads data from file '''
        return 4

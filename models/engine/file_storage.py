#!/usr/bin/python3
"""
Defines a FileStorage class
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """
    that serializes instances to a JSON file and
    deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """"returns a dictionary of obj in storage"""
        one_type_objects = {}
        if cls is not None:
            for key, value in self.__objects.items():
                if key.startswith(str(cls.__name__)):
                    one_type_objects[key] = value
        else:
            one_type_objects = self.__objects
        return one_type_objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
         serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, value in temp.items():
                temp[key] = value.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """To delete an object"""
        if obj:
            new_key = "{}.{}".format(type(obj).__name__, obj.id)
            if new_key in self.__objects:
                del self.__objects[new_key]
                self.save()

    def reload(self):
        """
        deserializes the JSON file to __objects only if the JSON
        file exists; otherwise, does nothing
        """
        current_classes = {'BaseModel': BaseModel, 'User': User,
                           'Amenity': Amenity, 'City': City, 'State': State,
                           'Place': Place, 'Review': Review}

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, 'r') as f:
            deserialized = None

            try:
                deserialized = json.load(f)
            except json.JSONDecodeError:
                pass

            if deserialized is None:
                return

            FileStorage.__objects = {
                k: current_classes[k.split('.')[0]](**v)
                for k, v in deserialized.items()}

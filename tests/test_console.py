#!/usr/bin/python3
"""Test Module for HBNBCommand class."""
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
import datetime
from unittest.mock import patch
import os
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Tests for HBNBCommand console"""

    def setUp(self):
        """Sets up test cases."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_help_console(self):
        """Tests the help command."""

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        s = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
"""
        self.assertEqual(s, f.getvalue())

    def test_help_EOF(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
        s = 'Type EOF to exit the command interpreter\n'
        self.assertEqual(s, f.getvalue())

    def test_help_quit(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        s = 'Type quit to exit the command interpreter\n'
        self.assertEqual(s, f.getvalue())

    def test_help_create(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        s = 'Creates a new Instance\n'
        self.assertEqual(s, f.getvalue())

    def test_help_show(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        s = "Prints the string representation of an instance base " + \
            "on\n        the class name and id\n        \n"
        self.assertEqual(s, f.getvalue())

    def test_help_destroy(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
        s = "Deletes an instance based on the class name and " + \
            "id\n        Exmaple: (hbnb) destroy User a8d30b54-af4d-" + \
            "401e-ba78-4c11c8294264\n        \n"
        self.assertEqual(s, f.getvalue())

    def test_help_all(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
        s = "Prints all string representation of " + \
            "all instances\n        based or not on the class name\n        \n"
        self.assertEqual(s, f.getvalue())

    def test_help_count(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
        s = "Method to count instances\n"
        self.assertEqual(s, f.getvalue())

    def test_help_update(self):
        """Tests the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
        s1 = 'Updates an instance based on the class name\n        '

        s2 = 'and id by adding or updating attribute\n        \n'
        s = s1 + s2
        self.assertEqual(s, f.getvalue())

    def test_emptyline(self):
        """Tests emptyline functionality."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        s = ""
        self.assertEqual(s, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("                  \n")
        s = ""
        self.assertEqual(s, f.getvalue())

    def test_do_quit(self):
        """Tests quit commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    def test_do_EOF(self):
        """Tests EOF commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        msg = f.getvalue()
        self.assertTrue(len(msg) == 0)
        self.assertEqual("", msg)

    def test_do_create(self):
        """Tests create for all classes."""
        for class_name in self.classes():
            self.help_test_do_create(class_name)

    def help_test_do_create(self, class_name):
        """Helper method to test the create commmand."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create {}".format(class_name))
        uid = f.getvalue()[:-1]
        self.assertTrue(len(uid) > 0)
        key = "{}.{}".format(class_name, uid)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all {}".format(class_name))
        self.assertTrue(uid in f.getvalue())

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def test_do_all_BaseModel(self):
        """Tests all commmand."""
        Instance = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.all()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_all_Review(self):
        """Tests all commmand."""
        Instance = Review()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.all()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_all_User(self):
        """Tests all commmand."""
        Instance = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.all()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_all_State(self):
        """Tests all commmand."""
        Instance = State()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.all()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_all_City(self):
        """Tests all commmand."""
        Instance = City()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.all()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_all_Amenity(self):
        """Tests all commmand."""
        Instance = Amenity()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.all()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_all_Place(self):
        """Tests all commmand."""
        Instance = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.all()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_count_BaseModel(self):
        """Tests count commmand."""
        Instance = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.count()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_count_Review(self):
        """Tests count commmand."""
        Instance = Review()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.count()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_count_User(self):
        """Tests count commmand."""
        Instance = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.count()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_count_State(self):
        """Tests count commmand."""
        Instance = State()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.count()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_count_City(self):
        """Tests count commmand."""
        Instance = City()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.count()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_count_Amenity(self):
        """Tests count commmand."""
        Instance = Amenity()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.count()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_count_Place(self):
        """Tests count commmand."""
        Instance = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.count()")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_show_BaseModel(self):
        """Tests show commmand."""
        Instance = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.show({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_show_Review(self):
        """Tests show commmand."""
        Instance = Review()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.show({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_show_User(self):
        """Tests show commmand."""
        Instance = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_show_State(self):
        """Tests show commmand."""
        Instance = State()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.show({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_show_City(self):
        """Tests show commmand."""
        Instance = City()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.show({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_show_Amenity(self):
        """Tests show commmand."""
        Instance = Amenity()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_show_Place(self):
        """Tests show commmand."""
        Instance = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_destroy_BaseModel(self):
        """Tests destroy commmand."""
        Instance = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.destroy({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_destroy_Review(self):
        """Tests destroy commmand."""
        Instance = Review()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.destroy({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_destroy_User(self):
        """Tests destroy commmand."""
        Instance = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.destroy({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_destroy_State(self):
        """Tests destroy commmand."""
        Instance = State()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.destroy({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_destroy_City(self):
        """Tests destroy commmand."""
        Instance = City()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.destroy({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_destroy_Amenity(self):
        """Tests show commmand."""
        Instance = Amenity()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_destroy_Place(self):
        """Tests destroy commmand."""
        Instance = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.destroy({Instance.id})")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_update_BaseModel(self):
        """Tests update commmand."""
        Instance = BaseModel()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update(, id, att, value)")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_update_Review(self):
        """Tests value commmand."""
        Instance = Review()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update(id, att, value)")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_update_User(self):
        """Tests update commmand."""
        Instance = User()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update(id, att, value)")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_update_State(self):
        """Tests update commmand."""
        Instance = State()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update(id, att, value)")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_update_City(self):
        """Tests update commmand."""
        Instance = City()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update(id, att, value)")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_update_Amenity(self):
        """Tests update commmand."""
        Instance = Amenity()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update(id, att, value)")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)

    def test_do_update_Place(self):
        """Tests update commmand."""
        Instance = Place()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update(id, att, value)")
        msg = f.getvalue()
        self.assertTrue(len(msg) != 0, True)


if __name__ == "__main__":
    unittest.main()

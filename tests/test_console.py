#!/usr/bin/python3
''' module for file_storage tests '''
from unittest import TestCase
from unittest.mock import patch
import json
import re
import sys
from uuid import UUID, uuid4
from datetime import datetime
from time import sleep
import os
from io import StringIO

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage
from console import HBNBCommand


def clio(sio):
    ''' clears a string i/o buffer '''
    sio.seek(0)
    sio.truncate(0)


class TestHBNBCommand(TestCase):
    ''' tests HBNBCommand class '''
    def test_6(self):
        ''' task 6 test '''
        FS_dict = FileStorage.__dict__
        FS__path = '_FileStorage__file_path'
        FS__objs = '_FileStorage__objects'
        FS_path = FS_dict[FS__path]
        FS_objs = FS_dict[FS__objs]

        sio = StringIO()
        with patch('sys.stdout', new=sio) as f:
            app = HBNBCommand()

            # TODO: help, quit and EOF validation
            # help not empty
            app.onecmd("help")
            self.assertTrue(sio.getvalue())

    def test_7(self):
        ''' task 7 test '''
        FS_dict = FileStorage.__dict__
        FS__path = '_FileStorage__file_path'
        FS__objs = '_FileStorage__objects'
        FS_path = FS_dict[FS__path]
        FS_objs = FS_dict[FS__objs]

        sio = StringIO()
        with patch('sys.stdout', new=sio) as f:
            app = HBNBCommand()

            # create
            # no arg
            clio(sio)
            app.onecmd("create")
            self.assertEqual(sio.getvalue(), "** class name missing **\n")

            # invalid arg
            clio(sio)
            app.onecmd("create ABC")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            # case-sensitivity
            app.onecmd("create basemodel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("create Basemodel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("create Base")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("create baseModel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")

            # valid arg
            clio(sio)
            objs_k = storage.all().copy()
            app.onecmd("create BaseModel")
            # model creation
            kid = 'BaseModel.{}'.format(sio.getvalue()[:-1])
            self.assertTrue(kid not in objs_k and kid in storage.all() and
                            type(storage.all()[kid]) == BaseModel)
            # saved to file
            with open(FS_path, 'r') as file:
                tmp = json.load(file)
                self.assertTrue(type(tmp) is dict and kid in tmp)
            obj = storage.all()[kid]
            storage.all().clear()
            storage.reload()
            self.assertTrue(kid in storage.all())
            self.assertEqual(obj.to_dict(), storage.all()[kid].to_dict())

            ##
            ##
            ##
            ##
            # show
            # missing model
            clio(sio)
            app.onecmd("show")
            self.assertEqual(sio.getvalue(), "** class name missing **\n")

            # invalid model
            clio(sio)
            app.onecmd("show ABC")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            # case-sensitivity
            app.onecmd("show basemodel ")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("show Basemodel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("show Base")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("create baseModel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")

            # missing id
            clio(sio)
            app.onecmd("show BaseModel")
            self.assertEqual(sio.getvalue(), "** instance id missing **\n")
            clio(sio)
            app.onecmd("show BaseModel ")
            self.assertEqual(sio.getvalue(), "** instance id missing **\n")

            # invalid id
            clio(sio)
            app.onecmd("show BaseModel dkkd")
            self.assertEqual(sio.getvalue(), "** no instance found **\n")
            clio(sio)
            app.onecmd("show BaseModel {}".format(str(uuid4())))
            self.assertEqual(sio.getvalue(), "** no instance found **\n")

            # valid args
            clio(sio)
            obj = BaseModel()
            # correct string representation
            self.assertEqual(str(obj), '[{}] ({}) {}'.format(
                'BaseModel', obj.id, obj.__dict__))

            key = 'BaseModel.{}'.format(obj.id)
            app.onecmd("show BaseModel {}".format(obj.id))
            self.assertEqual(sio.getvalue(), str(obj)+'\n')
            clio(sio)
            obj = BaseModel()
            key = 'BaseModel.{}'.format(obj.id)
            app.onecmd("show BaseModel {}".format(obj.id))
            self.assertEqual(sio.getvalue(), str(obj)+'\n')

            # ## ???
            # clio(sio)
            # obj.id=str(uuid4())
            # key = 'BaseModel.{}'.format(obj.id)
            # app.onecmd("show BaseModel {}".format(obj.id))
            # self.assertEqual(sio.getvalue(), str(obj)+'\n')

            del storage.all()[key]
            clio(sio)
            app.onecmd("show BaseModel {}".format(obj.id))
            self.assertEqual(sio.getvalue(), "** no instance found **\n")

            # precedence
            clio(sio)
            obj = BaseModel()
            app.onecmd("show ABC {}".format(obj.id))  # valid id
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("show ABC {}".format(str(uuid4())))  # invalid id
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")

            ##
            ##
            ##
            ##
            # destroy
            # missing model
            clio(sio)
            app.onecmd("destroy")
            self.assertEqual(sio.getvalue(), "** class name missing **\n")

            # invalid model
            clio(sio)
            app.onecmd("destroy ABC")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            # case-sensitivity
            app.onecmd("destroy basemodel ")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("destroy Basemodel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("destroy Base")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("destroy baseModel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")

            # missing id
            clio(sio)
            app.onecmd("destroy BaseModel")
            self.assertEqual(sio.getvalue(), "** instance id missing **\n")
            clio(sio)
            app.onecmd("destroy BaseModel ")
            self.assertEqual(sio.getvalue(), "** instance id missing **\n")

            # invalid id
            clio(sio)
            app.onecmd("destroy BaseModel dkkd")
            self.assertEqual(sio.getvalue(), "** no instance found **\n")
            clio(sio)
            app.onecmd("destroy BaseModel {}".format(str(uuid4())))
            self.assertEqual(sio.getvalue(), "** no instance found **\n")

            # valid args
            clio(sio)
            obj = BaseModel()
            storage.save()
            # correct string representation
            self.assertEqual(str(obj), '[{}] ({}) {}'.format(
                'BaseModel', obj.id, obj.__dict__))

            key = 'BaseModel.{}'.format(obj.id)
            storage.all().clear()
            storage.reload()
            self.assertTrue(key in storage.all())
            objs = storage.all()
            objs_cp = objs.copy()
            app.onecmd("destroy BaseModel {}".format(obj.id))
            self.assertTrue(key not in storage.all())
            objs.clear()
            storage.reload()
            self.assertTrue(key not in storage.all())
            self.assertEqual(sio.getvalue(), '')

            # precedence
            clio(sio)
            obj = BaseModel()
            app.onecmd("destroy ABC {}".format(obj.id))  # valid id
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("destroy ABC {}".format(str(uuid4())))  # invalid id
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")

            # all
            # invalid model
            clio(sio)
            app.onecmd("all ABC")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            # case-sensitivity
            app.onecmd("all basemodel ")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("all Basemodel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("all Base")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("all baseModel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")

            # valid args
            clio(sio)
            obj = BaseModel()
            # correct string representation
            self.assertEqual(str(obj), '[{}] ({}) {}'.format(
                'BaseModel', obj.id, obj.__dict__))
            key = 'BaseModel.{}'.format(obj.id)
            app.onecmd("all")
            siov = sio.getvalue()
            self.assertTrue(siov.endswith('\n'))
            self.assertEqual(sorted(json.loads(siov)),
                             sorted([str(v) for v in storage.all().values()]))

            clio(sio)
            obj = BaseModel()
            # correct string representation
            self.assertEqual(str(obj), '[{}] ({}) {}'.format(
                'BaseModel', obj.id, obj.__dict__))
            key = 'BaseModel.{}'.format(obj.id)
            app.onecmd("all BaseModel")
            siov = sio.getvalue()
            self.assertTrue(siov.endswith('\n'))
            try:
                self.assertEqual(sorted(json.loads(siov)),
                                 sorted([str(v) for v in storage.all().values()
                                         if type(v) is BaseModel]))
            except Exception as err:
                self.assertTrue(False)

            # update
            # missing model
            clio(sio)
            app.onecmd("update")
            self.assertEqual(sio.getvalue(), "** class name missing **\n")

            # invalid model
            clio(sio)
            app.onecmd("update ABC")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            # case-sensitivity
            app.onecmd("update basemodel ")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("update Basemodel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("update Base")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("update baseModel")
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")

            # missing id
            clio(sio)
            app.onecmd("update BaseModel")
            self.assertEqual(sio.getvalue(), "** instance id missing **\n")
            clio(sio)
            app.onecmd("update BaseModel   ")
            self.assertEqual(sio.getvalue(), "** instance id missing **\n")

            # invalid id
            clio(sio)
            app.onecmd("update BaseModel abc")
            self.assertEqual(sio.getvalue(), "** no instance found **\n")
            clio(sio)
            app.onecmd("update BaseModel {}".format(str(uuid4())))
            self.assertEqual(sio.getvalue(), "** no instance found **\n")

            # missing attribute
            clio(sio)
            obj = BaseModel()
            app.onecmd("update BaseModel {}".format(obj.id))
            self.assertEqual(sio.getvalue(), "** attribute name missing **\n")

            # missing value
            clio(sio)
            obj = BaseModel()
            app.onecmd("update BaseModel {} updated_at".format(obj.id))
            self.assertEqual(sio.getvalue(), "** value missing **\n")
            clio(sio)
            obj = BaseModel()
            app.onecmd("update BaseModel {} updated_at    ".format(obj.id))
            self.assertEqual(sio.getvalue(), "** value missing **\n")

            # valid args
            clio(sio)
            obj = BaseModel()
            key = 'BaseModel.{}'.format(obj.id)
            # correct string representation
            self.assertEqual(str(obj), '[{}] ({}) {}'.format(
                'BaseModel', obj.id, obj.__dict__))

            app.onecmd('update BaseModel {} email "abc@def.com"'.format(
                obj.id))
            self.assertEqual(sio.getvalue(), '')
            self.assertEqual(getattr(obj, 'email', ''), 'abc@def.com')
            # persistence
            storage.all().clear()
            storage.reload()
            self.assertEqual(getattr(storage.all()[key], 'email', ''),
                             'abc@def.com')

            # extra args ignored
            clio(sio)
            obj = storage.all()[key]
            app.onecmd('update BaseModel {} email "abcd@def.com" name ghk'
                       .format(obj.id))
            self.assertEqual(sio.getvalue(), '')
            self.assertEqual(getattr(obj, 'email', ''), 'abcd@def.com')
            self.assertFalse(hasattr(obj, 'name'))

            # precedence
            clio(sio)
            obj = BaseModel()
            app.onecmd("update ABC {}".format(obj.id))  # valid id
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")

            clio(sio)
            app.onecmd("update ABC {}".format(str(uuid4())))  # invalid id
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd("update ABC {} email".format(
                obj.id))  # valid id and attribute
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")
            clio(sio)
            app.onecmd('update ABC {} email "abc@123.com"'.format(
                obj.id))  # valid id, attribute and value
            self.assertEqual(sio.getvalue(), "** class doesn't exist **\n")

    def test_8(self):
        '''tests for task 8 in console app and User class'''
        console = HBNBCommand()
        buf = StringIO()

        with patch('sys.stdout', new=buf) as f:
            # test [ create ] command with User class
            console.onecmd('create User')
            user_id = buf.getvalue().strip()
            self.assertTrue(user_id)
            clio(buf)

            # test [ show ] command with the last User created
            console.onecmd('show User ' + user_id)
            self.assertTrue(('[User] (' + user_id + ')') in buf.getvalue())
            clio(buf)

            # test [ all ] command with User class
            console.onecmd('all User')
            self.assertTrue(('[User] (' + user_id + ')') in buf.getvalue())
            clio(buf)

            # test [ update ] command in the last user created with
            # comma seperated args
            console.onecmd(
                'update User ' + user_id +
                ' first_name updatedName'
                )
            console.onecmd('show User ' + user_id)
            self.assertTrue("'first_name': 'updatedName'" in buf.getvalue())
            clio(buf)

            # test [ destroy ] command to destroy last created User
            console.onecmd('destroy User ' + user_id)
            self.assertEqual(buf.getvalue(), "")
            console.onecmd('show User ' + user_id)
            self.assertEqual(buf.getvalue(), "** no instance found **\n")
            clio(buf)

    def test_11(self):
        '''tests for task 11 about dot commands syntax for the all command'''
        console = HBNBCommand()
        buf = StringIO()

        with patch('sys.stdout', new=buf) as f:
            console.onecmd('create State')
            state_id = buf.getvalue().strip()
            clio(buf)
            line = console.precmd('State.all()')
            console.onecmd(line)
            self.assertTrue(state_id in buf.getvalue())
            clio(buf)

    def test_12(self):
        '''tests for task 12 about dot commands syntax for the count command'''
        console = HBNBCommand()
        buf = StringIO()

        with patch('sys.stdout', new=buf) as f:
            console.onecmd('create State')
            clio(buf)
            line = console.precmd('State.count()')
            console.onecmd(line)
            self.assertTrue(0 <= int(buf.getvalue()))
            clio(buf)

    def test_13(self):
        '''tests for task 13 about dot commands syntax for the show command'''
        console = HBNBCommand()
        buf = StringIO()

        with patch('sys.stdout', new=buf) as f:
            console.onecmd('create State')
            state_id = buf.getvalue().strip()
            clio(buf)
            line = console.precmd('State.show(' + state_id + ')')
            console.onecmd(line)
            self.assertTrue(state_id in buf.getvalue())
            clio(buf)

    def test_14(self):
        ''' tests for task 14 about dot commands syntax for
            the destroy command
        '''
        console = HBNBCommand()
        buf = StringIO()

        with patch('sys.stdout', new=buf) as f:
            console.onecmd('create Review')
            review_id = buf.getvalue().strip()
            clio(buf)
            line = console.precmd('Review.destroy(' + review_id + ')')
            console.onecmd(line)
            clio(buf)
            console.onecmd('show Review ' + review_id)
            self.assertEqual(buf.getvalue(), "** no instance found **\n")
            clio(buf)

    def test_15(self):
        '''tests for task 15 about dot commands syntax for the update command
            with quoted strings
        '''
        console = HBNBCommand()
        buf = StringIO()

        with patch('sys.stdout', new=buf) as f:
            console.onecmd('create Review')
            review_id = buf.getvalue().strip()
            clio(buf)
            line = console.precmd(
                'Review.update(' + review_id +
                ', text, "this room is good")'
                )
            console.onecmd(line)
            console.onecmd('show Review ' + review_id)
            self.assertTrue("'text': 'this room is good'" in buf.getvalue())
            clio(buf)

    def test_16(self):
        '''tests for task 16 about dot commands syntax for the update command
            but using dictionarry arguments and quoted strings
        '''
        console = HBNBCommand()
        buf = StringIO()

        with patch('sys.stdout', new=buf) as f:
            console.onecmd('create Review')
            review_id = buf.getvalue().strip()
            clio(buf)
            line = console.precmd(
                'Review.update(' + review_id +
                ", {'text': 'worth it', 'user name': 'not me'})"
                )
            console.onecmd(line)
            console.onecmd('show Review ' + review_id)
            self.assertTrue(
                "'text': 'worth it', 'user name': 'not me'" in buf.getvalue()
                )
            clio(buf)

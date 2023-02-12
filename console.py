#!/usr/bin/python3
"""
module holds entry point of command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNH Console
    """
    prompt = "(hbnb) "

    allowed_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Place": Place,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF signal to exit the program
        """
        print("")
        return True

    def help(self):
        """
        help command
        """
        return True

    def emptyline(self):
        """
        registers an empty line and does a pass
        """
        pass

    def do_create(self, line):
        """
        creates a new class instance of BaseModel
        """

        if len(line) == 0:
            print('** class name missing **')

        elif line not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")

        for key, value in HBNBCommand.allowed_classes.items():
            if line == key:
                new_obj = HBNBCommand.allowed_classes[line]()
                print(new_obj.id)
                storage.new(new_obj)
                storage.save()
        return

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        command = line.partition(" ")
        class_name = command[0]
        class_id = command[2]

        if not class_name:
            print('** class name missing **')
            return False

        elif class_name not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return False

        elif not class_id:
            print('** instance id missing **')
            return False

        key = class_name + '.' + class_id

        try:
            print(storage._FileStorage__objects[key])

        except KeyError:
            print("** no instance found **")
            return False

    def do_destroy(self, line):
        """
        deletes an instance specified by user
        """
        command = line.partition(" ")
        class_name = command[0]
        class_id = command[2]

        if not class_name:
            print("** class name missing **")
            return False

        if class_name not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return False

        if not class_id:
            print("** instance id missing **")
            return False

        key = class_name + '.' + class_id

        try:
            del(storage.all()[key])
            storage.save()

        except KeyError:
            print("** no instance found **")
            return False

    def do_all(self, line):
        """
        prints all string rep of instance
        based or not in the class name
        """
        all_list = []

        if line:
            split = line.split(" ")[0]
            if line not in HBNBCommand.allowed_classes:
                print("** class doesn't exist **")
                return False
            for key, value in storage._FileStorage__objects.items():
                all_list.append(str(value))
        else:
            for key, value in storage._FileStorage__objects.items():
                all_list.append(str(value))

        print(all_list)

    def do_update(self, line):
        """
        Updates an instance based or not in the class name
        """
        command = line.partition(" ")
        class_name = command[0]
        class_id = command[2]
        id_part = class_id.partition(" ")
        class_id = id_part[0]
        email = id_part[2].partition(" ")
        class_attr = email[0]
        class_attr_val = email[2]

        if not class_name:
            print("** class name missing **")
            return

        if class_name not in HBNBCommand.allowed_classes:
            print("** class doesn't exist **")
            return

        if not class_id:
            print("** instance id missing **")
            return

        if class_id:
            class_name = class_name + "." + class_id
            if class_name not in storage.all().keys():
                print("** no instance found **")
                return

        if not class_attr:
            print("** attribute name missing **")
            return

        if not class_attr_val:
            print("** value missing **")
            return

        if class_attr:
            for key, value in storage.all().items():
                if class_id == value.id:
                    setattr(value, class_attr, str(class_attr_val))
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

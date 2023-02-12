#!/usr/bin/python3
""" Command interpretor """
import cmd
import re
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Represents the Base model for all other classes in the project
    Attributes:
        prompt (str): Displays a `(hbnb`) prompt and waits for a command
    """

    prompt = "(hbnb) "
    __my_classes = {
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
    }

    def emptyline(self):
        """Called when nothing is typed before hitting enter
        """
        pass

    def default(self, arg):
        """Method called on an input line when the command prefix
        is not recognied
        """
        commands = {
                "all": self.do_all,
                "show": self.do_show,
                "count": self.do_count,
                "update": self.do_update,
                "destroy": self.do_destroy
        }
        try:
            values = arg.split('.')
            puncts = re.search(r"\((.*?)\)", arg)
            if puncts is not None:
                raw_re = re.search(r"\((.*?)\)", arg)
                clean = ([arg[:raw_re.span()[0]],
                         raw_re.group()[1:-1]])
                if len(clean) == 2:
                    value = str(clean[0]).split('.')
                    execute = "{} {}".format(value[0], clean[1].strip('"'))
                    return commands[value[1]](execute)
            else:
                command = values[1][:-2]
                if (command in commands.keys()and (
                        values[0] in HBNBCommand.__my_classes)):
                    commands[command](values[0])
        except Exception as e:
            print(e)

    def do_EOF(self, arg):
        """`EOF` signal to exit the program
        """
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_create(self, arg):
        """Crates a new instance, saves it (to JSON file) and prints the `id`.
        Usage: create <class>
        """
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.__my_classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            models.storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        Usage: `$ show <class name> <id>
        """
        obj_dict = models.storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        else:
            tokens = arg.split()

            if tokens[0] not in HBNBCommand.__my_classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            elif (tokens[0] + '.' + tokens[1]) not in obj_dict:
                print("** no instance found **")
            else:
                print(obj_dict[tokens[0] + '.' + tokens[1]])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id,
        and saves the changes into (the) JSON file
        Usage: `$ destroy <class name> <instance id>
        """
        obj_dict = models.storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        else:
            tokens = arg.split()

            if tokens[0] not in HBNBCommand.__my_classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            elif (tokens[0] + '.' + tokens[1]) not in obj_dict:
                print("** no instance found **")
            else:
                del obj_dict[tokens[0] + '.' + tokens[1]]
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the classe name
        Usage: `$ all <class name>`
        """
        obj_dict = models.storage.all()
        selected = []
        if len(arg) != 0:
            if arg not in HBNBCommand.__my_classes:
                print("** class doesn't exist **")
            else:
                for each in obj_dict.values():
                    if arg == each.__class__.__name__:
                        selected.append(each.__str__())
                print(selected)

        else:
            for each in obj_dict.values():
                selected.append(each.__str__())
            print(selected.__str__())

    def do_count(self, arg):
        """Retrives the number of instances of a classe
        """
        obj_dict = models.storage.all()
        cnt = 0
        if len(arg) == 0:
            print("** class name missing **")
        else:
            if arg not in HBNBCommand.__my_classes:
                print("** class doesn't exist **")
            else:
                for each in obj_dict.keys():
                    if arg in each:
                        cnt += 1
                print(cnt)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change to the JSON file
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Ex: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        obj_dict = models.storage.all()

        if len(arg) == 0:
            print("** class name missing **")
        else:
            tokens = arg.split()

            if tokens[0] not in HBNBCommand.__my_classes:
                print("** class doesn't exist **")
            elif len(tokens) == 1:
                print("** instance id missing **")
            elif (tokens[0] + '.' + tokens[1]) not in obj_dict:
                print("** no instance found **")
            elif len(tokens) == 2:
                print("** attribute name missing **")
            elif len(tokens) == 3:
                print("** value missing **")
            else:
                obj = obj_dict[tokens[0] + '.' + tokens[1]]
                if tokens[2] in obj.__class__.__dict__.keys():
                    v_type = type(obj.__class__.__dict__[tokens[2]])
                    obj.__dict__[tokens[2]] = (v_type(tokens[3]))
                else:
                    obj.__dict__[tokens[2]] = tokens[3]
                models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()

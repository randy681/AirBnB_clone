#!/usr/bin/python3
'''this module for the console app'''


import cmd
import sys
import shlex
import re
import ast
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''HBNB Command Prompt class'''

    # determines prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    # available classes that can be created
    classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }

    attr_types = {
             'number_rooms': int, 'number_bathrooms': int,
             'max_guest': int, 'price_by_night': int,
             'latitude': float, 'longitude': float
            }

    def preloop(self):
        """Prints the prompt when isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """This function gets the line before it gets processed
        and here we can reformat command line for the dot.command syntax.
        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in usage example.)
        """
        cmd = cls = id = args = new_line = ''

        # check if the line has normal commands and
        # dosen't need reformatting
        if not ('.' in line and '(' in line and ')' in line):
            splt_line = shlex.split(line)
            if len(splt_line) > 3:
                final_line = '{} {} {} {}'.format(splt_line[0],
                                                  splt_line[1],
                                                  splt_line[2],
                                                  ' '.join(
                                                           ('"' + r + '"')
                                                           for r in
                                                           splt_line[3:]
                                                           ))
            else:
                return line
        # use this string as a refernece to the regex
        # User.update(id, {"first_name":"elmahdi", "email":"test@alx.com"})
        # this finds the class name from the start
        # of the line to the first dot it encounters [User.]
        cls = re.search(r".+?\.", line)
        # this finds the command from the first
        # dot it encounters to the first left brace [.update(]
        cmd = re.search(r"\..+?\(", line)
        # checking if one of them is not found then syntax is wrong
        if not cls or not cmd:
            # so i just return the line as it is and the
            # cmd class will return a syntax error
            return line

        cls = cls.group(0)[:-1]  # changing [User.] to [User]
        cmd = cmd.group(0)[1:-1]  # changing [.update(] to [update]
        # this searchs for the id in both cases where
        # there will be just the id as arguments like
        # User.show(id)
        # and when there is more arguments after the id
        # like in the update function
        id = re.search(r"\(.+?\,|\(.+?\)", line)  # finds [(id,]
        if id:
            id = id.group(0)[1:-1]  # change [(id,] to [id]
        else:
            # if not found make it empty string
            # because this will be used later
            id = ''

        # this finds the rest of arguments either are normal arguments
        # or a dictionary they will always be between a comman "," and a ")"
        # this find [, {"first_name":"elmahdi", "email":"test@alx.com"})]
        args = re.search(r",.+?\)", line)
        evl_dict = ''
        if args:
            # change [, {"first_name":"elmahdi", "email":"test@alx.com"})]
            # to [{"first_name":"elmahdi", "email":"test@alx.com"}]
            args = args.group(0)[1:-1].strip()
            try:
                # trying to cast it to a dict
                evl_dict = ast.literal_eval(args)
            except Exception:
                pass  # means it's not a dict
            # if not dict so args are normal args separated with commas
            if not isinstance(evl_dict, dict):
                # i split on commas and join them back with space
                args = ' '.join(args.split(','))
        # if nor arguments found by the regex means there is not args
        else:
            # store an empty string in it cuz this var will be used later
            args = ''
        # refomating the line to the normal way
        new_line = "{} {} {} {}".format(cmd,
                                        cls.strip("\"'"),
                                        id.strip("\"'"),
                                        args)
        # so this
        # User.update(id, {"first_name":"elmahdi", "email":"test@alx.com"})
        # will become this
        # update User id {"first_name":"elmahdi", "email":"test@alx.com"}
        return new_line

    def postcmd(self, stop, line):
        """Prints the prompt when isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def emptyline(self):
        ''' overrides the bhavior of an empty line'''
        pass

    def do_quit(self, arg):
        '''method for the quit command'''
        exit()

    def help_quit(self):
        '''prints the documentation for the command quit'''
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        '''method that handles the EOF and exit the program'''
        print()
        exit()

    def help_EOF(self):
        """ Prints the documentation for EOF """
        print("The EOF exits the program\n")

    def do_create(self, arg):
        ''' creates a new instance of the class passed as argument
            and saves it to the json storage file
        '''
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        storage.save()
        print(new_instance.id)

    def help_create(self):
        """ prints Documentation for the create command """
        print("creates a new instance of the class passed as argument")
        print("[Usage]: create <className>\n")

    def do_show(self, arg):
        ''' prints the string representation of an instance
            based on the class name and id
        '''
        args = shlex.split(arg)

        if len(args) >= 1:
            cls = args[0]
        else:
            print("** class name missing **")
            return
        if cls not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) >= 2:
            id = args[1]
        else:
            print("** instance id missing **")
            return

        key = cls + '.' + id
        all = storage.all()
        if key not in all:
            print("** no instance found **")
            return
        print(all[key])

    def help_show(self):
        """ prints documentation for the show command """
        print("prints the string representation of an instance")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, arg):
        ''' Deletes an instance based on the class name and id
            and saves the change into the JSON Storage file
        '''
        args = shlex.split(arg)

        if len(args) >= 1:
            cls = args[0]
        else:
            print("** class name missing **")
            return
        if cls not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) >= 2:
            id = args[1]
        else:
            print("** instance id missing **")
            return

        key = cls + '.' + id
        all = storage.all()
        if key not in all:
            print("** no instance found **")
            return

        del (all[key])
        storage.save()

    def help_destroy(self):
        ''' prints documentaion for the destroy command '''
        print("Deletes an instance based on the class name and id")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, arg):
        ''' Prints all string representation of all instances
            based or not on the class name.
        '''
        arg = arg.strip("\"'")
        result = []
        all = storage.all()
        if not arg:
            for key in all.keys():
                result.append(all[key].__str__())
            print(result)
            return

        for key in all.keys():
            if key.find(arg) != -1 and arg in self.classes:
                result.append(all[key].__str__())
        if len(result) <= 0 and arg not in self.classes:
            print("** class doesn't exist **")
            return
        print(result)

    def help_all(self):
        ''' prints documentaion for the all command '''
        print("Prints all string representation of all instances")
        print("based or not on the class name")
        print("[Usage]: all <className>\n")

    def do_update(self, arg):
        '''  Updates an instance based on the class name
            and id by adding or updating attribute and saves
            the change into the JSON Storage file
        '''
        args = shlex.split(arg)
        cls = id = attr = val = ''

        if len(args) >= 1:
            cls = args[0]
        else:
            print("** class name missing **")
            return
        if cls not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) >= 2:
            id = args[1]
        else:
            print("** instance id missing **")
            return
        key = cls + '.' + id
        if key not in storage.all():
            print("** no instance found **")
            return

        arg_section = ''
        if len(args) >= 3:
            arg_section = arg.split(None, 2)[2]
            evaled_args = ''
            try:
                evaled_args = ast.literal_eval(arg_section)
            except (SyntaxError, ValueError, AssertionError):
                pass

            if isinstance(evaled_args, dict):
                arg_section = evaled_args
            else:
                attr = args[2]
        else:
            print("** attribute name missing **")
            return
        if len(args) >= 4:
            if not isinstance(arg_section, dict):
                val = args[3]
        else:
            print("** value missing **")
            return

        obj = storage.all()[key]
        if isinstance(arg_section, dict):
            # type cast the value depends on the attribute
            for key in arg_section.keys():
                if key in self.attr_types:
                    arg_section[key] = self.attr_types[key](arg_section[key])
            # update the object attributes dictionary
            obj.__dict__.update(arg_section)
        else:
            # type cast the value depends on the attribute
            if attr in self.attr_types:
                val = self.attr_types[attr](val)
            new_attr = {attr: val}
            # update the object attributes  dictionary
            obj.__dict__.update(new_attr)
        obj.save()

    def help_update(self):
        """ prints Documentation for the update command """
        print("Updates an object's attributes")
        print("Usage: update <className> <id> <attName> <attVal>\n")

    def do_count(self, args):
        """Counts the number of class instances created"""
        count = 0
        for k in storage.all().keys():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """ prints the documentation of the count command"""
        print("Usage: count <class_name>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

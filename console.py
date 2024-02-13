#!/usr/bin/python3
""" Console Module """
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    # ... (previous code remains unchanged)

    def do_create(self, args):
        """ Create an object of any class"""
        try:
            if not args:
                raise SyntaxError()
            arg_list = args.split(" ")
            kw = {}
            for arg in arg_list[1:]:
                arg_splited = arg.split("=")
                arg_splited[1] = eval(arg_splited[1])
                if type(arg_splited[1]) is str:
                    arg_splited[1] = arg_splited[1].replace("_", " ").replace('"', '\\"')
                kw[arg_splited[0]] = arg_splited[1]
        except SyntaxError:
            print("** class name missing **")
            return
        except NameError:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes.get(arg_list[0])
        if new_instance:
            new_instance = new_instance(**kw)
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    # ... (remaining code remains unchanged)

    def do_update(self, args):
        """ Updates a certain object with new info """
        c_name, c_id, att_name, att_val, kwargs = '', '', '', '', ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # class name not present
            print("** class name missing **")
            return

        class_instance = HBNBCommand.classes.get(c_name)
        if not class_instance:
            print("** class doesn't exist **")
            return

        # isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # id not present
            print("** instance id missing **")
            return

        # generate key from class and id
        key = c_name + "." + c_id

        # determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # first determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
        else:  # isolate args
            args = args[2].partition(' ')

            # if att_name was not quoted arg
            att_name = args[0].replace('\"', '')

            # check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)].replace('\"', '')

        # retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # update dictionary with name, value pair
        new_dict.__dict__.update({att_name: att_val})
        new_dict.save()  # save updates to file


if __name__ == "__main__":
    HBNBCommand().cmdloop()

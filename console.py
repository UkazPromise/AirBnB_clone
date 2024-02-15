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
    # ... (existing code)

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it to JSON file and prints the id.
        Usage: create <class_name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id.
        Usage: show <class_name> <id>
        """
        args = arg.split()
        if not args or len(args) == 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            all_objs = storage.all()
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        args = arg.split()
        if not args or len(args) == 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            all_objs = storage.all()
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representations of all
        instances based or not on the class name.
        Usage: all [class_name]
        """
        args = arg.split()
        all_objs = storage.all()
        if not args:
            for obj in all_objs.values():
                print(obj)
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        for key, obj in all_objs.items():
            if key.startswith(class_name):
                print(obj)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        args = arg.split()
        if not args or len(args) == 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) == 3:
            print("** value missing **")
            return
        attr_value = args[3]
        obj = all_objs[key]
        setattr(obj, attr_name, attr_value)
        obj.save()

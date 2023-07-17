#!/usr/bin/python3
"""This program contains the entry point of the command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """the HBNB Command Interpreter.

    Attributes:
        prompt (str): a custom prompt string
    """

    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program.
        """
        return True

    def emptyline(self):
        """Handles empty line input.
        """
        return

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id."""
        if line:
            try:
                cls_to_call = eval(line)
            except (NameError, SyntaxError):
                print("** class doesn't exist **")
                return
            obj = cls_to_call()
            obj.save()
            print(obj.id)
        else:
            print("** class name missing **")

    def help_create(self, line):
        print("Usage: create <classname>",
              "To create an instance of that class", sep='\n')

    def do_show(self, line):
        """Prints the string representation of an instance based on the class
        name and id.
        """
        if line:
            args = line.split()
            try:
                cls = eval(args[0])
            except NameError:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
            else:
                id = args[1]
                key = f"{cls.__name__}.{id}"
                stored_objects = FileStorage().all()
                if key in stored_objects:
                    print(stored_objects[key])
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def help_show(self):
        print("Usage: show <class name> <id>",
              "To print the string representation of an instance based on the"
              "class name and id", sep='\n')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        if line:
            args = line.split()
            try:
                cls = eval(args[0])
            except NameError:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            else:
                id = args[1]
                key = f"{cls.__name__}.{id}"
                stored_objects = FileStorage._FileStorage__objects
                if key in stored_objects:
                    del stored_objects[key]
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def help_destroy(self):
        print("Usage: destroy <class name> <id>",
              "Deletes an instance based on the class name and id",
              sep='\n')

    def do_all(self, line):
        """Prints all string representation of all instances based or not the
        class name.
        """
        stored_objects = FileStorage().all()
        if line:
            try:
                cls = eval(line)
            except (NameError, SyntaxError):
                print("** class doesn't exist **")
                return
            lst = [str(value) for key, value in stored_objects.items() if
                   value.__class__ == cls]
            print(lst)
        else:
            lst = [str(value) for key, value in stored_objects.items()]
            print(lst)

    def help_all(self):
        print("Usage: all <class name> or all",
              "prints all string representation of all instanced based or"
              " not on the class name", sep='\n')

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        if line:
            args = line.split()
            try:
                cls = eval(args[0])
            except NameError:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            else:
                id = args[1]
                key = f"{cls.__name__}.{id}"
                stored_objects = FileStorage._FileStorage__objects
                if key in stored_objects:
                    if len(args) < 3:
                        print("** attribute name missing **")
                    else:
                        if len(args) < 4:
                            print("** value missing **")
                            return
                        stripped = args[3].strip('"')
                        obj = stored_objects[key]
                        try:
                            attr_type = type(getattr(obj, args[2]))
                        except AttributeError:
                            setattr(obj, args[2], stripped)
                        else:
                            setattr(obj, args[2], attr_type(stripped))
                        storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def help_update(self):
        print("Usage: update <class name> <id> <attribute name> \"<attribute"
              "value>\"", "Updates an instance based on the class name and id"
              "by adding or updating attributes")

    def do_EOF(self, line):
        """Handles end-of-file marker."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

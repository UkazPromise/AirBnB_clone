#!/usr/bin/python3
""" Module for testing file storage"""
import json
import shlex
from models.user import User
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review,
    }

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if partition[0] == cls.__name__:
                    dic[key] = self.__objects[key]
            return dic
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value["__class__"]
                    if class_name in self.__objects:
                        value = self.__objects[class_name](**value)
                        self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ calls reload()
        """
        self.reload()

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up the test environment."""
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Remove the storage file at the end of tests."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_objects_empty(self):
        """__objects is initially empty."""
        self.assertEqual(len(storage.all()), 0)

    def test_new_object_added(self):
        """New object is correctly added to __objects."""
        new_instance = BaseModel()
        stored_objects = storage.all()
        self.assertIn(new_instance, stored_objects.values())

    def test_all_returns_dict(self):
        """__objects is properly returned as a dictionary."""
        stored_objects = storage.all()
        self.assertIsInstance(stored_objects, dict)

    def test_base_model_save_does_not_create_file(self):
        """File is not created on BaseModel save."""
        new_instance = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_save_method_creates_file(self):
        """FileStorage save method."""
        new_instance = BaseModel()
        storage.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload_loads_to_objects(self):
        """Storage file is successfully loaded to __objects."""
        new_instance = BaseModel()
        storage.save()
        storage.reload()
        loaded_instance = storage.all().values()
        self.assertEqual(new_instance.to_dict()['id'], loaded_instance.to_dict()['id'])

    # ... (other test methods)

if __name__ == '__main__':
    unittest.main()

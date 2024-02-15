#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import os
from models.base_model import BaseModel
from models import storage


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

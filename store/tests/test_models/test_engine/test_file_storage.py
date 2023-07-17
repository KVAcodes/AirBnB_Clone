#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""

import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""
    @classmethod
    def setUpClass(cls):
        cls.bm = BaseModel()

    def test_1_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_2_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        self.assertTrue(f"{self.bm.__class__.__name__}.{self.bm.id}"
                        in models.storage.all())

    def test_3_save(self):
        models.storage.save()
        with open("file.json", "r") as json_file:
            save_text = json_file.read()
            self.assertIn("BaseModel." + self.bm.id, save_text)

    def test_4_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_5_reload(self):
        models.storage.reload()
        objs = models.storage.all()
        self.assertIn("BaseModel." + self.bm.id, objs)

    def test_6_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

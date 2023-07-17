#!/usr/bin/python3
"""This module contains the TestCases for the FileStorage class.
"""

import json
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class Test_FileStorage_Instantiation_and_attr(unittest.TestCase):
    """TestCase for the instantiation of the FileStorage objects and
    the private attributes contained.
    """
    
    def test_instantiation_with_args(self):
        """Tests the FIleStorage class for instantiation with args.
        """
        with self.assertRaises(TypeError):
            f_model = FileStorage('args')
    
    def test_private_attr(self):
        """Tests if the private attributes exists.
        """
        self.assertTrue(type(FileStorage._FileStorage__objects) is dict)
        self.assertTrue(type(FileStorage._FileStorage__file_path) is str)

class Test_FileStorage_Methods(unittest.TestCase):
    """TestCase for the methods of the FileStorage class.
    """
        
    @classmethod
    def setUpClass(cls):
        """Executes the block of code in it before all the tests are
        carried out.
        """
        cls.bm = BaseModel()

    def test_1_all_and_new(self):
        """Tests the all and new method of the FileStorage class.
        Note: the new method is called implicitly in the BaseModel's class'
              __init__ method.
        """
        objs = models.storage.all()
        self.assertTrue(type(objs) is dict)
        self.assertTrue(f"{self.bm.__class__.__name__}.{self.bm.id}" in objs)
    
    def test_2_save(self):
        """Tests the save method in the FileStorage class.
        Note: the save method in the FileStorage class is called implicitly
              in the BaseModel's save method.
        """
        models.storage.save()
        with open('file.json', 'r') as json_file:
            o_dict = json.load(json_file)
        self.assertTrue(f"{self.bm.__class__.__name__}.{self.bm.id}" in o_dict)

    def test_3_reload(self):
        """Tests if the reload method in the FileStorage class.
        """
        models.storage.reload()
        self.assertTrue(f"{self.bm.__class__.__name__}.{self.bm.id}" in 
                        models.storage.all())


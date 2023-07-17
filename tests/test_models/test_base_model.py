#!/usr/bin/python3
"""This module contains the unittest of the BaseModel class.
"""


import unittest
import pep8
import re
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO
import datetime


class TestBaseModelModule(unittest.TestCase):
    """Testcase for the base_model.py and test_base_model.py modules."""

    def test_pep8_conformance_base_model(self):
        """Tests if base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/base_model.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base_model(self):
        """Tests if test_base_model.py conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["tests/test_models/"
                                        "test_base_model.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestBaseModel(unittest.TestCase):
    """Testcase for the BaseModel class.
    """

    @classmethod
    def setUpClass(cls):
        """Executes the contained code before any test is run.
        """
        cls.test_model_a = BaseModel()

    # Public instance attributes
    def test_id(self):
        """Tests if uuid is generated and assigned to id for
        every instance created.
        """
        self.assertRegex(self.test_model_a.id, ".{8}-.{4}-.{4}-.{4}-.{12}")

    def test_created_and_updated_at(self):
        """Tests the created_at and updated_at attributes to see they are
        instantiated with the current datetime.
        """
        test_model_1 = BaseModel()
        diff = datetime.datetime.now() - test_model_1.created_at
        self.assertTrue(diff.total_seconds() < 1)
        diff = datetime.datetime.now() - test_model_1.updated_at
        self.assertTrue(diff.total_seconds() < 1)

    def test_str(self):
        """Tests string representation of the BaseModel object i.e
        "[{self.__class__.__name__}] ({self.id}) {self.__dict__}" is correct
        and gets printed out accurately.
        """
        with patch('sys.stdout', StringIO()) as fake_out:
            print(self.test_model_a)
            str_rep = fake_out.getvalue()
            self.assertIn("[BaseModel]", str_rep)
            self.assertIn("created_at", str_rep)
            self.assertIn("updated_at", str_rep)
            self.assertIn("id", str_rep)

    def test_save(self):
        """Tests if the save method updates the public instance attribute
        updated_at with the current datetime.
        """
        self.test_model_a.save()
        diff = datetime.datetime.now() - self.test_model_a.created_at
        self.assertTrue(diff.total_seconds() < 1)

    def test_to_dict(self):
        """Tests the to_dict method and all it's requirements.
        """
        tmp_dict = self.test_model_a.to_dict()
        self.assertEqual(tmp_dict['__class__'], "BaseModel")
        self.assertRegex(tmp_dict['updated_at'], ".{4}-.{2}-.{5}:.{2}:.{9}")
        self.assertRegex(tmp_dict['id'], ".{8}-.{4}-.{4}-.{4}-.{12}")
        self.assertRegex(tmp_dict['created_at'], ".{4}-.{2}-.{5}:.{2}:.{9}")

    def test_kwargs(self):
        """Tests the use of keyword arguments in the instantiation of BaseModel
        objects and the re-creation of instances from dictionary
        representations.
        """
        test_model_2 = BaseModel()
        test_model_3 = BaseModel(**test_model_2.to_dict())
        self.assertTrue(test_model_2.id == test_model_3.id)
        self.assertTrue(test_model_2.created_at == test_model_3.created_at)
        self.assertTrue(test_model_2.updated_at == test_model_3.updated_at)

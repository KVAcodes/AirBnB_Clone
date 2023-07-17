#!/usr/bin/python3
"""This module contains the Testcase of the BaseModel class.
"""

import unittest
import datetime
import sys
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This class is a Testcase for the BaseModel class.
    """
    @classmethod
    def setUpClass(cls):
        """Executes a block of code before the tests begin.
        """
        cls.model_1 = BaseModel()

    def test_id_is_str(self):
        """Tests if the id attribute is a string.
        """
        self.assertIs(type(self.model_1.id), str)

    def test_id_is_uuid4(self):
        """Tests if the id attribute of the objects are
        instantiated with the uuid4 id string.
        """

        self.assertRegex(self.model_1.id, ".{8}-.{4}-.{4}-.{4}-.{12}")

    def test_created_at_and_updated_at(self):
        """Tests if the created_at and updated_at attributes are equal
        when an object is created initially.
        """

        self.assertEqual(self.model_1.created_at, self.model_1.updated_at)

    def test_str(self):
        """Test the string representation of a BaseModel object as it gets
        printed to stdout
        """
        with patch('sys.stdout', StringIO()) as fake_out:
            print(self.model_1)
            print_output = fake_out.getvalue()
            exp_out = (
                f"[{self.model_1.__class__.__name__}] ({self.model_1.id})"
                f" {self.model_1.__dict__}\n"
            )
            self.assertEqual(exp_out, print_output)

    def test_save(self):
        """Tests that the save method updates the 'updated_at' with
        the current datetime."""
        self.model_1.save()
        diff = datetime.datetime.now() - self.model_1.updated_at

        self.assertTrue(diff.seconds < 1)

    def test_to_dict(self):
        """Tests the to_dict method. also checks the __dict__ built-in
        is not modified in-place.
        """

        new_dict = self.model_1.to_dict()
        self.assertNotEqual(new_dict, self.model_1.__dict__)
        self.assertIn('__class__', new_dict)
        self.assertEqual(new_dict['__class__'],
                         self.model_1.__class__.__name__)
        self.assertTrue(type(new_dict['created_at']) == str and
                        type(new_dict['updated_at']) == str)

    def test_init_args_and_kwargs(self):
        """Test the creation of an instance using args and kwargs.
        """
        json = self.model_1.to_dict()
        new_model = BaseModel(**json)
        self.assertNotIn('__class__', new_model.__dict__)
        self.assertTrue(type(new_model.__dict__['created_at']) ==
                        datetime.datetime)
        new_model2 = BaseModel('foo', 'foobar')
        self.assertTrue(hasattr(new_model2, "id"))
        self.assertTrue(hasattr(new_model2, "created_at"))
        self.assertTrue(hasattr(new_model2, "updated_at"))


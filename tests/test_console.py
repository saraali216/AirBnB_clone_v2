#!/usr/bin/python3
"""test module"""
import unittest
import console
from unittest.mock import patch
from io import StringIO
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage
import os


class TestHBNBCommand(unittest.TestCase):
    """Test HBNBCommand class"""

    def setUp(self):
        """Set up test environment"""
        self.HBNBCommand = console.HBNBCommand()

    def tearDown(self):
        """Clean up test environment"""
        del self.HBNBCommand

    def test_help_method(self):
        """Test the help method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNBCommand.onecmd("help quit")
            self.assertEqual("Quit command to exit the program.", f.getvalue()[:-1])

    def test_create(self):
        """Test the create method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNBCommand.onecmd("create")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])

    def test_show(self):
        """Test the show method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNBCommand.onecmd("show")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])

    def test_destroy(self):
        """Test the destroy method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNBCommand.onecmd("destroy")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])

    def test_count(self):
        """Test the count method"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.HBNBCommand.onecmd("count")
            self.assertEqual("** class name missing **", f.getvalue()[:-1])


if __name__ == "__main__":
    unittest.main()

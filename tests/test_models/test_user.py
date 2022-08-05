#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
        TestUser_init
        TestUser_save
        TestUser_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_init(unittest.TestCase):
    """Tests for instatntiation of User class."""

    def test_init_with_no_args(self):
        self.assertEqual(type(User()), User)

    def test_new_instance_in_objects(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(type(User().id), str)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(type(User().created_at), datetime)

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(type(User().updated_at), datetime)

    def test_email_is_public_str(self):
        self.assertEqual(type(User().email), str)

    def test_password_is_public_str(self):
        self.assertEqual(type(User().password), str)

    def test_first_name_is_public_str(self):
        self.assertEqual(type(User().first_name), str)

    def test_last_name_is_public_str(self):
        self.assertEqual(type(User().last_name), str)

    def test_two_users_unique_id(self):
        user_1 = User()
        user_2 = User()
        self.assertNotEqual(user_1.id, user_2.id)

    def test_two_users_created_at_different(self):
        user_1 = User()
        sleep(0.05)
        user_2 = User()
        self.assertLess(user_1.created_at, user_2.created_at)

    def test_two_users_updated_at_different(self):
        user_1 = User()
        sleep(0.05)
        user_2 = User()
        self.assertLess(user_1.updated_at, user_2.updated_at)

    def test_str_repr(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        user_1 = User()
        user_1.id = "123456"
        user_1.created_at = user_1.updated_at = dt
        user_1_str = user_1.__str__()
        self.assertIn("[User] (123456)", user_1_str)
        self.assertIn("'id': '123456'", user_1_str)
        self.assertIn("'created_at': " + dt_repr, user_1_str)
        self.assertIn("'updated_at': " + dt_repr, user_1_str)

    def test_unused_args(self):
        user_1 = User(None)
        self.assertNotIn(None, user_1.__dict__.values())

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)


class TestUser_save(unittest.TestCase):
    """Tests for save method of the class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_different_updated_at_after_save(self):
        user_1 = User()
        sleep(0.05)
        prior_updated_at = user_1.updated_at
        user_1.save()
        self.assertLess(prior_updated_at, user_1.updated_at)

    def test_save_with_None_arg(self):
        user_1 = User()
        with self.assertRaises(TypeError):
            user_1.save(None)

    def test_save_updates_file_with_user(self):
        user_1 = User()
        user_1.save()
        user_1_id = "User." + user_1.id
        with open("file.json", "r") as f:
            self.assertIn(user_1_id, f.read())


class TestUser_to_dict(unittest.TestCase):
    """Tests for to_dict method of the class."""

    def test_to_dict_type(self):
        self.assertTrue(type(User().to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        user_1 = User()
        self.assertIn("id", user_1.to_dict())
        self.assertIn("created_at", user_1.to_dict())
        self.assertIn("updated_at", user_1.to_dict())
        self.assertIn("__class__", user_1.to_dict())

    def test_to_dict_contains_added_attrs(self):
        user_1 = User()
        user_1.pet_name = "Danny"
        user_1.phone = 234
        self.assertEqual(user_1.pet_name, "Danny")
        self.assertIn("phone", user_1.to_dict())

    def test_to_dict_datetime_attrs_are_str(self):
        user_1 = User()
        user_1_dict = user_1.to_dict()
        self.assertEqual(type(user_1_dict["created_at"]), str)
        self.assertEqual(type(user_1_dict["updated_at"]), str)

    def test_contrast_to_dict_dunder_dict(self):
        user_1 = User()
        self.assertNotEqual(user_1.to_dict(), user_1.__dict__)

    def test_to_dict_with_None_arg(self):
        user_1 = User()
        with self.assertRaises(TypeError):
            user_1.to_dict(None)


if __name__ == "__main__":
    unittest.main()

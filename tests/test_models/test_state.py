#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_init
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_init(unittest.TestCase):
    """Tests for instantiation of State class."""

    def test_init_with_no_args(self):
        self.assertEqual(type(State()), State)

    def test_new_instance_in_objects(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(type(State().id), str)

    def test_created_at_is_public_datetime(self):
        self.assertEqual(type(State().created_at), datetime)

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(type(State().updated_at), datetime)

    def test_name_is_public_class_str(self):
        state_1 = State()
        self.assertEqual(type(State.name), str)
        self.assertIn("name", dir(state_1))

    def test_two_states_unique_id(self):
        state_1 = State()
        state_2 = State()
        self.assertNotEqual(state_1, state_2)

    def test_two_states_different_created_at(self):
        state_1 = State()
        sleep(0.05)
        state_2 = State()
        self.assertLess(state_1.created_at, state_2.created_at)

    def test_two_states_different_updated_at(self):
        state_1 = State()
        sleep(0.05)
        state_2 = State()
        self.assertLess(state_1.updated_at, state_2.updated_at)

    def test_str_repr(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        state_1 = State()
        state_1.id = "123456"
        state_1.created_at = state_1.updated_at = dt
        state_1_str = state_1.__str__()
        self.assertIn("[State] (123456)", state_1_str)
        self.assertIn("'id': '123456'", state_1_str)
        self.assertIn("'created_at': " + dt_repr, state_1_str)
        self.assertIn("'updated_at': " + dt_repr, state_1_str)

    def test_unused_args(self):
        state_1 = State(None)
        self.assertNotIn(None, state_1.__dict__.values())

    def test_init_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
    """Tests for save method of the State class."""

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
        state_1 = State()
        sleep(0.05)
        prior_updated_at = state_1.updated_at
        state_1.save()
        self.assertLess(prior_updated_at, state_1.updated_at)

    def test_save_with_None_arg(self):
        state_1 = State()
        with self.assertRaises(TypeError):
            state_1.save(None)

    def test_save_updates_file_with_state(self):
        state_1 = State()
        state_1.save()
        state_1_id = "State." + state_1.id
        with open("file.json", "r") as f:
            self.assertIn(state_1_id, f.read())


class TestState_to_dict(unittest.TestCase):
    """Tests for to_dict method of State class."""

    def test_to_dict_type(self):
        self.assertEqual(type(State().to_dict()), dict)

    def test_to_dict_contains_correct_keys(self):
        state_1 = State()
        self.assertIn("id", state_1.to_dict())
        self.assertIn("created_at", state_1.to_dict())
        self.assertIn("updated_at", state_1.to_dict())
        self.assertIn("__class__", state_1.to_dict())

    def test_to_dict_contains_added_attrs(self):
        state_1 = State()
        state_1.pet_name = "Dan"
        state_1.phone = "123456"
        self.assertEqual(state_1.pet_name, "Dan")
        self.assertIn("phone", state_1.to_dict())

    def test_to_dict_datetime_attrs_are_str(self):
        state_1 = State()
        state_1_dict = state_1.to_dict()
        self.assertEqual(type(state_1_dict["created_at"]), str)
        self.assertEqual(type(state_1_dict["updated_at"]), str)

    def test_contrast_to_dict_dunder_dict(self):
        state_1 = State()
        self.assertNotEqual(state_1.to_dict(), state_1.__dict__)

    def test_to_dict_with_None_arg(self):
        state_1 = State()
        with self.assertRaises(TypeError):
            state_1.to_dict(None)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
""" """
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestCaseReview(unittest.TestCase):
    """Test cases for Review class."""

    def test_instance(self):
        """Test for creating an instance of Review"""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_is_class(self):
        """Test if Review is a class"""
        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")

    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        review = Review()
        self.assertTrue(issubclass(type(review), BaseModel))

    def test_place_id(self):
        """Test if place_id can be set and retrieved correctly"""
        review = Review()
        self.assertEqual(review.place_id, "")
        review.place_id = ""
        self.assertEqual(review.place_id, "")

    def test_user_id(self):
        """Test if user_id can be set and retrieved correctly"""
        review = Review()
        self.assertEqual(review.user_id, "")
        review.user_id = ""
        self.assertEqual(review.user_id, "")

    def test_text(self):
        """Test if text can be set and retrieved correctly"""
        review = Review()
        self.assertEqual(review.text, "")
        review.text = ""
        self.assertEqual(review.text, "")

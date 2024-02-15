#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUser(test_basemodel):
    """Test class for User model."""

    def __init__(self, *args, **kwargs):
        """Initialize the test class."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def setUp(self):
        """Set up a common instance for tests."""
        self.new_user = self.value()

    def test_first_name_type(self):
        """Test that first_name attribute is of type str."""
        self.assertEqual(type(self.new_user.first_name), str)

    def test_last_name_type(self):
        """Test that last_name attribute is of type str."""
        self.assertEqual(type(self.new_user.last_name), str)

    def test_email_type(self):
        """Test that email attribute is of type str."""
        self.assertEqual(type(self.new_user.email), str)

    def test_password_type(self):
        """Test that password attribute is of type str."""
        self.assertEqual(type(self.new_user.password), str)


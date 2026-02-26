# tests/test_validator.py
import unittest
from src.validator import validate_date, validate_time

class TestValidator(unittest.TestCase):

    def test_valid_date(self):
        self.assertTrue(validate_date("2026-02-25"))
        self.assertFalse(validate_date("2026-02-30"))

    def test_valid_time(self):
        self.assertTrue(validate_time("14:30"))
        self.assertFalse(validate_time("25:00"))

if __name__ == "__main__":
    unittest.main()
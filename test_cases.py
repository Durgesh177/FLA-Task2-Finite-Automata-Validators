"""Unit tests: at least five accepted and five rejected cases per DFA."""

import unittest

from atm_pin_validator import validate_pin
from password_validator import validate_password
from email_validator import validate_email


class TestATMPinDFA(unittest.TestCase):
    def test_accepted_pins(self):
        for value in ["1234", "0000", "2580", "9071", "0042"]:
            with self.subTest(value=value):
                self.assertTrue(validate_pin(value))

    def test_rejected_pins(self):
        for value in ["123", "12345", "12A4", "12 4", ""]:
            with self.subTest(value=value):
                self.assertFalse(validate_pin(value))


class TestPasswordDFA(unittest.TestCase):
    def test_accepted_passwords(self):
        for value in [
            "Abcdef1@", "Hello123#", "A1bcdef$", "XyZ9876&", "Secure2026@a"
        ]:
            with self.subTest(value=value):
                self.assertTrue(validate_password(value))

    def test_rejected_passwords(self):
        for value in [
            "Ab1@", "abcdefgh1@", "ABCDEFGH1@", "Abcdefgh@", "Abcdefg1"
        ]:
            with self.subTest(value=value):
                self.assertFalse(validate_password(value))


class TestEmailDFA(unittest.TestCase):
    def test_accepted_emails(self):
        for value in [
            "ben@gmail.com",
            "user1@site.in",
            "abc123@domain.org",
            "A9@X2.co",
            "student2026@univ.edu",
        ]:
            with self.subTest(value=value):
                self.assertTrue(validate_email(value))

    def test_rejected_emails(self):
        for value in [
            "@gmail.com",
            "usergmail.com",
            "user@.com",
            "user@domain.c",
            "user@domain.c0m",
        ]:
            with self.subTest(value=value):
                self.assertFalse(validate_email(value))


if __name__ == "__main__":
    unittest.main(verbosity=2)

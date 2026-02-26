# tests/test_appointment.py
import unittest
from src.appointment import Appointment

class TestAppointment(unittest.TestCase):

    def test_to_dict(self):
        app = Appointment("001", "John Doe", "2026-02-25", "10:00", "Consultation")
        self.assertEqual(app.to_dict()['student_name'], "John Doe")

    def test_str(self):
        app = Appointment("001", "John Doe", "2026-02-25", "10:00", "Consultation")
        self.assertIn("John Doe", str(app))

if __name__ == "__main__":
    unittest.main()
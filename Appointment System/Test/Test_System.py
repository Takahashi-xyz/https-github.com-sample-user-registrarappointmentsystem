# tests/test_system.py
import unittest
from src.appointment_system import RegistrarAppointmentSystem

class TestRegistrarSystem(unittest.TestCase):

    def setUp(self):
        self.system = RegistrarAppointmentSystem()
        self.system.appointments = []  # start fresh

    def test_add_appointment(self):
        success, msg = self.system.add_appointment("001", "Alice", "2026-02-25", "09:00", "Query")
        self.assertTrue(success)
        self.assertEqual(len(self.system.appointments), 1)

    def test_duplicate_id(self):
        self.system.add_appointment("001", "Alice", "2026-02-25", "09:00", "Query")
        success, msg = self.system.add_appointment("001", "Bob", "2026-02-26", "10:00", "Info")
        self.assertFalse(success)

    def test_update_appointment(self):
        self.system.add_appointment("002", "Charlie", "2026-02-26", "11:00", "Check")
        success, msg = self.system.update_appointment("002", time="12:00")
        self.assertTrue(success)
        self.assertEqual(self.system.appointments[0].time, "12:00")

    def test_delete_appointment(self):
        self.system.add_appointment("003", "Diana", "2026-02-27", "14:00", "Issue")
        success, msg = self.system.delete_appointment("003")
        self.assertTrue(success)
        self.assertEqual(len(self.system.appointments), 0)

if __name__ == "__main__":
    unittest.main()
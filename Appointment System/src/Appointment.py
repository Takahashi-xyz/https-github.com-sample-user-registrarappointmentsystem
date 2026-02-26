# src/appointment.py
class Appointment:
    """Represents a single student appointment."""

    def __init__(self, id, student_name, date, time, purpose):
        self.id = id
        self.student_name = student_name
        self.date = date
        self.time = time
        self.purpose = purpose

    def to_dict(self):
        """Convert appointment to dictionary for JSON storage."""
        return {
            "id": self.id,
            "student_name": self.student_name,
            "date": self.date,
            "time": self.time,
            "purpose": self.purpose
        }

    def __str__(self):
        return f"ID: {self.id} | Student: {self.student_name:<15} | Date: {self.date} | Time: {self.time} | Purpose: {self.purpose}"
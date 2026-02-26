# src/appointment_system.py
import json
import os
from .Appointment import Appointment
from .Validator import validate_date, validate_time

DATA_FILE = "appointments.json"

class RegistrarAppointmentSystem:
    """Core subsystem for managing appointments."""

    def __init__(self):
        self.appointments = []
        self.load_data()

    # -------------------
    # Data Persistence
    # -------------------
    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    data = json.load(f)
                    self.appointments = [Appointment(**a) for a in data]
                print(f"Loaded {len(self.appointments)} appointments.")
            except json.JSONDecodeError:
                print("JSON file corrupted. Starting fresh.")
                self.appointments = []
        else:
            print("No existing appointments. Starting new system.")

    def save_data(self):
        with open(DATA_FILE, 'w') as f:
            json.dump([a.to_dict() for a in self.appointments], f, indent=4)

    # -------------------
    # CRUD Operations
    # -------------------
    def add_appointment(self, id, student_name, date, time, purpose):
        if any(a.id == id for a in self.appointments):
            return False, "Appointment ID already exists."
        if not validate_date(date):
            return False, "Invalid date format."
        if not validate_time(time):
            return False, "Invalid time format."
        self.appointments.append(Appointment(id, student_name, date, time, purpose))
        self.save_data()
        return True, "Appointment added successfully."

    def view_all_appointments(self):
        return sorted(self.appointments, key=lambda x: (x.date, x.time))

    def search_appointment(self, query):
        query = query.lower()
        return [a for a in self.appointments if query in a.id.lower() or query in a.student_name.lower()]

    def update_appointment(self, id, student_name=None, date=None, time=None, purpose=None):
        appointment = next((a for a in self.appointments if a.id == id), None)
        if not appointment:
            return False, "Appointment not found."
        if student_name:
            appointment.student_name = student_name
        if date and validate_date(date):
            appointment.date = date
        if time and validate_time(time):
            appointment.time = time
        if purpose:
            appointment.purpose = purpose
        self.save_data()
        return True, "Appointment updated successfully."

    def delete_appointment(self, id):
        appointment = next((a for a in self.appointments if a.id == id), None)
        if not appointment:
            return False, "Appointment not found."
        self.appointments.remove(appointment)
        self.save_data()
        return True, "Appointment deleted successfully."
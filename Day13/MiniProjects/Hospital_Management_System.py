from abc import ABC, abstractmethod

# Abstract class
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"{self.get_role()}: {self.name}, Age: {self.age}"

# Doctor class
class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def get_role(self):
        return "Doctor"

    def __str__(self):
        return super().__str__() + f", Specialization: {self.specialization}"

# Patient class
class Patient(Person):
    def __init__(self, name, age, symptoms):
        super().__init__(name, age)
        self.symptoms = symptoms

    def get_role(self):
        return "Patient"

    def __str__(self):
        return super().__str__() + f", Symptoms: {self.symptoms}"

# Prescription class
class Prescription:
    def __init__(self, patient, doctor, medicine):
        self.patient = patient
        self.doctor = doctor
        self.medicine = medicine

    def __str__(self):
        return f"Prescription for {self.patient.name} by Dr. {self.doctor.name}: {self.medicine}"

# Appointment class aggregates Doctor and Patient
class Appointment:
    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.prescription = None

    def assign_prescription(self, medicine):
        self.prescription = Prescription(self.patient, self.doctor, medicine)

    def __str__(self):
        result = f"Appointment:\n  Patient: {self.patient.name}\n  Doctor: {self.doctor.name}\n  Date: {self.date}"
        if self.prescription:
            result += f"\n  Prescription: {self.prescription.medicine}"
        else:
            result += "\n  Prescription: Not yet assigned"
        return result


"""
# Create doctor and patient
doc1 = Doctor("Dr. Sahana", 45, "Cardiologist")
pat1 = Patient("Ragul", 28, "Chest Pain")

# Book an appointment
appt = Appointment(pat1, doc1, "2025-07-22")
print(appt)

# Generate prescription
appt.assign_prescription("Aspirin 75mg, daily for 7 days")
print("\nAfter Prescription:\n")
print(appt)
"""
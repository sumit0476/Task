from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    # Serialize method to send JSON data


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctor.id"))
    patient_name = db.Column(db.String(100))
    date = db.Column(db.Date)
    # Serialize method to send JSON data

from flask import Flask, request, jsonify
from models import db, Doctor, Appointment

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)


@app.route("/doctors", methods=["GET"])
def get_doctors():
    doctors = Doctor.query.all()
    return jsonify([doctor.serialize() for doctor in doctors])


@app.route("/doctors/<int:doctor_id>", methods=["GET"])
def get_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    return jsonify(doctor.serialize())


@app.route("/doctors/<int:doctor_id>/availability", methods=["GET"])
def check_availability(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    # Implement logic to return availability
    return jsonify(doctor.get_availability())


@app.route("/appointments", methods=["POST"])
def create_appointment():
    data = request.json
    appointment = Appointment(
        doctor_id=data["doctor_id"],
        patient_name=data["patient_name"],
        date=data["date"],
    )
    db.session.add(appointment)
    db.session.commit()
    return jsonify(appointment.serialize()), 201


if __name__ == "__main__":
    app.run(debug=True)

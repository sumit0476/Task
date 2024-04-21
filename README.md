This project implements a simple REST API for an out-patient appointment system where doctors have a weekly schedule and can handle a certain number of patients each evening, except Sundays.

## Technologies Used

- Python with Flask for the backend.
- SQLite for the database using Flask-SQLAlchemy.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
2. Create and activate a virtual environment:
  python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate

3. Install dependencies: pip install -r requirements.txt

4. Initialize the database:
from app import db
db.create_all()


5. Run the application:

## API Endpoints

- `GET /doctors` - Retrieves a list of all doctors.
- `GET /doctors/<id>` - Retrieves detailed information about a specific doctor.
- `GET /doctors/<id>/availability` - Checks the availability of a specific doctor for the upcoming week.
- `POST /appointments` - Books an appointment with a doctor.

## Usage

Here are some example `curl` commands to interact with the API:

- List all doctors: curl -X GET http://localhost:5000/doctors

- Check doctor availability: curl -X POST http://localhost:5000/appointments -H "Content-Type: application/json" -d '{"doctor_id": 1, "patient_name": "John Doe", "date": "2024-04-15"}'





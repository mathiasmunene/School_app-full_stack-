from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from models import db, Course, Student, Enrollment

#..Create a Flask aplication instance
app = Flask(__name__)

# Setup DB resources
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///schools.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db.init_app(app) #Initialize sqlalchemy with your flask app


# Initialize SQLAlchemy first
# db = SQLAlchemy(app)

with app.app_context():
    db.create_all()  # create all non-existent table

# Import models AFTER creating db instance


#CREATE Student
@app.route('/student', methods=["POST"])
def create_student():
    data = request.get_json()
    name=data["name"]
    age=data["age"]
    student=Student(full_name=name, age=age)
    db.session.add(student)
    db.session.commit()
    return jsonify(student.to_dict()), 201

# Read all users
@app.route('/students', methods=["GET"])
def get_students():
    students = Student.query.all()
    students_data = [student.to_dict() for student in students]
    return jsonify(students_data), 200


@app.route('/')
def index():
    return "<p>Hello World</p>"

@app.route('/courses')
def courses():
    return "This is the courses page"

@app.route('/about')
def about():
    return "ABout"

@app.route('/courses/<int:course_id>')
def course_details(course_id):
    return f"This is course: {course_id}"

# @app.route('/courses/<course_id>')
# def course_name(course_id):
#     return f"This is course: {course_id}"

# Path parameters
# @app.route('/courses/<path:course_file>')
# def course_file(course_file):
#     return f'Currently serving: {course_file}'

@app.route('/courses/<path:course_file>')
def course_file(course_file):
    return f'<img src="~/{course_file}">'

@app.route('/chicken')
def chicken():
    return '<img src="https://www.istockphoto.com/vector/scared-cartoon-chicken-gm451537227-25267701" alt="Chicken">'

# Query parameters
@app.route('/course_details')
def course_detail():
    c_name = request.args.get("name")
    c_date = request.args.get("date")
    return f'The course {c_name} was created on {c_date}'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
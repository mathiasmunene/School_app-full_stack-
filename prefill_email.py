from app import app
from models import db, Student

with app.app_context():
    students = Student.query.filter(Student.email == None).all()
    # Logic here
    # load file, check each id, the corresponding email, attach to that student
    for s in students:
        s.email = f"{s.id}@sample.com"
    db.session.commit()
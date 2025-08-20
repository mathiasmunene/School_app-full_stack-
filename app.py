from flask import Flask, request

#..Create a Flask aplication instance
app = Flask(__name__)

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

@app.route('/courses/<course_id>')
def course_name(course_id):
    return f"This is course: {course_id}"
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
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


def calculate_gpa(course_units, grades):

    """
    Calculate the GPA given the course units and grades.
    """

    if not all(0.00<=i<=5.00 for i in grades):
        return jsonify({'error': 'Invalid grade value'})
    total_cu = sum(course_units)

    weighted_points = 0

    for i in range(len(course_units)):

        weighted_points += course_units[i] * grades[i]

    gpa = weighted_points / total_cu

    return round(gpa, 2)


def calculate_cgpa_utme(level, sem, prev_cgpa, gpa):

    cgpa = prev_cgpa #initialize cgpa to the previous cgpa

    if level == 100:

        if sem == 1:

            cgpa = 0

        elif sem == 2:

            cgpa = (prev_cgpa + gpa) / 2

    elif level == 200:

        if sem == 1:

            cgpa = (prev_cgpa * 2 + gpa) / 3

        elif sem == 2:

            cgpa = (prev_cgpa * 3 + gpa) / 4

    elif level == 300:

        if sem == 1:

            cgpa = (prev_cgpa * 4 + gpa)/5

        elif sem == 2:

            cgpa = (prev_cgpa * 5 + gpa)/6

    elif level == 400:

        if  sem == 1:

            cgpa = (prev_cgpa * 6 + gpa)/7

        elif sem == 2:

            cgpa = (prev_cgpa * 7 + gpa)/8

    elif level == 500:

        if sem == 1:

            cgpa = (prev_cgpa * 8 + gpa)/9

        elif sem == 2:

            cgpa = (prev_cgpa * 9 + gpa)/10

    elif level == 600:

        if sem == 1:

            cgpa = (prev_cgpa * 10 + gpa)/11

        elif sem == 2:

            cgpa = (prev_cgpa * 11 + gpa)/12

    return round(cgpa, 2)


def calculate_cgpa_de(level, sem, prev_cgpa, gpa):

    cgpa = prev_cgpa #initialize current cgpa to previous cgpa

    if level == 200:

        if sem == 1:

            cgpa = 0

        elif sem == 2:

            cgpa = (prev_cgpa + gpa) / 2

    elif level == 300:

        if sem == 1:

            cgpa = (prev_cgpa * 2 + gpa) / 3

        elif sem == 2:

            cgpa = (prev_cgpa * 3 + gpa) / 4

    elif level == 400:

        if sem == 1:

            cgpa = (prev_cgpa * 4 + gpa)/5

        elif sem == 2:

            cgpa = (prev_cgpa * 5 + gpa)/6

    elif level == 500:

        if  sem == 1:

            cgpa = (prev_cgpa * 6 + gpa)/7

        elif sem == 2:

            cgpa = (prev_cgpa * 7 + gpa)/8

    elif level == 600:

        if sem == 1:

            cgpa = (prev_cgpa * 8 + gpa)/9

        elif sem == 2:

            cgpa = (prev_cgpa * 9 + gpa)/10            

    return round(cgpa, 2)

@app.route('/generate_result', methods=['POST'])
@cross_origin()
def generate_result():

    data = request.get_json()

    admission_mode = data['admission_mode']

    course_codes = data['course_codes']

    course_units = data['course_units']

    grades = data['grades']

    level = data['level']

    sem = data['sem']

    prev_cgpa = data['prev_cgpa']

    gpa = calculate_gpa(course_units, grades)

    if admission_mode == 'UTME':

        cgpa = calculate_cgpa_utme(level, sem, prev_cgpa, gpa)

    else:

        cgpa = calculate_cgpa_de(level, sem, prev_cgpa, gpa)

    result = {

        'Course Codes': course_codes,

        'Course Units': course_units,

        'Grades': grades,

        'GPA': gpa,

        'CGPA': cgpa

    }

    return jsonify(result)

@app.route('/')
def application_great():
    return 'This application is great!'

@app.route('/add_names')
def add_names():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    full_name = first_name + " " + last_name
    return full_name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


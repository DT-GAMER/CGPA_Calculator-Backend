from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route('/calculate_gpa', methods=['POST'])

def calculate_gpa():

    """

    Calculate the GPA given the course units and grades.

    """

    data = request.get_json()

    course_units = data['course_units']

    grades = data['grades']

    total_cu = sum(course_units)

    weighted_points = 0

    for i in range(len(course_units)):

        weighted_points += course_units[i] * grades[i]

    gpa = weighted_points / total_cu

    return jsonify({'gpa': round(gpa, 2)})

@app.route('/calculate_cgpa_utme', methods=['POST'])

def calculate_cgpa_utme():

    data = request.get_json()

    level = data['level']

    sem = data['sem']

    prev_cgpa = data['prev_cgpa']

    gpa = data['gpa']

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

    return jsonify({'cgpa': round(cgpa, 2)})

@app.route('/calculate_cgpa_de', methods=['POST'])
def calculate_cgpa_de():

    data = request.get_json()

    level = data['level']

    sem = data['sem']

    prev_cgpa = data['prev_cgpa']

    gpa = data['gpa']

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

    return jsonify({'cgpa': round(cgpa, 2)})

@app.route('/generate_result', methods=['POST'])

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

if __name__ == '__main__':

    app.run(debug=True)


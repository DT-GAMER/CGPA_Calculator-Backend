from flask import Flask, request, jsonify

from calculate_gpa import calculate_gpa, calculate_cgpa_utme, calculate_cgpa_de

app = Flask(__name__)

@app.route('/calculate_gpa', methods=['POST'])

def calculate_gpa_route():

    course_units = request.json['course_units']

    grades = request.json['grades']

    gpa = calculate_gpa(course_units, grades)

    return jsonify(gpa=gpa)

@app.route('/calculate_cgpa_utme', methods=['POST'])

def calculate_cgpa_utme_route():

    level = request.json['level']

    sem = request.json['sem']

    prev_cgpa = request.json['prev_cgpa']

    gpa = request.json['gpa']

    cgpa = calculate_cgpa_utme(level, sem, prev_cgpa, gpa)

    return jsonify(cgpa=cgpa)

@app.route('/calculate_cgpa_de', methods=['POST'])

def calculate_cgpa_de_route():

    level = request.json['level']

    sem = request.json['sem']

    prev_cgpa = request.json['prev_cgpa']

    gpa = request.json['gpa']

    cgpa = calculate_cgpa_de(level, sem, prev_cgpa, gpa)

    return jsonify(cgpa=cgpa)

if __name__ == '__main__':

    app.run()

from flask import Flask, jsonify, request

import pandas as pd

app = Flask(__name__)

# function to calculate GPA

def calculate_gpa(cu, gp):

    total_cu = sum(cu)

    weighted_points = [cu[i] * gp[i] for i in range(len(cu))]

    total_weighted_points = sum(weighted_points)

    gpa = total_weighted_points / total_cu

    return round(gpa, 2)

# function to calculate CGPA

def calculate_cgpa(level, sem, prev_cgpa, gpa):

    cgpa = 0

    if level == 100:

        if sem == 1:

            cgpa = gpa

        elif sem == 2:

            cgpa = (prev_cgpa + gpa) / 2

            return round(cgpa, 2)

    elif level == 200:

        if sem == 1:

            cgpa = (prev_cgpa * 2 + gpa) / 3

            return round(cgpa, 2)

        elif sem == 2:

            cgpa = (prev_cgpa * 3 + gpa) / 4

            return round(cgpa, 2)

    elif level == 300:

        if sem == 1:

            cgpa = (prev_cgpa * 4 + gpa)/5

            return round(cgpa, 2)

        elif sem == 2:

            cgpa = (prev_cgpa * 5 + gpa)/6

            return round(cgpa, 2)

    elif level == 400:

        if  sem == 1:

            cgpa = (prev_cgpa * 6 + gpa)/7

            return round(cgpa, 2)

        elif sem == 2:

            cgpa = (prev_cgpa * 7 + gpa)/8

            return round(cgpa, 2)

    elif level == 500:

        if sem == 1:

            cgpa = (prev_cgpa * 8 + gpa)/9

            return round(cgpa, 2)

        elif sem == 2:

            cgpa = (prev_cgpa * 9 + gpa)/10

            return round(cgpa, 2)

    elif level == 600:

        if sem == 1:

            cgpa = (prev_cgpa * 10 + gpa)/11

            return round(cgpa, 2)

        elif sem == 2:

            cgpa = (prev_cgpa * 11 + gpa)/12

    return round(cgpa, 2)

# function to display information in a table
def display_table(course_codes, cu, grades):

    data = list(zip(course_codes, cu, grades))

    df = pd.DataFrame(data, columns=['Course Code', 'Course Unit', 'Grade'])

    df.index = df.index + 1

    return df

@app.route('/generate_result', methods=['POST'])

def generate_result():

    # acquire input from the client

    level = request.json['level']

    sem = request.json['sem']

    prev_cgpa = request.json['prev_cgpa']

    course_codes = request.json['course_codes']

    cu = request.json['cu']

    grades = request.json['grades']
    
    # validate input

if level < 100 or level > 600 or level not in (100, 200, 300, 400, 500, 600):

    return jsonify({"error": "Invalid input. Please enter a level between 100 - 600."})

if sem > 2 or sem < 1:

    return jsonify({"error": "Invalid input. Please enter a valid semester between 1 - 2."})
    
if course_unit < 1 or course_unit > 6:
    return jsonify({"error": "Invalid input. Please a valid course unit between 1 - 6."})

if course_grade not in ['A', 'B', 'C', 'D', 'E', 'F']:
    return jsonify({"error": "Invalid input. Please a valid grade between A - F."})
    
# calculate gpa and cgpa

gpa = calculate_gpa(cu, grades)

cgpa = calculate_cgpa(level, sem, prev_cgpa, gpa)

# display table

table = display_table(course_codes, cu, grades).to_html()

# return result

return jsonify({"table": table, "gpa": gpa, "cgpa": cgpa})









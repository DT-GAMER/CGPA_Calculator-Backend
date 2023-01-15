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

# function to display information in a table
def display_table(course_codes, cu, grades):

    data = list(zip(course_codes, cu, grades))

    df = pd.DataFrame(data, columns=['Course Code', 'Course Unit', 'Grade'])

    df.index = df.index + 1

    return df

@app.route('/generate_result', methods=['POST'])
def generate_result():
        # acquire input from the client
    Level = request.json['level']
    Semester = request.json['sem']
    Current_CGPA = request.json['prev_cgpa']
    Course_Codes = request.json['course_codes']
    Course_Unit = request.json['cu']
    Course_Grades = request.json['grades']

    # validate input
    if not(100 <= Level <= 600):
        return jsonify({"error": "Invalid input. Please enter a level between 100 - 600."})

    if Semester not in [1, 2]:
        return jsonify({"error": "Invalid input. Please enter a valid semester between 1 - 2."})

    if not all(0 < c <= 6 for c in Course_Unit):
        return jsonify({"error": "Invalid input. Please a valid course unit between 1 - 6."})

    if not all(g in ['A', 'B', 'C', 'D', 'E', 'F'] for g in Course_Grades):
        return jsonify({"error": "Invalid input. Please enter a valid grade"})
 
    # calculate GPA
    gpa = calculate_gpa(Course_Unit, Course_Grades)

    # calculate CGPA
    cgpa = calculate_cgpa(Level, Semester, Current_CGPA, gpa)

    # display information in a table
    result_table = display_table(Course_Codes, Course_Unit, Course_Grades)

    # return result
    return jsonify({"GPA": gpa, "CGPA": cgpa, "Result Table": result_table.to_dict()})

if __name__ == "__main__":
    app = Flask(__name__)
    app.run()

if __name__ == '__main__':
    app.run(debug=True)

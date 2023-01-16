#!/usr/bin/python3
import pandas as pd
import numpy as np

def calculate_gpa(course_units, grades):
    """
    Calculate the GPA given the course units and grades.
    course_units: list of integers representing the course units
    grades: list of integers representing the grades
    return: float rounded to 2 decimal places representing the GPA
    """
    
    
    total_cu = sum(course_units)
    weighted_points = np.dot(course_units, grades)
    gpa = weighted_points / total_cu
    return round(gpa, 2)

def calculate_cgpa(level, sem, prev_cgpa, gpa):

    """
    Calculate the CGPA given the level, semester, previous CGPA, and current GPA.
    level: integer representing the student's level
    sem: integer representing the student's semester (1 or 2)
    prev_cgpa: float representing the student's previous CGPA
    gpa: float representing the student's current semester GPA
    return: float rounded to 2 decimal places representing the CGPA
    """
    

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

def display_table(course_codes, course_units, grades):
    """
    Display a table of the course code, course units and course grade.
    course_codes: list of strings representing the course codes
    course_units: list of integers representing the course units
    grades: list of integers representing the grades
    """
    

    data = list(zip(course_codes, course_units, grades))
    df = pd.DataFrame(data, columns=['Course Code', 'Course Unit', 'Grade'])
    df.index = df.index + 1
    return df

def generate_result(course_codes, course_units, grades, level, sem, prev_cgpa):
    
    """
    Generate the student's result and display it in a table.
    course_codes: list of strings representing the course codes
    course_units: list of integers representing the course units
    grades: list of integers representing the grade
    level: integer representing the student's level
    sem: integer representing the student's semester (1 or 2)
    prev_cgpa: float representing the student's previous CGPA
    """


    gpa = calculate_gpa(course_units, grades)
    cgpa = calculate_cgpa(level, sem, prev_cgpa, gpa)
    print(display_table(course_codes, course_units, grades))
    print("GPA: ", gpa)
    print("CGPA: ", cgpa)

# acquire student's level
try:
    level = int(input("Level: "))
    if level < 100 or level > 600 or level not in (100, 200, 300, 400, 500, 600):
        raise ValueError("Invalid input. Please enter a level between 100 - 600.")
except ValueError as e:
    print(e)
    level = int(input("Level: "))

# acquire student's semester
try:
    sem = int(input("Semester: "))
    if sem > 2 or sem < 1:
        raise ValueError("Invalid input. Please enter a valid semester between 1 and 2.")
except ValueError as e:
    print(e)
    sem = int(input("Semester: "))

try:
    prev_cgpa = float(input("Previous CGPA: "))
    if prev_cgpa < 0.00 or prev_cgpa > 5.00:
        raise ValueError("Invalid input. Please enter a valid CGPA between 0.00 and 5.00")
except ValueError as e:
    print(e)
    prev_cgpa = float(input("Previous CGPA: "))

print("===========================")

# acquire number of courses attempted
while True:
    try:
        course_num = int(input("Courses Attempted: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("===========================")

# empty lists to accept course codes, course units, and grades
course_codes = []
cu = []
grades = []

print("===========================")

# loop to accept course codes, course units, and grades
for i in range(course_num):
    while True:
        try:
            course_code = input("Course code for course {}: ".format(i+1))
            course_unit = int(input("Course unit for course {}: ".format(i+1)))
            course_grade = input("Grade for course {}: ".format(i+1))
            if course_unit < 1 or course_unit > 6:
                raise ValueError("Invalid input. Please enter a valid course unit between 1 and 6.")
            if course_grade not in ['A', 'B', 'C', 'D', 'E', 'F']:
                raise ValueError("Invalid input. Please enter a valid grade between A and F.")
            break
        except ValueError as e:
            print(e)
    course_codes.append(course_code)
    cu.append(course_unit)
    grades.append(course_grade)

# convert grades to numerical equivalents
grades = [5.0 if grade == 'A' else 4.0 if grade == 'B' else 3.0 if grade == 'C' else 2.0 if grade == 'D' else 1.0 if grade == 'E' else 0.0 if grade == 'F' else None for grade in grades]

print("===========================")

# generate student's result
generate_result(course_codes, cu, grades, level, sem, prev_cgpa)

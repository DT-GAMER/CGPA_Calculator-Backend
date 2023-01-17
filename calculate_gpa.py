#!/usr/bin/python3
from tabulate import tabulate
import numpy as np

def calculate_gpa(course_units, grades):
    """
    Calculate the GPA given the course units and grades.
    """
    total_cu = sum(course_units)
    weighted_points = np.dot(course_units, grades)
    gpa = weighted_points / total_cu
    return round(gpa, 2)

def calculate_cgpa_utme(level, sem, prev_cgpa, gpa):

    """
    Calculate the CGPA of the Admission Mode "UTME" given the level, semester, previous CGPA, and current GPA.
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

def calculate_cgpa_de(level, sem, prev_cgpa, gpa):
    """
    Calculate the CGPA of the admission mode "DE" given the level, semester, previous CGPA, and current GPA.
    """
    cgpa = prev_cgpa #initialize cgpa to the previous cgpa
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
    
def display_table(course_codes, course_units, grades):
    """
    Display a table of the course codes, course units, and grades.
    """
    data = list(zip(course_codes, course_units, grades))
    table = tabulate(data, headers=["Course Code", "Course Units", "Grades"], tablefmt="fancy_grid")
    print(table)

def generate_result(course_codes, course_units, grades, level, sem, prev_cgpa):
    """
    Generate the student's result and display it in a table.
    """
    gpa = calculate_gpa(course_units, grades)
    print(display_table(course_codes, course_units, grades))
    print("GPA: ", gpa)
    if admission_mode == 'UTME':
    	cgpa = calculate_cgpa_utme(level, sem, prev_cgpa, gpa)
    	print("CGPA: ", cgpa)
    if admission_mode == 'DE':
    	cgpa = calculate_cgpa_de(level, sem, prev_cgpa, gpa)
    	print("CGPA: ", cgpa)
    	    	
	 
# Acquire Student admission mode 
try:
	 admission_mode = input("'UTME or DE': ").upper()
	 if admission_mode not in ['UTME', 'DE']:
	 	 raise ValueError("Invalid Input. Input one of 'UTME' or 'DE'")
except ValueError as e:
	 	 print(e)
	 	 admission_mode = input("'UTME or DE': ")
	 	 
# acquire student's level
try:
    level = int(input("Level: "))
    if admission_mode == 'UTME':
	    if level < 100 or level > 600 or level not in (100, 200, 300, 400, 500, 600):
	        raise ValueError("Invalid input. Please enter a level between 100 - 600.")
except ValueError as e:
	    print(e)
	    level = int(input("Level: "))
	    
try:	    
	if admission_mode == 'DE':
	        if level < 200 or level > 600 or level not in (200, 300, 400, 500, 600):
	        	raise ValueError("Invalid input. Please enter a level between 200 - 600.")
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
            course_code = input("Course code for course {}: ".format(i+1)).upper()
            course_unit = int(input("Course unit for course {}: ".format(i+1)))
            course_grade = input("Grade for course {}: ".format(i+1)).upper()
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

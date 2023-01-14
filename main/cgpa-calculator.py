import pandas as pd

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
    print(df)

# function to generate student's result
def generate_result(course_codes, cu, grades, level, sem, prev_cgpa):
    gpa = calculate_gpa(cu, grades)
    cgpa = calculate_cgpa(level, sem, prev_cgpa, gpa)
    display_table(course_codes, cu, grades)
    print("GPA: ", gpa)
    print("CGPA: ", cgpa)

# acquire student's level
while True:
    try:
        level = int(input("Level: "))
        if level < 100 or level > 600 or level not in (100, 200, 300, 400, 500, 600):
            raise ValueError("Invalid input. Please enter a level between 100 - 600.")
        break
    except ValueError as e:
        print(e)

# acquire student's semester
while True:
    try:
        sem = int(input("Semester: "))
        if sem > 2 or sem < 1:
            raise ValueError("Invalid input. Please enter a valid semester between 1 and 2.")
        break
    except ValueError as e:
        print(e)
        
while True:             
    try:
        prev_cgpa = float(input("Current CGPA: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

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

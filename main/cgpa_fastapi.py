from fastapi import FastAPI, HTTPException

import pandas as pd

app = FastAPI()

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

# function to generate student's result

def generate_result(course_codes, cu, grades, level, sem,

def generate_result(course_codes, cu, grades, level, sem,prev_cgpa):

    gpa = calculate_gpa(cu, grades)

    cgpa = calculate_cgpa(level, sem, prev_cgpa, gpa)

    return {"table": display_table(course_codes, cu, grades).to_dict(), "GPA": gpa, "CGPA": cgpa}

@app.post("/generate_result/")

async def generate_result_api(course_codes: List[str], cu: List[int], grades: List[float], level: int, sem: int, prev_cgpa: float):

    if level < 100 or level > 600 or level not in (100, 200, 300, 400, 500, 600):

        raise HTTPException(status_code=400, detail="Invalid level. Please enter a level between 100 - 600.")

    if sem > 2 or sem < 1:

        raise HTTPException(status_code=400, detail="Invalid semester. Please enter a valid semester between 1 and 2.")
        
    if course_unit < 1 or course_unit > 6:

        raise HTTPException(status_code=400, detail="Invalid input. Please a valid course unit between 1 - 6."})

    if course_grade not in ['A', 'B', 'C', 'D', 'E', 'F']:

        raise HTTPException(status_code=400, detail="Invalid input. Please a valid grade between A - F."})

    return generate_result(course_codes, cu, grades, level, sem, prev_cgpa) 

from fastapi import FastAPI
from typing import List, Tuple
import pandas as pd

app = FastAPI()

#Function to Calculate CGPA
def calculate_cgpa(cu: List[int], gp: List[float]) -> float:
    tcu = sum(cu)
    wp = [a*b for a,b in zip(cu,gp)]
    twp = sum(wp)
    cgpa = twp/tcu
    return round(cgpa,2)

# Function that displays information on Table 
def table(CourseCodes: List[str], cu: List[int], grade: List[str]) -> str:
    gt = list(zip(CourseCodes,cu,grade))
    df = pd.DataFrame(gt, columns=['Course Code', 'Course Unit', 'Grade'])
    df.index = df.index+1
    return df.to_markdown()

@app.post("/cgpa")
def cgpa(CourseCodes: List[str], cu: List[int], grade: List[str]):
    gp = []
    for point in grade:
        if point == "A":
            gp.append(5.0)
        elif point == "B":
            gp.append(4.0)
        elif point == "C":
            gp.append(3.0)
        elif point == "D":
            gp.append(2.0)
        elif point == "E":
            gp.append(1.0)
        elif point == "F":
            gp.append(0.0)
    cgpa = calculate_cgpa(cu, gp)
    table_data = table(CourseCodes, cu, grade)
    return {"cgpa": cgpa, "table": table_data}

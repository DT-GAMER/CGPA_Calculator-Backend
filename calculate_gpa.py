# ===============================
# GPA & CGPA CALCULATOR
# ===============================

def calculate_gpa(course_units, grades):
    """
    Calculate the GPA given the course units and grades.
    """
    if not course_units or not grades:
        raise ValueError("Course units and grades cannot be empty")

    if len(course_units) != len(grades):
        raise ValueError("Course units and grades must be the same length")

    if not all(0.0 <= g <= 5.0 for g in grades):
        raise ValueError("Grades must be between 0.0 and 5.0")

    total_cu = sum(course_units)
    if total_cu == 0:
        raise ValueError("Total course units cannot be zero")

    weighted_points = sum(course_units[i] * grades[i] for i in range(len(course_units)))
    gpa = weighted_points / total_cu
    return round(gpa, 2)


def calculate_cgpa_utme(level, sem, prev_cgpa, gpa):
    """
    Calculate CGPA for UTME students.
    """
    cgpa_map = {
        (100, 1): lambda p, g: 0,
        (100, 2): lambda p, g: (p + g) / 2,

        (200, 1): lambda p, g: (p * 2 + g) / 3,
        (200, 2): lambda p, g: (p * 3 + g) / 4,

        (300, 1): lambda p, g: (p * 4 + g) / 5,
        (300, 2): lambda p, g: (p * 5 + g) / 6,

        (400, 1): lambda p, g: (p * 6 + g) / 7,
        (400, 2): lambda p, g: (p * 7 + g) / 8,

        (500, 1): lambda p, g: (p * 8 + g) / 9,
        (500, 2): lambda p, g: (p * 9 + g) / 10,

        (600, 1): lambda p, g: (p * 10 + g) / 11,
        (600, 2): lambda p, g: (p * 11 + g) / 12,
    }

    key = (level, sem)
    if key not in cgpa_map:
        raise ValueError("Invalid level or semester for UTME")

    return round(cgpa_map[key](prev_cgpa, gpa), 2)


def calculate_cgpa_de(level, sem, prev_cgpa, gpa):
    """
    Calculate CGPA for Direct Entry (DE) students.
    """
    cgpa_map = {
        (200, 1): lambda p, g: 0,
        (200, 2): lambda p, g: (p + g) / 2,

        (300, 1): lambda p, g: (p * 2 + g) / 3,
        (300, 2): lambda p, g: (p * 3 + g) / 4,

        (400, 1): lambda p, g: (p * 4 + g) / 5,
        (400, 2): lambda p, g: (p * 5 + g) / 6,

        (500, 1): lambda p, g: (p * 6 + g) / 7,
        (500, 2): lambda p, g: (p * 7 + g) / 8,

        (600, 1): lambda p, g: (p * 8 + g) / 9,
        (600, 2): lambda p, g: (p * 9 + g) / 10,
    }

    key = (level, sem)
    if key not in cgpa_map:
        raise ValueError("Invalid level or semester for DE")

    return round(cgpa_map[key](prev_cgpa, gpa), 2)


def generate_result(admission_mode, course_codes, course_units, grades, level, sem, prev_cgpa):
    """
    Generate and print student's GPA and CGPA.
    """
    gpa = calculate_gpa(course_units, grades)
    print(f"GPA: {gpa}")

    if admission_mode == "UTME":
        cgpa = calculate_cgpa_utme(level, sem, prev_cgpa, gpa)
    else:
        cgpa = calculate_cgpa_de(level, sem, prev_cgpa, gpa)

    print(f"CGPA: {cgpa}")


# ===============================
# INPUT SECTION
# ===============================

def get_input(prompt, cast_func, condition=None, error_msg="Invalid input"):
    while True:
        try:
            value = cast_func(input(prompt))
            if condition and not condition(value):
                raise ValueError
            return value
        except ValueError:
            print(error_msg)


admission_mode = input("Admission Mode (UTME or DE): ").upper()
while admission_mode not in ("UTME", "DE"):
    admission_mode = input("Admission Mode (UTME or DE): ").upper()

level_range = (100, 200, 300, 400, 500, 600) if admission_mode == "UTME" else (200, 300, 400, 500, 600)

level = get_input(
    "Level: ",
    int,
    lambda x: x in level_range,
    "Invalid level for admission mode",
)

sem = get_input(
    "Semester (1 or 2): ",
    int,
    lambda x: x in (1, 2),
    "Semester must be 1 or 2",
)

prev_cgpa = get_input(
    "Previous CGPA: ",
    float,
    lambda x: 0.0 <= x <= 5.0,
    "CGPA must be between 0.0 and 5.0",
)

course_num = get_input(
    "Courses Attempted: ",
    int,
    lambda x: x > 0,
    "Number of courses must be greater than 0",
)

course_codes = []
course_units = []
grades = []

grade_map = {"A": 5.0, "B": 4.0, "C": 3.0, "D": 2.0, "E": 1.0, "F": 0.0}

for i in range(course_num):
    print(f"\nCourse {i + 1}")

    code = input("Course Code: ").upper()
    unit = get_input(
        "Course Unit (1–6): ",
        int,
        lambda x: 1 <= x <= 6,
        "Course unit must be between 1 and 6",
    )

    grade_letter = input("Grade (A–F): ").upper()
    while grade_letter not in grade_map:
        grade_letter = input("Grade (A–F): ").upper()

    course_codes.append(code)
    course_units.append(unit)
    grades.append(grade_map[grade_letter])


print("\n===========================")
generate_result(
    admission_mode,
    course_codes,
    course_units,
    grades,
    level,
    sem,
    prev_cgpa,
)

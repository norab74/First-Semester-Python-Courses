# BellP10 - Supplemental
# Purpose: Define Course class and load courses from CSV

import csv

class Course:
    # Represents a single course
    def __init__(self, course_id, course_name, crn, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.crn = crn
        self.instructor = instructor

    def __str__(self):
        return f"{self.course_id}: {self.course_name} (CRN: {self.crn}, Instructor: {self.instructor})"

@staticmethod
def load_courses_from_csv(file_path):
    courses = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            # Validate required columns
            required_fields = {'course_id', 'course_name', 'crn', 'instructor'}
            if not required_fields.issubset(reader.fieldnames):
                raise ValueError(f"CSV missing columns: {required_fields - set(reader.fieldnames)}")

            for row in reader:
                courses.append(Course(row['course_id'], row['course_name'], row['crn'], row['instructor']))

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except csv.Error as e:
        raise ValueError(f"Malformed CSV: {e}")

    return courses
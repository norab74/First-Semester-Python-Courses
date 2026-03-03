#BellP5 - Supplemental
#purpose - Imported as a library for Comp9, most code here has been disabled
from Course import Course, load_courses_from_csv

# Load available courses from CSV
available_courses = load_courses_from_csv('Programming Fundamentals/Comp10/availCourses.csv')

class Student:
    def __init__(self, student_id, name):
        # Initialize variables
        self.student_id = student_id
        self.name = name
        self.courses = []

    def register_course(self, course_id):
        for course in available_courses:
            if course.course_id == course_id:  # Check if course_id exists in schedule
                if course not in self.courses:
                    self.courses.append(course)  # register it if it doesn't
                return

    def drop_course(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:  # check if course_id exists in schedule
                self.courses.remove(course)  # if it does, remove it
                return

    @staticmethod
    def validate_student_id(student_id):
        # Validates that the student ID is a 5-digit number.
        return student_id.isdigit() and len(student_id) == 5

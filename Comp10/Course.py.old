#BellP5 - Supplemental
#purpose - To learn to define classes as single files, for import as library.

class Course:
    # Represents a single course.
    def __init__(self, course_id, course_name, instructor):
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor

    def __str__(self): 
        #instructs python HOW to return a string of our course.
        return f"{self.course_id}: {self.course_name} (Instructor: {self.instructor})"

# Example list of available courses (can be imported elsewhere)
available_courses = [
    Course('MATH 101', 'Intro to Arithmetic', 'B. Howell'),
    Course('CIS 202', 'Hacking and Its Prevention', 'J.B. Goode'),
    Course('IST 201', 'Standards and Instrumentation', 'I. Leanne'),
    Course('CMBA 101', 'Intro to Wumbology: The History of Chumbawumba', 'I.P. Freely')
]
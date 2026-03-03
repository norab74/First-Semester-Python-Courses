#BellP5 - Supplemental
#purpose - Imported as a library for Comp9, most code here has been disabled
from Course import available_courses, Course
#from time import sleep



class Student:
    def __init__(self, student_id, name):
        #Initialize variables
        self.student_id = student_id
        self.name = name
        self.courses = []
    def register_course(self, course_id):
        for course in available_courses:
            if course.course_id == course_id: #Check if course_id exists in schedule
                if course not in self.courses:
                    self.courses.append(course) #register it if it doesn't
                    #print(f"Registered for {course}")
                    #sleep(1)
                #else:
                    #print("Already registered for this course.") #report back if it does
                    #sleep(1)
                return
        #print("Course not found.") #report back if it doesn't exist at all

    def drop_course(self, course_id):
        for course in self.courses: 
            if course.course_id == course_id: # check if course_id exists in schedule
                self.courses.remove(course) #if it does, remove it
                #print(f"Dropped {course}")
                #sleep(1)
                return
        #print("Course not found in your schedule.") #if it doesn't move on
        #sleep(1)

    #def display_schedule(self):
        #if not self.courses: #check if courses are registered
            #print("No courses registered.") #report back if no
            #sleep(1)
        #else:
            #print("Your schedule:")
            #for course in self.courses: #report back with the schedule if yes
                #print(course)
            #sleep(2)

    @staticmethod
    def validate_student_id(student_id):
        # Validates that the student ID is a 5-digit number.
        return student_id.isdigit() and len(student_id) == 5
            

    #@classmethod
    #def display_available_courses(cls,available_courses):
        # Displays all available courses.
        #print("Display Available Courses function selected.")
        #sleep(1)
        #for course in available_courses: #iterate accross the available courses and #print them, as defined in Course.py
            #print(course) #type:ignore
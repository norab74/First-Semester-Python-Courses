#BellP5
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate proficiency with class definitions.
from Course import available_courses, Course
from Student import Student

def main():
    
    student_id = input("Enter your 5-digit Student ID: ")
    
    name = input("Enter your name: ")
    if not Student.validate_student_id(student_id):
        print("Invalid student ID. Must be 5 digits.")
        return
    student = Student(student_id, name)
    while True:
        
        print("\nMain Menu:")
        print("1. Register for a Course")
        print("2. Drop a Course")
        print("3. Display Schedule")
        print("4. Display Available Courses")
        print("5. Exit")
        choice = input("Please select an option: ").strip()

        match choice: #Super simple main menu logic, predefined in template with minor modification.
            case "1":
                Student.display_available_courses(available_courses)
                course_id = input("Enter course ID to register: ")
                student.register_course(course_id.upper())
            case "2":               
                course_id = input("Enter course ID to drop: ")
                student.drop_course(course_id)                
            case "3":
                student.display_schedule()
            case "4":
                Student.display_available_courses(available_courses)
            case "5":
                print("Exiting the program.")
                break
            case _:
                print("Invalid selection. Please try again.")
if __name__ == "__main__":
    main()

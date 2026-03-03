from Student import Student
def main():
    # Main menu for student course management.
    # Prompt user for student ID and name.
    student_id = input("Enter your 5-digit Student ID: ")
    name = input("Enter your name: ")
    # TODO: Validate student ID using Student.validate_student_id() and create a Student instance.
    # For now, assume the input is valid.

    if Student.validate_student_id(student_id) == 0:
        print("Invalid Student ID number, please try again")
        exit()
    else:
        student = Student()
        
        while True:
            print("\nMain Menu:")
            print("1. Register for a Course")
            print("2. Drop a Course")
            print("3. Display Schedule")
            print("4. Display Available Courses")
            print("5. Exit")
            choice = input("Please select an option: ").strip()
            
            # Use the match-case statement to handle user selection (requires Python 3.10+)
            match choice:
                case "1":
                    # TODO: Prompt for course ID if needed and call student.register_course()
                    student.register_course("dummy_course_id")
                case "2":
                    # TODO: Prompt for course ID if needed and call student.drop_course()
                    student.drop_course("dummy_course_id")
                case "3":
                    student.display_schedule()
                case "4":
                    Student.display_available_courses(Student.available_courses)
                case "5":
                    print("Exiting the program.")
                    break
                case _:
                    print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()

#BellP12
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To integrate SQLite3 into an already existing application, enabling data persistence accross sessions without cookies.

#Special Notes: This code has been refactored by Co-Pilot to improve readability and add docstrings, all included logic is original.

"""
Student.py
==========
This module defines the Student class, which manages student-related operations
in the Student Registration System using an SQLite database.

Features:
- Create tables for students and their registered courses.
- Add a student to the database.
- Register and drop courses for a student.
- List a student's schedule.
- Validate student IDs.

Modules:
    - sqlite3: For database operations.
"""

import sqlite3

class Student:
    
    """
    A class to manage student-related operations in the database.

    Attributes:
        student_id (str): The unique ID of the student.
        name (str): The name of the student.
        conn (sqlite3.Connection): The SQLite database connection.
        cursor (sqlite3.Cursor): Cursor object for executing SQL commands.
    """

    def __init__(self, student_id, name, conn):

        """
        Initialize the Student manager with student details and a database connection.

        Args:
            student_id (str): The unique ID of the student.
            name (str): The name of the student.
            conn (sqlite3.Connection): The SQLite database connection.
        """

        self.student_id = student_id
        self.name = name
        self.conn = conn
        self.cursor = conn.cursor()

    def create_tables(self):
        
        """
        Create required tables for students and their registered courses if they do not exist.

        Tables Created:
            - Students(student_id TEXT PRIMARY KEY, name TEXT)
            - RegisteredCourses(student_id TEXT, course_id TEXT)
              with foreign keys referencing Students and AvailableCourses.

        Commits changes to the database.
        """

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Students (
            student_id TEXT PRIMARY KEY,
            name TEXT
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS RegisteredCourses (
            student_id TEXT,
            course_id TEXT,
            FOREIGN KEY(student_id) REFERENCES Students(student_id),
            FOREIGN KEY(course_id) REFERENCES AvailableCourses(course_id)
        )
        """)
        self.conn.commit()

    def add_student_to_db(self):
        
        """
        Add the student to the Students table if not already present.

        Uses INSERT OR IGNORE to prevent duplicate entries.

        Handles database errors gracefully.
        """

        try:
            self.cursor.execute(
                "INSERT OR IGNORE INTO Students (student_id, name) VALUES (?, ?)",
                (self.student_id, self.name)
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def register_course(self, course_id):
        
        """
        Register the student for a course by adding an entry to RegisteredCourses.

        Args:
            course_id (str): The ID of the course to register.

        Notes:
            - Handles IntegrityError if the course or student does not exist or is already registered.
        """

        try:
            self.cursor.execute(
                "INSERT INTO RegisteredCourses (student_id, course_id) VALUES (?, ?)",
                (self.student_id, course_id)
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            print("Error: Course or student does not exist or already registered.")

    def drop_course(self, course_id):

        """
        Drop a course for the student by removing the entry from RegisteredCourses.

        Args:
            course_id (str): The ID of the course to drop.

        Handles database errors gracefully.
        """

        try:
            self.cursor.execute(
                "DELETE FROM RegisteredCourses WHERE student_id=? AND course_id=?",
                (self.student_id, course_id)
            )
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def list_schedule(self):

        """
        Retrieve the student's schedule by joining RegisteredCourses and AvailableCourses.

        Returns:
            list of tuples: Each tuple contains (course_id, course_name).
        """

        self.cursor.execute("""
        SELECT AvailableCourses.course_id, AvailableCourses.course_name
        FROM RegisteredCourses
        JOIN AvailableCourses ON RegisteredCourses.course_id = AvailableCourses.course_id
        WHERE RegisteredCourses.student_id=?
        """, (self.student_id,))
        return self.cursor.fetchall()

    @staticmethod
    def validate_student_id(student_id):
        
        """
        Validate the student ID format.

        Args:
            student_id (str): The student ID to validate.

        Returns:
            bool: True if the ID is numeric and exactly 5 digits long, False otherwise.
        """

        return student_id.isdigit() and len(student_id) == 5
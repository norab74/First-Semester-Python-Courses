#BellP12
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To integrate SQLite3 into an already existing application, enabling data persistence accross sessions without cookies.

#Special Notes: This code has been refactored by Co-Pilot to improve readability and add docstrings, all included logic is original.


"""
Course.py
=========
This module defines the Course class, which manages course-related operations
in the Student Registration System using an SQLite database.

Features:
- Create the AvailableCourses table.
- Populate courses from a CSV file.
- List all available courses.

Modules:
    - sqlite3: For database operations.
    - csv: For reading course data from CSV files.
"""





import sqlite3
import csv

class Course:   
    """
    A class to manage course-related operations in the database.

    Attributes:
        conn (sqlite3.Connection): The SQLite database connection.
        cursor (sqlite3.Cursor): Cursor object for executing SQL commands.
    """

    def __init__(self, conn):
        """
        Initialize the Course manager with a database connection.

        Args:
            conn (sqlite3.Connection): The SQLite database connection.
        """

        self.conn = conn
        self.cursor = conn.cursor()

    def create_tables(self):
        """
        Create the AvailableCourses table if it does not already exist.

        Table Structure:
            - course_id (TEXT PRIMARY KEY)
            - course_name (TEXT)
            - crn (TEXT)
            - instructor (TEXT)

        Commits changes to the database.
        """

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS AvailableCourses (
            course_id TEXT PRIMARY KEY,
            course_name TEXT,
            crn TEXT,
            instructor TEXT
        )
        """)
        self.conn.commit()

    def populate_courses(self, csv_file):

        """
        Populate the AvailableCourses table using data from a CSV file.

        Args:
            csv_file (str): Path to the CSV file containing course data.

        CSV Format:
            - course_id
            - course_name
            - crn
            - instructor

        Notes:
            - Uses INSERT OR IGNORE to avoid duplicate entries.
            - Prints an error message if the CSV file is not found.
            - Handles SQLite database errors gracefully.
        """

        try:
            with open(csv_file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.cursor.execute("""
                    INSERT OR IGNORE INTO AvailableCourses (course_id, course_name, crn, instructor)
                    VALUES (?, ?, ?, ?)
                    """, (row['course_id'], row['course_name'], row['crn'], row['instructor']))
            self.conn.commit()
        except FileNotFoundError:
            print(f"CSV file '{csv_file}' not found.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def list_courses(self):

        """
        Retrieve all available courses from the database.

        Returns:
            list of tuples: Each tuple contains (course_id, course_name, crn, instructor).
        """

        self.cursor.execute("SELECT * FROM AvailableCourses")
        return self.cursor.fetchall()
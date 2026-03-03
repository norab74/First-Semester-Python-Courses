#BellP12
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To integrate SQLite3 into an already existing application, enabling data persistence accross sessions without cookies.

#Special Notes: This code has been refactored by Co-Pilot to improve readability and add docstrings, all included logic is original.


'''
db_Initializer.py
=================
Simple database initialization script for the Student Registration System

This script:
-Creates a SQLite database and populates it with data from a supplied CSV file
matching the name 'schedule.csv'

Tables Created:
    -Students: Stores Student ID's and Names
    -AvailableCourses: Stores courses currently available
    -RegisteredCourses: Stores courses currently registered to students
    
Manual Intervention Possibly Needed:
    -Towards the bottom of this file, under "if __name__ == "__main__":"
        there is a line which begins with 'populate_available_courses':
        You may need to update this line such that 'schedule.csv'
        is replaced with the absolute path of your copy of 'schedule.csv'
'''



import sqlite3
import csv

def get_connection():
    '''
    Establish and return a multithread enabled connection to the SQLite database
    '''
    return sqlite3.connect('university.db', check_same_thread=False)

def create_tables(cursor):
    '''
    Create required tables in the database if they do not exist already
    
    Args:
        - cursor (sqlite3.Cursor): Cursor object to execute SQL commands.

    Tables Created:
        - Students(student_id TEXT PRIMARY KEY, name TEXT)
        - AvailableCourses(course_id TEXT PRIMARY KEY, course_name TEXT, crn TEXT, instructor TEXT)
        - RegisteredCourses(student_id TEXT, course_id TEXT) with UNIQUE constraint

    '''
    # Students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        student_id TEXT PRIMARY KEY,
        name TEXT
    )
    """)

    # AvailableCourses table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS AvailableCourses (
        course_id TEXT PRIMARY KEY,
        course_name TEXT,
        crn TEXT,
        instructor TEXT
    )
    """)

    # RegisteredCourses table with UNIQUE constraint
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS RegisteredCourses (
        student_id TEXT,
        course_id TEXT,
        FOREIGN KEY(student_id) REFERENCES Students(student_id),
        FOREIGN KEY(course_id) REFERENCES AvailableCourses(course_id),
        UNIQUE(student_id, course_id)  -- Prevent duplicate registrations
    )
    """)

def populate_available_courses(cursor, csv_file):
    '''

    Populate the AvailableCourses table using data from a CSV file.

    Args:
        cursor (sqlite3.Cursor): Cursor object to execute SQL commands.
        csv_file (str): Path to the CSV file containing course data.

    CSV Format:
        - course_id
        - course_name
        - crn
        - instructor

    Notes:
        - Uses INSERT OR IGNORE to avoid duplicate entries.
        - Prints an error message if the CSV file is not found.
    '''
    try:
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cursor.execute("""
                INSERT OR IGNORE INTO AvailableCourses (course_id, course_name, crn, instructor)
                VALUES (?, ?, ?, ?)
                """, (row['course_id'], row['course_name'], row['crn'], row['instructor']))
    except FileNotFoundError:
        print(f"CSV file '{csv_file}' not found.")

if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()
    create_tables(cursor)
    #absPath = input("Paste the absolute path of schedule.csv")
    # Update path to your CSV file if needed
    populate_available_courses(cursor, 'schedule.csv')
    conn.commit()
    conn.close()
#BellP12
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To integrate SQLite3 into an already existing application, enabling data persistence accross sessions without cookies.

#Special Notes: This code has been refactored by Co-Pilot to improve readability and add docstrings, all included logic is original.

"""
StreamlitUI.py
===============
A Streamlit-based Student Registration System integrated with SQLite.

Features:
- Student login using name and ID.
- View available courses.
- Register for courses.
- Drop courses.
- View schedule.

Modules:
    - streamlit: For building the web interface.
    - sqlite3: For database connectivity.
    - pandas: For displaying tabular data.
    - Student: Custom class for student operations.
    - Course: Custom class for course operations.
"""

import streamlit as st
import sqlite3
import pandas as pd
from Student import Student
from Course import Course


def get_connection():
    """
    Establish and return a connection to the SQLite database.

    Returns:
        sqlite3.Connection: A connection object to interact with the database.
    """
    return sqlite3.connect("university.db", check_same_thread=False)


# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="Registration System", initial_sidebar_state='expanded')

# -------------------------
# Session State Initialization
# -------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.student = None
    st.session_state.conn = None

# -------------------------
# Login Page
# -------------------------
if not st.session_state.logged_in:
    st.title("Course Registration System")
    st.subheader("Login")
    name = st.text_input("Enter your name:")
    student_id = st.text_input("Enter your Student ID (5 digits):")

    if st.button("Login"):
        if Student.validate_student_id(student_id) and name.strip():
            # Initialize DB connection
            st.session_state.conn = get_connection()
            conn = st.session_state.conn

            # Instantiate Student and Course managers
            student = Student(student_id, name, conn)
            course_manager = Course(conn)

            # Ensure tables exist
            student.create_tables()
            course_manager.create_tables()

            # Add student to DB
            student.add_student_to_db()

            # Save student object in session
            st.session_state.student = student
            st.session_state.logged_in = True

            st.success(f"Welcome, {name}!")
            st.rerun()
        else:
            st.error("Invalid Student ID or Name. Please try again.")
    st.stop()

# -------------------------
# Main App
# -------------------------
if st.session_state.logged_in:
    student = st.session_state.student
    conn = st.session_state.conn

    # Safety check for DB connection
    if conn is None:
        st.error("Database connection not initialized. Please log in again.")
        st.stop()

    # Instantiate Course manager only after confirming conn exists
    course_manager = Course(conn)

    st.sidebar.title("Controls")
    action = st.sidebar.radio("Choose an action:", ["View Courses", "Register", "Drop", "View Schedule", "Logout"])

    if action == "View Courses":
        st.subheader("Available Courses")
        courses = course_manager.list_courses()
        if courses:
            # Display only Course ID and Course Name
            df = pd.DataFrame([row[:4] for row in courses], columns=["Course ID", "Course Name", 'CRN', "Instructor"])
            st.dataframe(df)
        else:
            st.info("No courses available. Please check database initialization.")

    elif action == "Register":
        st.subheader("Register for a Course")
        courses = course_manager.list_courses()
        course_ids = [c[0] for c in courses]  # course_id from DB
        selected_course = st.selectbox("Select a course to register:", course_ids)
        if st.button("Confirm Registration"):
            student.register_course(selected_course)
            st.success(f"Registered for {selected_course}")

    elif action == "Drop":
        st.subheader("Drop a Course")
        schedule = student.list_schedule()
        if schedule:
            course_ids = [c[0] for c in schedule]
            selected_course = st.selectbox("Select a course to drop:", course_ids)
            if st.button("Confirm Drop"):
                student.drop_course(selected_course)
                st.success(f"Dropped {selected_course}")
        else:
            st.info("You have no courses to drop.")

    elif action == "View Schedule":
        st.subheader("Your Schedule")
        schedule = student.list_schedule()
        if schedule:
            # Display only Course ID and Course Name
            df = pd.DataFrame([row[:2] for row in schedule], columns=["Course ID", "Course Name"])
            st.dataframe(df)
        else:
            st.info("You have not registered for any courses yet.")

    elif action == "Logout":
        st.session_state.logged_in = False
        st.session_state.student = None
        if st.session_state.conn:
            st.session_state.conn.close()
        st.session_state.conn = None
        st.success("Logged out successfully.")
        st.rerun()
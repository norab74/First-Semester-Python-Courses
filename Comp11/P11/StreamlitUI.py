#BellP11
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate competency with streamlit, a server and page generator designed for datascience applications.



import streamlit as st
import pandas as pd
from Student import Student
from Course import load_courses_from_csv

# Load courses
availablecourses = load_courses_from_csv("availCourses.csv")

# Convert list of Course objects to DataFrame
def courses_to_dataframe(courses):
    data = [{
        "Course ID": course.course_id,
        "Course Name": course.course_name,
        "CRN": course.crn,
        "Instructor": course.instructor
    } for course in courses]
    return pd.DataFrame(data)

# --- PAGE CONFIG ---
st.set_page_config(page_title="Registration System", initial_sidebar_state='expanded') #Set sidebar to expanded so users can see where to navigate, they can close it if they want

# --- SESSION STATE ---
if "logged_in" not in st.session_state: #basic user tracking to ensure that we can verify a successful login, may implement tracking cookies for cross session tracking
    st.session_state.logged_in = False
    st.session_state.student = None

# --- LOGIN PAGE ---
if not st.session_state.logged_in:
    st.title("Course Registration System")
    st.subheader("Login")
    name = st.text_input("Enter your name:")
    student_id = st.text_input("Enter your Student ID (5 digits):")

    if st.button("Login"):
        if Student.validate_student_id(student_id) and name.strip():
            st.session_state.logged_in = True
            st.session_state.student = Student(student_id, name)
            st.success(f"Welcome, {name}!")
            st.rerun() #Reload the page
        else:
            st.error("Invalid Student ID or Name. Please try again.")
    st.stop()  # Hide everything else until a successful login
else:
    # --- MAIN APP ---
    #This section has a boatload of errors according to pylance, but that's a load of malarkey, she'll run just give 'er some gas
    st.sidebar.title("Controls")
    action = st.sidebar.radio("Choose an action:", ["View Courses", "Register", "Drop", "View Schedule", "Logout"])

    if action == "View Courses":
        st.subheader("Available Courses")
        df = courses_to_dataframe(availablecourses)
        st.dataframe(df)

    elif action == "Register":
        st.subheader("Register for a Course")
        course_ids = [course.course_id for course in availablecourses]
        selected_course = st.selectbox("Select a course to register:", course_ids)
        if st.button("Confirm Registration"):
            st.session_state.student.register_course(selected_course)
            st.success(f"Registered for {selected_course}")

    elif action == "Drop":
        st.subheader("Drop a Course")
        if st.session_state.student.courses:
            course_ids = [course.course_id for course in st.session_state.student.courses]
            selected_course = st.selectbox("Select a course to drop:", course_ids)
            if st.button("Confirm Drop"):
                st.session_state.student.drop_course(selected_course)
                st.success(f"Dropped {selected_course}")
        else:
            st.info("You have no courses to drop.")

    elif action == "View Schedule":
        st.subheader("Your Schedule")
        if st.session_state.student.courses:
            df = courses_to_dataframe(st.session_state.student.courses)
            st.dataframe(df)
        else:
            st.info("You have not registered for any courses yet.")

    elif action == "Logout":
        st.session_state.logged_in = False
        st.session_state.student = None
        st.rerun()
        

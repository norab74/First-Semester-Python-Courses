
# BellP13
# Programmer: Nora Bell
# Email: nbell8@cnm.edu
# Purpose: Replace Streamlit with Flask, using existing templates and session-based state.

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from Student import Student
from Course import Course

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for Flask session management

# --- DB Helper ---
def get_connection():
    # Assumes the database is pre-initialized
    return sqlite3.connect("university.db", check_same_thread=False)

# --- Login (index) ---
@app.route("/", methods=["GET", "POST"], endpoint="home")
def home():
    """
    Renders the login page (index.html) and handles login POST.
    Sets session['logged_in'], session['student_id'], session['name'] on success.
    """
    if request.method == "POST":
        student_id = request.form.get("student_id")
        name = request.form.get("name") or ""

        if Student.validate_student_id(student_id) and name.strip():
            conn = get_connection()
            try:
                # Create a Student with this connection
                student = Student(student_id, name, conn)
                # (Safe to call even if DB is pre-initialized)
                student.create_tables()
                student.add_student_to_db()

                # Persist session
                session["logged_in"] = True
                session["student_id"] = student_id
                session["name"] = name.strip()

                return redirect(url_for("menu"))
            finally:
                conn.close()
        else:
            # Minimal feedback; template stays unchanged
            return render_template("index.html", message="Invalid Student ID or Name.")

    # GET: render login
    return render_template("index.html")

# --- Menu ---
# Provide two route paths to satisfy both {{ url_for('menu') }} and {{ url_for('main_menu') }} in templates.
@app.route("/menu", methods=["GET", "POST"], endpoint="menu")
@app.route("/main_menu", methods=["GET", "POST"], endpoint="main_menu")
def menu():
    """
    Shows the main menu (menu.html).
    On POST, reads 'action' and redirects server-side based on the choice.
    """
    if not session.get("logged_in"):
        return redirect(url_for("home"))

    if request.method == "POST":
        # Read action sent by submit buttons in menu.html
        action = (request.form.get("action") or "").lower()

        route_map = {
            "register": "register",
            "drop": "drop",
            "sched": "sched",
            "catalog": "catalog",
            "exit": "bye",
        }
        target = route_map.get(action)

        if target:
            return redirect(url_for(target))

        # Fallback: unrecognized action; keep template unchanged, add minimal message
        return render_template("menu.html", name=session.get("name"), message="Invalid option.")

    # GET: render menu with user's name
    return render_template("menu.html", name=session.get("name"))

# --- Catalog (View Available Courses) ---
@app.route("/catalog", methods=["GET"], endpoint="catalog")
def catalog():
    """
    Renders catalog.html with available courses from the DB.
    """
    if not session.get("logged_in"):
        return redirect(url_for("home"))

    conn = get_connection()
    try:
        course_manager = Course(conn)
        courses = course_manager.list_courses()  # List of tuples: (course_id, course_name, crn, instructor)
        return render_template("catalog.html", available_courses=courses)
    finally:
        conn.close()

# --- Register ---
@app.route("/register", methods=["GET", "POST"], endpoint="register")
def register():
    """
    Renders register.html.
    On POST, attempts to register the given course_id for the logged-in student.
    """
    if not session.get("logged_in"):
        return redirect(url_for("home"))

    message = ""
    if request.method == "POST":
        course_id = (request.form.get("course_id") or "").strip()
        if course_id:
            conn = get_connection()
            try:
                student = Student(session["student_id"], session["name"], conn)
                # Student.register_course handles integrity constraints
                student.register_course(course_id)
                message = f"Course {course_id} registered successfully!"
            finally:
                conn.close()
        else:
            message = "Please enter a Course ID."

    return render_template("register.html", message=message)

# --- Drop ---
@app.route("/drop", methods=["GET", "POST"], endpoint="drop")
def drop():
    """
    Renders drop.html.
    On POST, attempts to drop the given course_id for the logged-in student.
    """
    if not session.get("logged_in"):
        return redirect(url_for("home"))

    message = ""
    if request.method == "POST":
        course_id = (request.form.get("course_id") or "").strip()
        if course_id:
            conn = get_connection()
            try:
                student = Student(session["student_id"], session["name"], conn)
                student.drop_course(course_id)
                message = f"Dropped {course_id}"
            finally:
                conn.close()
        else:
            message = "Please enter a Course ID."

    return render_template("drop.html", message=message)

# --- Schedule ---
@app.route("/sched", methods=["GET"], endpoint="sched")
def sched():
    """
    Renders sched.html with the student's current schedule
    (list of tuples: (course_id, course_name)).
    """
    if not session.get("logged_in"):
        return redirect(url_for("home"))

    conn = get_connection()
    try:
        student = Student(session["student_id"], session["name"], conn)
        schedule = student.list_schedule()
        return render_template("sched.html", schedule=schedule)
    finally:
        conn.close()

# --- Exit / Logout ---
@app.route("/bye", methods=["GET"], endpoint="bye")
def bye():
    """
    Clears the session and renders bye.html.
    Template contains a link back to the main menu.
    """
    session.clear()
    return render_template("bye.html")

# --- Dev entrypoint ---
if __name__ == "__main__":
    app.run(debug=True)

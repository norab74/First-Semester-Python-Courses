# Bellp9 - Supplemental
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QListWidget, QMessageBox, QHBoxLayout
)
from Course import Course ,load_courses_from_csv # Import Course class and loader
from Student import Student  # Import Student class
from PySide6.QtCore import Qt


class CourseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint | Qt.Dialog)  # type: ignore
        self.setWindowTitle("Course Registration System")
        self.student = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # -------------------------
        # STUDENT LOGIN SECTION
        # -------------------------
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Enter 5-digit Student ID")

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        self.login_label = QLabel("Student Login")
        self.login_label.show()

        layout.addWidget(self.login_label)
        layout.addWidget(self.id_input)
        layout.addWidget(self.name_input)
        layout.addWidget(self.login_button)

        # -------------------------
        # COURSE LIST SECTION
        # -------------------------
        self.course_label = QLabel("Available Courses")
        self.course_list = QListWidget()

        # Load courses with error handling
        try:
            self.courses = load_courses_from_csv('Programming Fundamentals/Comp10/availCourses.csv')
        except Exception as e:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error Loading Courses")
            msg.setText("An error occurred while loading courses.")
            msg.setInformativeText(str(e))
            msg.exec()
            self.courses = []

        for course in self.courses:
            self.course_list.addItem(str(course))

        self.course_label.hide()
        self.course_list.hide()

        layout.addWidget(self.course_label)
        layout.addWidget(self.course_list)

        # -------------------------
        # BUTTONS SECTION
        # -------------------------
        button_layout = QHBoxLayout()
        self.register = QPushButton("Register")
        self.drop = QPushButton("Drop")
        self.schedule = QPushButton("Show Schedule")
        self.exit = QPushButton("Exit")

        self.register.hide()
        self.drop.hide()
        self.schedule.hide()

        self.register.clicked.connect(self.register_course)
        self.drop.clicked.connect(self.drop_course)
        self.schedule.clicked.connect(self.show_schedule)
        self.exit.clicked.connect(self.close)

        for button in [self.register, self.drop, self.schedule, self.exit]:
            button_layout.addWidget(button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def login(self):
        student_id = self.id_input.text()
        name = self.name_input.text()

        if not Student.validate_student_id(student_id):
            QMessageBox.warning(self, "Invalid ID", "Student ID must be 5 digits.")
            return

        self.student = Student(student_id, name)
        QMessageBox.information(self, "Login Successful", f"Welcome, {name}!")  # type: ignore

        self.course_label.show()
        self.course_list.show()

        self.id_input.hide()
        self.name_input.hide()
        self.login_button.hide()
        self.login_label.hide()

        self.register.show()
        self.drop.show()
        self.schedule.show()

    def register_course(self):
        if not self.student:
            QMessageBox.warning(self, "Not Logged In", "Please login first.")
            return
        selected = self.course_list.currentItem()
        if selected:
            course_id = selected.text().split(":")[0]
            self.student.register_course(course_id)

    def drop_course(self):
        if not self.student:
            QMessageBox.warning(self, "Not Logged In", "Please login first.")
            return
        selected = self.course_list.currentItem()
        if selected:
            course_id = selected.text().split(":")[0]
            self.student.drop_course(course_id)

    def show_schedule(self):
        if not self.student:
            QMessageBox.warning(self, "Not Logged In", "Please login first.")
            return
        schedule = "\n".join(str(course) for course in self.student.courses)
        if not schedule:
            schedule = "No courses registered."
        QMessageBox.information(self, "Your Schedule", schedule)  # type: ignore
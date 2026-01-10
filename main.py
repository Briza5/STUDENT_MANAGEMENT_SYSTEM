from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QPushButton, QGridLayout, \
    QLineEdit, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QComboBox
from PyQt6.QtGui import QAction
import sys  # Import the sys module to handle command-line arguments
import sqlite3  # Import the sqlite3 module to work with SQLite databases


class MainWindow(QMainWindow):  # Define the MainWindow class inheriting from QMainWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        file_menu_item = self.menuBar().addMenu("&File")  # Create a File menu
        help_menu_item = self.menuBar().addMenu("&Help")  # Create a Help menu

        # Create an Add Student action
        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.insert)
        # Add the action to the File menu
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)  # Create an About action
        # Add the action to the Help menu
        help_menu_item.addAction(about_action)

        self.table = QTableWidget()  # Create a table widget
        # Set the number of columns in the table
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            # Set the header labels for the table
            ("ID", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)  # Hide the vertical header
        # Set the table as the central widget
        self.setCentralWidget(self.table)

    def load_data(self):
        # Connect to the SQLite database
        connection = sqlite3.connect("database.db")
        # Execute a query to fetch all students
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)  # Clear existing rows in the table
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)  # Insert a new row in the table
            for column_number, data in enumerate(row_data):
                # Set the item in the table at the specified row and column
                self.table.setItem(row_number, column_number,
                                   QTableWidgetItem(str(data)))
        connection.close()  # Close the database connection

    def insert(self):
        dialog = InsertDialog()  # Create an instance of the InsertDialog
        dialog.exec()  # Execute the dialog


class InsertDialog(QDialog):  # Define the InsertDialog class inheriting from QDialog
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)  # Set a fixed width for the dialog
        self.setFixedHeight(300)  # Set a fixed height for the dialog

        layout = QVBoxLayout()  # Create a vertical box layout

        # Add student name widget
        self.student_name = QLineEdit()  # Create a line edit for the student name
        self.student_name.setPlaceholderText("Name")  # Set placeholder text
        layout.addWidget(self.student_name)  # Add the line edit to the layout

        # Add combo box for course name
        self.course_name = QComboBox()  # Create a combo box for the course name
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)  # Add the combo box to the layout

        # Add mobile number widget
        self.mobile_number = QLineEdit()  # Create a line edit for the mobile number
        self.mobile_number.setPlaceholderText("Mobile")  # Set placeholder text
        layout.addWidget(self.mobile_number)  # Add the line edit to the layout

        # Add submit button
        submit_button = QPushButton("Submit")  # Create a submit button
        # Connect the button click to add_student method
        submit_button.clicked.connect(self.add_student)
        layout.addWidget(submit_button)  # Add the button to the layout

        self.setLayout(layout)  # Set the layout of the dialog

    def add_student(self):
        name = self.student_name.text()  # Get the student name from the line edit
        # Get the selected course from the combo box
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_number.text()  # Get the mobile number from the line edit
        # Connect to the SQLite database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()  # Create a cursor object
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, mobile))  # Execute the insert query
        connection.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor
        connection.close()  # Close the database connection
        main_window.load_data()  # Reload data in the main window


app = QApplication(sys.argv)  # Create the application object
main_window = MainWindow()  # Create an instance of the MainWindow class
main_window.show()  # Show the MainWindow window
main_window.load_data()  # Load data into the table
sys.exit(app.exec())  # Start the application's event loop

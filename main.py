from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QPushButton, QGridLayout, \
    QLineEdit, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QComboBox, QToolBar, QStatusBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6 import QtCore
import sys  # Import the sys module to handle command-line arguments
import sqlite3  # Import the sqlite3 module to work with SQLite databases


class MainWindow(QMainWindow):  # Define the MainWindow class inheriting from QMainWindow
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)  # Set the minimum size of the window

        file_menu_item = self.menuBar().addMenu("&File")  # Create a File menu
        help_menu_item = self.menuBar().addMenu("&Help")  # Create a Help menu
        edit_menu_item = self.menuBar().addMenu("&Edit")  # Create an Edit menu

        # Create an Add Student action
        add_student_action = QAction(
            QIcon("icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.insert)
        # Add the action to the File menu
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)  # Create an About action
        # Add the action to the Help menu
        help_menu_item.addAction(about_action)

        # Create a Search action
        search_action = QAction(QIcon("icons/search.png"), "Search", self)
        search_action.triggered.connect(self.search)
        # Add the action to the Edit menu
        edit_menu_item.addAction(search_action)

        self.table = QTableWidget()  # Create a table widget
        # Set the number of columns in the table
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            # Set the header labels for the table
            ("ID", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)  # Hide the vertical header
        # Set the table as the central widget
        self.setCentralWidget(self.table)

        # Create toolbar and add toolbar elements
        toolbar = QToolBar()  # Create a toolbar
        toolbar.setMovable(True)  # Make the toolbar movable
        self.addToolBar(toolbar)  # Add the toolbar to the main window
        # Add the Add Student action to the toolbar
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # Create status bar and add status bar elements
        self.statusbar = QStatusBar()  # Create a status bar
        # Set the status bar for the main window
        self.setStatusBar(self.statusbar)

        # Detect when a cell is clicked in the table
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")  # Create an Edit button
        # Connect the button click to edit method
        edit_button.clicked.connect(self.edit)

        delete_button = QPushButton("Delete Record")  # Create a Delete button
        # Connect the button click to delete method
        delete_button.clicked.connect(self.delete)

        # Clear existing buttons in the status bar
        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusBar().removeWidget(child)

        self.statusBar().addWidget(edit_button)  # Add the button to the status bar
        self.statusBar().addWidget(delete_button)  # Add the button to the status bar

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

    def search(self):
        dialog = SearchDialog()  # Create an instance of the SearchDialog
        dialog.exec()  # Execute the dialog

    def edit(self):
        dialog = EditDialog()  # Create an instance of the EditDialog
        dialog.exec()  # Execute the dialog
        pass

    def delete(self):
        dialog = DeleteDialog()  # Create an instance of the DeleteDialog
        dialog.exec()  # Execute the dialog
        pass


class EditDialog(QDialog):  # Define the EditDialog class inheriting from QDialog
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student Data")
        self.setFixedWidth(300)  # Set a fixed width for the dialog
        self.setFixedHeight(300)  # Set a fixed height for the dialog

        layout = QVBoxLayout()  # Create a vertical box layout
        # Get student name from the selected row in the main window table
        index = main_window.table.currentRow()  # Get the currently selected row index
        student_name = main_window.table.item(index, 1).text()

        # Get id from the selected row in the main window table
        self.student_id = main_window.table.item(index, 0).text()

        # Create a line edit for the student name
        self.student_name = QLineEdit(student_name)
        self.student_name.setPlaceholderText("Name")  # Set placeholder text
        layout.addWidget(self.student_name)  # Add the line edit to the layout

        # Add combo box for course name
        # Get the course name from the table
        course_name = main_window.table.item(index, 2).text()
        self.course_name = QComboBox()  # Create a combo box for the course name
        courses = ["Biology", "Math", "Astronomy", "Physics"]
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course_name)
        layout.addWidget(self.course_name)  # Add the combo box to the layout

        # Add mobile number widget
        # Get the mobile number from the table
        mobile_number = main_window.table.item(index, 3).text()
        # Create a line edit for the mobile number
        self.mobile_number = QLineEdit(mobile_number)
        self.mobile_number.setPlaceholderText("Mobile")  # Set placeholder text
        layout.addWidget(self.mobile_number)  # Add the line edit to the layout

        # Add submit button
        submit_button = QPushButton("Update")  # Create a update button
        # Connect the button click to add_student method
        submit_button.clicked.connect(self.update_student)
        layout.addWidget(submit_button)  # Add the button to the layout

        self.setLayout(layout)  # Set the layout of the dialog

    def update_student(self):
        # Connect to the SQLite database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()  # Create a cursor object
        cursor.execute("""UPDATE students SET name=?, course=?, mobile=? WHERE id=?""",
                       (self.student_name.text(),
                        self.course_name.itemText(
                            self.course_name.currentIndex()),
                        self.mobile_number.text(),
                        self.student_id))  # Execute the update query
        connection.commit()  # Commit the changes to the database
        cursor.close()  # Close the cursor

        main_window.load_data()  # Reload data in the main window


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


class SearchDialog(QDialog):  # Define the SearchDialog class inheriting from QDialog
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student Data")
        self.setFixedWidth(200)  # Set a fixed width for the dialog
        self.setFixedHeight(200)  # Set a fixed height for the dialog

        layout = QVBoxLayout()  # Create a vertical box layout

        # Add search data widget
        self.search_student = QLineEdit()  # Create a line for the search data
        self.search_student.setPlaceholderText("Name")  # Set placeholder text
        # Add the line edit to the layout
        layout.addWidget(self.search_student)

        # Add search button
        search_button = QPushButton("Search")  # Create a search button
        # Connect the button click to search_student_data method
        search_button.clicked.connect(self.search)
        layout.addWidget(search_button)  # Add the button to the layout

        self.setLayout(layout)  # Set the layout of the dialog

    def search(self):
        name = self.search_student.text()  # Get the search name from the line edit
        # Connect to the SQLite database
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()  # Create a cursor object
        result = cursor.execute("SELECT * FROM students WHERE name=?", (name,))
        rows = list(result)
        items = main_window.table.findItems(
            name, QtCore.Qt.MatchFlag.MatchExactly)  # Find matching items in the table
        for item in items:
            print(item)
            main_window.table.item(item.row(), 1).setSelected(
                True)  # Select the matching rows
        cursor.close()  # Close the cursor
        connection.close()  # Close the database connection


app = QApplication(sys.argv)  # Create the application object
main_window = MainWindow()  # Create an instance of the MainWindow class
main_window.show()  # Show the MainWindow window
main_window.load_data()  # Load data into the table
sys.exit(app.exec())  # Start the application's event loop

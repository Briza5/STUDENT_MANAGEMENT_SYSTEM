from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QPushButton, QGridLayout, \
    QLineEdit, QMainWindow, QTableWidget, QTableWidgetItem
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


app = QApplication(sys.argv)  # Create the application object
main_window = MainWindow()  # Create an instance of the MainWindow class
main_window.show()  # Show the MainWindow window
main_window.load_data()  # Load data into the table
sys.exit(app.exec())  # Start the application's event loop

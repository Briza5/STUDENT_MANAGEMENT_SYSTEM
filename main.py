from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QPushButton, QGridLayout, \
    QLineEdit, QMainWindow
from PyQt6.QtGui import QAction
import sys  # Import the sys module to handle command-line arguments


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


app = QApplication(sys.argv)  # Create the application object
main_window = MainWindow()  # Create an instance of the MainWindow class
main_window.show()  # Show the MainWindow window
sys.exit(app.exec())  # Start the application's event loop

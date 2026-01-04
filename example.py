from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QPushButton, QGridLayout, \
    QLineEdit
import sys  # Import the sys module to handle command-line arguments
from datetime import datetime  # Import the datetime module to work with dates


class AgeCalculator(QWidget):  # Define the AgeCalculator class inheriting from QWidget
    def __init__(self):  # Constructor method
        super().__init__()  # Call the constructor of the parent class
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()  # Create a grid layout

        name_label = QLabel("Name:")  # Create a label for the name input
        self.name_line_edit = QLineEdit()  # Create a line edit for the name input

        # Create a label for the date of birth input
        date_birth_label = QLabel("Date of Birth MM/DD/YYYY:")
        # Create a line edit for the date of birth inputs
        self.date_birth_line_edit = QLineEdit()

        # Create a button to calculate age
        calculate_button = QPushButton("Calculate Age")
        # Connect the button click to the calculate_age method
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")  # Create a label to display the output

        # Add widgets to the grid layout
        # Add the name label to the grid layout
        grid.addWidget(name_label, 0, 0)
        # Add the name line edit to the grid layout
        grid.addWidget(self.name_line_edit, 0, 1)
        # Add the date of birth label to the grid layout
        grid.addWidget(date_birth_label, 1, 0)
        # Add the date of birth line edit to the grid layout
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        # Add the calculate button to the grid layout
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        # Add the output label to the grid layout
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)  # Set the layout of the widget to the grid layout

    def calculate_age(self):  # Method to calculate age
        current_year = datetime.now().year  # Get the current year
        date_of_birth = self.date_birth_line_edit.text()
        year_of_birth = datetime.strptime(
            date_of_birth, "%m/%d/%Y").date().year
        age = current_year - year_of_birth  # Calculate the age
        # Set the output label text to display the age
        self.output_label.setText(
            f"{self.name_line_edit.text()} is {age} years old")


app = QApplication(sys.argv)  # Create the application object
age_calculator = AgeCalculator()  # Create an instance of the AgeCalculator class
age_calculator.show()  # Show the AgeCalculator window
sys.exit(app.exec())  # Start the application's event loop

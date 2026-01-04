from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QPushButton, QGridLayout, \
    QLineEdit, QComboBox
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()  # Create a grid layout
        self.combo = QComboBox()
        distance_label = QLabel("Distance:", )
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours)")
        self.time_line_edit = QLineEdit()

        # Create a button to calculate age
        calculate_button = QPushButton("Calculate")

        # Connect the button click to the calculate_age method
        calculate_button.clicked.connect(self.calculate_distance)
        self.combo.addItems(
            ["Metric (km)", "Imperial (miles)"])
        self.output_label = QLabel("")  # Create a label to display the output

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.combo, 0, 3)

        # Add the output label to the grid layout
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        self.setLayout(grid)  # Set the layout of the widget to the grid layout

    def calculate_distance(self):
        distance = self.distance_line_edit.text()
        time = self.time_line_edit.text()
        average_speed = int(distance)/int(time)
        self.choice = self.combo.currentText()

        if self.choice == 'Metric (km)':
            self.output_label.setText(
                f"Average speed is {average_speed} km/h")
        if self.choice == 'Imperial (miles)':
            self.output_label.setText(
                f"Average speed is {average_speed} miles per hour")


app = QApplication(sys.argv)  # Create the application object
# Create an instance of the AgeCalculator class
age_calculator = SpeedCalculator()
age_calculator.show()  # Show the AgeCalculator window
sys.exit(app.exec())  # Start the application's event loop

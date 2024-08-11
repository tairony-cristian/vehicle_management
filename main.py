from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox
from dbConnection import DatabaseConnection
from vehicle import Vehicle

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DatabaseConnection()  # Initializes the database connection
        self.init_ui()  # Sets up the user interface

    def init_ui(self):
        self.setWindowTitle("Vehicle Management System")

        self.layout = QVBoxLayout()

        # Search field by plate
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search by Plate...")
        self.layout.addWidget(self.search_input)

        # Search field by color
        self.search_color_input = QLineEdit(self)
        self.search_color_input.setPlaceholderText("Search by Color...")
        self.layout.addWidget(self.search_color_input)

        # Search button by plate
        self.search_button = QPushButton("Search by Plate", self)
        self.search_button.clicked.connect(self.search_vehicle_by_plate)
        self.layout.addWidget(self.search_button)

        # Search button by color
        self.search_color_button = QPushButton("Search by Color", self)
        self.search_color_button.clicked.connect(self.search_vehicle_by_color)
        self.layout.addWidget(self.search_color_button)

        # Button to list all vehicles
        self.list_all_button = QPushButton("List All Vehicles", self)
        self.list_all_button.clicked.connect(self.list_all_vehicles)
        self.layout.addWidget(self.list_all_button)

        # Button to add new vehicle
        self.add_button = QPushButton("Add Vehicle", self)
        self.add_button.clicked.connect(self.add_vehicle)
        self.layout.addWidget(self.add_button)

        # Button to update a vehicle
        self.update_button = QPushButton("Update Vehicle", self)
        self.update_button.clicked.connect(self.update_vehicle)
        self.layout.addWidget(self.update_button)

        # Button to delete a vehicle by ID
        self.delete_button = QPushButton("Delete Vehicle", self)
        self.delete_button.clicked.connect(self.delete_vehicle)
        self.layout.addWidget(self.delete_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)


    def search_vehicle(self):
        plate = self.search_input.text()  # Retrieves the text entered in the search input field
        result = self.db.get_vehicle_by_plate(plate)  # Queries the database for the vehicle by its plate number
        if result == "Vehicle not found.":  # Checks if the vehicle was not found
            QMessageBox.warning(self, "Error", "Vehicle not found.")  # Displays a warning message if the vehicle was not found
        else:
            QMessageBox.information(self, "Vehicle Found", f"Details: {result}")  # Displays vehicle details if found

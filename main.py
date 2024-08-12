from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox, QFormLayout, QInputDialog, QApplication
from dbConnection import DatabaseConnection
from vehicle import Vehicle
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DatabaseConnection()  # Initializes the database connection
        self.init_ui()  # Sets up the user interface

    def init_ui(self):
        self.setWindowTitle("Vehicle Management System")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout() #initialization main layout

        self.form_layout = QFormLayout() #Layout for form fields

        # Input fields for vehicle details
        self.name_input = QLineEdit(self)
        self.plate_input = QLineEdit(self)
        self.brand_input = QLineEdit(self)
        self.year_input = QLineEdit(self)
        self.color_input = QLineEdit(self)
        self.renavam_input = QLineEdit(self)

        # Add fields to the form layout
        self.form_layout.addRow("User Name:", self.name_input)
        self.form_layout.addRow("Plate:", self.plate_input)
        self.form_layout.addRow("Brand:", self.brand_input)
        self.form_layout.addRow("Year:", self.year_input)
        self.form_layout.addRow("Color:", self.color_input)
        self.form_layout.addRow("Renavam:", self.renavam_input)

        self.layout.addLayout(self.form_layout)  #Add the form layout to the main layout

       # Buttons to add vehicles
        self.add_button = QPushButton("Add Vehicle", self)
        self.add_button.clicked.connect(self.add_vehicle)
        self.layout.addWidget(self.add_button)

        # Search field by id
        self.search_id_input = QLineEdit(self)
        self.search_id_input.setPlaceholderText("Search by Id...")
        self.layout.addWidget(self.search_id_input)

        # Search field by plate
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Search by Plate...")
        self.layout.addWidget(self.search_input)

        # Search field by color
        self.search_color_input = QLineEdit(self)
        self.search_color_input.setPlaceholderText("Search by Color...")
        self.layout.addWidget(self.search_color_input)

         # Search button by id
        self.search_id_button = QPushButton("Search by Id", self)
        self.search_id_button.clicked.connect(self.search_vehicle_by_id)
        self.layout.addWidget(self.search_id_button)

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

        # Button to update a vehicle
        self.update_button = QPushButton("Update Vehicle", self)
        self.update_button.clicked.connect(self.edit_vehicle)
        self.layout.addWidget(self.update_button)

        # Button to delete a vehicle by ID
        self.delete_button = QPushButton("Delete Vehicle", self)
        self.delete_button.clicked.connect(self.delete_vehicle)
        self.layout.addWidget(self.delete_button)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def search_vehicle_by_id(self):
        id = self.search_id_input.text()
        result = self.db.get_vehicle_by_id(id)
        if result == "Vehicle not found.":
            QMessageBox.warning(self, "Error", "Vehicle not found.")
        else:
            QMessageBox.information(self, "Vehicle Found", f"Details: {result}")

    def search_vehicle_by_plate(self):
        plate = self.search_input.text()
        result = self.db.get_vehicle_by_plate(plate)
        if result == "Vehicle not found.":
            QMessageBox.warning(self, "Error", "Vehicle not found.")
        else:
            QMessageBox.information(self, "Vehicle Found", f"Details: {result}")

    def search_vehicle_by_color(self):
        color = self.search_color_input.text()
        result = self.db.get_vehicles_by_color(color)
        if result == "Vehicle not found.":
            QMessageBox.warning(self, "Error", "No vehicles found with this color.")
        else:
            QMessageBox.information(self, "Vehicles Found", f"Details: {result}")

    def list_all_vehicles(self):
        result = self.db.get_all_vehicles()
        if not result:
            QMessageBox.warning(self, "Error", "No vehicles found.")
        else:
            QMessageBox.information(self, "All Vehicles", f"Details: {result}")

    def add_vehicle(self):
            vehicle = Vehicle(
                id=None,
                user_name=self.name_input.text(),
                plate=self.plate_input.text(),
                brand=self.brand_input.text(),
                year=int(self.year_input.text()),
                color=self.color_input.text(),
                renavam=self.renavam_input.text()
            )
            self.db.add_vehicle(vehicle)
            QMessageBox.information(self, "Success", "Vehicle added successfully!")

    def edit_vehicle(self):
        vehicle_id = int(QInputDialog.getText(self, "Vehicle ID", "Enter the vehicle ID to edit:")[0])
        vehicle = Vehicle(
            id=vehicle_id,
            user_name=self.name_input.text(),
            plate=self.plate_input.text(),
            brand=self.brand_input.text(),
            year=int(self.year_input.text()),
            color=self.color_input.text(),
            renavam=self.renavam_input.text()
        )
        self.db.edit_vehicle(vehicle_id, vehicle)
        QMessageBox.information(self, "Success", "Vehicle updated successfully!")

    def delete_vehicle(self):
        vehicle_id, ok = QInputDialog.getInt(self, "Delete Vehicle", "Enter Vehicle ID:")
        if ok:
            self.db.delete_vehicle(vehicle_id)
            QMessageBox.information(self, "Success", f"Vehicle with ID {vehicle_id} deleted.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
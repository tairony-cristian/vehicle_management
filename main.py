from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox, 
                             QFormLayout, QInputDialog, QApplication, QComboBox, QTableWidget, 
                             QTableWidgetItem, QDialog, QHBoxLayout,QHeaderView)
from dbConnection import DatabaseConnection
from vehicle import Vehicle
from EditVehicleDialog import EditVehicleDialog
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DatabaseConnection()  # Initializes the database connection
        self.init_ui()  # Sets up the user interface

    def init_ui(self):
        self.setWindowTitle("Vehicle Management System")
        self.setGeometry(100, 100, 1200, 600)

        self.layout = QVBoxLayout() # Initialization main layout

        search_layout = QHBoxLayout()

         # search field
        self.search_input = QLineEdit(self)
        self.search_input.setPlaceholderText("Enter search term...")
        search_layout.addWidget(self.search_input)

        # ComboBox to select search type
        self.search_type_combobox = QComboBox(self)
        self.search_type_combobox.addItems(["Search by ID", "Search by Plate", "Search by Color"])
        search_layout.addWidget(self.search_type_combobox)

        # Search button
        self.search_button = QPushButton("Search", self)
        self.search_button.clicked.connect(self.perform_search)
        search_layout.addWidget(self.search_button)

        # Add the search layout to the main layout
        self.layout.addLayout(search_layout)

        # Input fields for vehicle details
        self.name_input = QLineEdit(self)
        self.plate_input = QLineEdit(self)
        self.brand_input = QLineEdit(self)
        self.year_input = QLineEdit(self)
        self.color_input = QLineEdit(self)
        self.renavam_input = QLineEdit(self)


        # Add fields to the form layout
        self.form_layout = QFormLayout() # Layout for form fields
        self.form_layout.addRow("User Name:", self.name_input)
        self.form_layout.addRow("Plate:", self.plate_input)
        self.form_layout.addRow("Brand:", self.brand_input)
        self.form_layout.addRow("Year:", self.year_input)
        self.form_layout.addRow("Color:", self.color_input)
        self.form_layout.addRow("Renavam:", self.renavam_input)
        self.layout.addLayout(self.form_layout)  # Add the form layout to the main layout

        # Button layout to align buttons side by side
        button_layout = QHBoxLayout()

        # Buttons to add vehicles
        self.add_button = QPushButton("Add Vehicle", self)
        self.add_button.clicked.connect(self.add_vehicle)
        button_layout.addWidget(self.add_button)

        # Button to list all vehicles
        self.list_all_button = QPushButton("List All Vehicles", self)
        self.list_all_button.clicked.connect(self.list_all_vehicles)
        button_layout.addWidget(self.list_all_button)

        # Button to update a vehicle
        self.Edit_button = QPushButton("Edit Vehicle", self)
        self.Edit_button.clicked.connect(self.edit_vehicle)
        button_layout.addWidget(self.Edit_button)

        # Button to delete a vehicle by ID
        self.delete_button = QPushButton("Delete Vehicle", self)
        self.delete_button.clicked.connect(self.delete_vehicle)
        button_layout.addWidget(self.delete_button)

       # Add the button layout to the main layout
        self.layout.addLayout(button_layout) 

        # Table to display vehicle data
        self.table_widget = QTableWidget()
        self.table_widget.setSelectionBehavior(QTableWidget.SelectRows)  # Select entire rows
        self.table_widget.setSelectionMode(QTableWidget.SingleSelection)  # Allow only one selection at a time
        self.layout.addWidget(self.table_widget)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        self.list_all_vehicles()

    def perform_search(self):
        search_type = self.search_type_combobox.currentText()
        search_term = self.search_input.text()

        if search_type == "Search by ID":
            results = self.db.get_vehicle_by_id(search_term)
            if results == "Vehicle not found.":
                QMessageBox.warning(self, "Error", "Vehicle not found.")
                self.table_widget.setRowCount(0)
            else:
                self.update_table(results)

        elif search_type == "Search by Plate":
            results = self.db.get_vehicle_by_plate(search_term)
            if results == "Vehicle not found.":
                QMessageBox.warning(self, "Error", "Vehicle not found.")
                self.table_widget.setRowCount(0)
            else:
                self.update_table(results)

        elif search_type == "Search by Color":
            results = self.db.get_vehicles_by_color(search_term)
            if results == "Vehicle not found.":
                QMessageBox.warning(self, "Error", "No vehicles found with this color.")
                self.table_widget.setRowCount(0)
            else:
                self.update_table(results)

    def list_all_vehicles(self):
        results = self.db.get_all_vehicles()
        if not results:
            QMessageBox.warning(self, "Error", "No vehicles found.")
            self.table_widget.setRowCount(0)
        else:
            self.update_table(results)

    def update_table(self, data):
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(7)  # Number of columns (adjust if needed)
        self.table_widget.setHorizontalHeaderLabels(["ID", "User Name", "Plate", "Brand", "Year", "Color", "Renavam"])

        for row_num, row_data in enumerate(data):
            for col_num, item in enumerate(row_data):
                self.table_widget.setItem(row_num, col_num, QTableWidgetItem(str(item)))
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)  # Adjust columns proportionally to the window size

    def add_vehicle(self):
        # Verifica se algum campo está vazio
        if not all([self.name_input.text(), self.plate_input.text(), self.brand_input.text(),
                    self.year_input.text(), self.color_input.text(), self.renavam_input.text()]):
            QMessageBox.warning(self, "Input Error", "Please fill in all fields.")
            return

        try:
            year = int(self.year_input.text())
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Year must be a valid number.")
            return

        vehicle = Vehicle(
            id=None,
            user_name=self.name_input.text(),
            plate=self.plate_input.text(),
            brand=self.brand_input.text(),
            year=year,
            color=self.color_input.text(),
            renavam=self.renavam_input.text()
        )
        self.db.add_vehicle(vehicle)
        QMessageBox.information(self, "Success", "Vehicle added successfully!")
        
        # Clear input fields after adding
        self.name_input.clear()
        self.plate_input.clear()
        self.brand_input.clear()
        self.year_input.clear()
        self.color_input.clear()
        self.renavam_input.clear()

        self.list_all_vehicles()

    def edit_vehicle(self):
        selected_items = self.table_widget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Error", "Please select a vehicle to edit.")
            return
        
        selected_row = selected_items[0].row()
        vehicle_id = self.table_widget.item(selected_row, 0).text()

        # Fetch current details of the selected vehicle
        vehicle_details = self.db.get_vehicle_by_id(vehicle_id)
        if vehicle_details == "Vehicle not found.":
            QMessageBox.warning(self, "Error", "Vehicle not found.")
            return
        
        # Open the edit dialog
        dialog = EditVehicleDialog(vehicle_id, vehicle_details[0], self.db, self)
        if dialog.exec_() == QDialog.Accepted:
            self.list_all_vehicles()  # Refresh the table after update

    def delete_vehicle(self):
        selected_items = self.table_widget.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Error", "Please select a vehicle to delete.")
            return
        
        vehicle_id = self.table_widget.item(selected_items[0].row(), 0).text()
        self.db.delete_vehicle(int(vehicle_id))
        QMessageBox.information(self, "Success", f"Vehicle with ID {vehicle_id} deleted.")
        self.list_all_vehicles()  # Refresh the table after deletion

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

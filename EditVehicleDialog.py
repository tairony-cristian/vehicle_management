from PyQt5.QtWidgets import QDialog, QFormLayout, QPushButton, QLineEdit, QVBoxLayout, QMessageBox
from vehicle import Vehicle

class EditVehicleDialog(QDialog):
    def __init__(self, vehicle_id, vehicle_details, db, parent=None):
        super().__init__(parent)
        self.vehicle_id = vehicle_id
        self.db = db
        self.init_ui(vehicle_details)

    def init_ui(self, vehicle_details):
        self.setWindowTitle("Edit Vehicle")
        self.setGeometry(150, 150, 300, 200)

        layout = QFormLayout()

        self.name_input = QLineEdit(self)
        self.name_input.setText(vehicle_details[1])
        layout.addRow("User Name:", self.name_input)

        self.plate_input = QLineEdit(self)
        self.plate_input.setText(vehicle_details[2])
        layout.addRow("Plate:", self.plate_input)

        self.brand_input = QLineEdit(self)
        self.brand_input.setText(vehicle_details[3])
        layout.addRow("Brand:", self.brand_input)

        self.year_input = QLineEdit(self)
        self.year_input.setText(str(vehicle_details[4]))
        layout.addRow("Year:", self.year_input)

        self.color_input = QLineEdit(self)
        self.color_input.setText(vehicle_details[5])
        layout.addRow("Color:", self.color_input)

        self.renavam_input = QLineEdit(self)
        self.renavam_input.setText(vehicle_details[6])
        layout.addRow("Renavam:", self.renavam_input)

        button_layout = QVBoxLayout()
        self.save_button = QPushButton("Save", self)
        self.save_button.clicked.connect(self.save_changes)
        button_layout.addWidget(self.save_button)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(self.cancel_button)

        layout.addRow(button_layout)
        self.setLayout(layout)

    def save_changes(self):
        updated_vehicle = Vehicle(
            id=self.vehicle_id,
            user_name=self.name_input.text(),
            plate=self.plate_input.text(),
            brand=self.brand_input.text(),
            year=int(self.year_input.text()),
            color=self.color_input.text(),
            renavam=self.renavam_input.text()
        )
        self.db.update_vehicle(self.vehicle_id, updated_vehicle)
        QMessageBox.information(self, "Success", "Vehicle updated successfully!")
        self.accept()

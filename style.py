from PyQt5.QtWidgets import QApplication

class Style:
    @staticmethod
    def apply_style(app: QApplication):
        # Define a custom style sheet
        style_sheet = """
        QMainWindow {
            background-color: #f5f5f5;
        }
        QWidget {
            font-family: Arial, sans-serif;
            font-size: 12px;
        }
        QLineEdit, QComboBox, QPushButton {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 5px;
        }
        QPushButton {
            background-color: #0070C0;
            color: white;
            font-weight: bold;
            padding: 10px;
        }
        QPushButton:hover {
            background-color: #00418A;
        }
        QLineEdit:focus, QComboBox:focus {
            border-color: #0070C0;
        }
        QTableWidget {
            border: 1px solid #ddd;
            gridline-color: #ddd;
        }
        QTableWidget::item {
            padding: 5px;
        }
        QHeaderView::section {
            background-color: #0070C0;
            color: white;
            padding: 5px;
            border: 1px solid #ddd;
        }
        QFormLayout {
            margin: 10px;
        }
        """
        app.setStyleSheet(style_sheet)

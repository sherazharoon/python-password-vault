# ui.py
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication, QDesktopWidget

class PasswordVaultUI(QWidget):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.service_name_label = QLabel('Service/App Name:')
        self.service_name_entry = QLineEdit()

        self.username_label = QLabel('Username:')
        self.username_entry = QLineEdit()

        self.password_label = QLabel('Password:')
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.add_button = QPushButton('Add Entry', self)
        self.retrieve_button = QPushButton('Retrieve Password', self)
        self.exit_button = QPushButton('Exit', self)

        # Set up layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.service_name_label)
        layout.addWidget(self.service_name_entry)
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.add_button)
        layout.addWidget(self.retrieve_button)
        layout.addWidget(self.exit_button)

        # Apply dark theme with a lighter tone of purple
        self.setStyleSheet("""
            QWidget {
                background-color: #1E1E3C;
                color: #FFFFFF;
            }

            QLabel {
                color: #BB86FC;
            }

            QLineEdit {
                background-color: #29294E;
                color: #FFFFFF;
                border: 1px solid #BB86FC;
                border-radius: 5px;
            }

            QPushButton {
                background-color: #6200EA;
                color: #FFFFFF;
                border: 1px solid #6200EA;
                border-radius: 5px;
                padding: 5px;
            }

            QPushButton:hover {
                background-color: #3D007A;
                border: 1px solid #3D007A;
            }

            QPushButton:pressed {
                background-color: #1D004E;
                border: 1px solid #1D004E;
            }
        """)

        # Set window title
        self.setWindowTitle('Vault')

        # Center the window on the screen and set a larger size
        self.center_on_screen()

    def center_on_screen(self):
        # Get screen geometry
        screen = QDesktopWidget().screenGeometry()

        # Calculate center position
        x_position = (screen.width() - self.width()) // 2
        y_position = (screen.height() - self.height()) // 2

        # Set window position and size
        self.setGeometry(x_position, y_position, self.width(), self.height())

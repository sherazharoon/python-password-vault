# main.py
from PyQt5.QtWidgets import QApplication
from ui import PasswordVaultUI
from logic import PasswordVaultLogic
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create UI and logic objects
    password_vault_ui = PasswordVaultUI()
    password_vault_logic = PasswordVaultLogic(password_vault_ui)

    # Show the main window
    password_vault_ui.show()

    sys.exit(app.exec_())

# logic.py
from PyQt5.QtWidgets import QMessageBox
from cryptography.fernet import Fernet
import sqlite3

class PasswordVaultLogic:
    def __init__(self, ui):
        self.ui = ui

        # Generate a key for encryption and decryption
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

        # Connect to the database (create it if not exists)
        self.connection = sqlite3.connect("password_vault.db")
        self.cursor = self.connection.cursor()

        # Create a table to store the vault entries
        self.cursor.execute("CREATE TABLE IF NOT EXISTS vault (id INTEGER PRIMARY KEY, service_name TEXT, username TEXT, password TEXT)")

        # Connect UI signals to logic functions
        self.ui.add_button.clicked.connect(self.create_entry)
        self.ui.retrieve_button.clicked.connect(self.retrieve_password)
        self.ui.exit_button.clicked.connect(self.exit_application)

    def create_entry(self):
        service_name = self.ui.service_name_entry.text()
        username = self.ui.username_entry.text()
        password = self.ui.password_entry.text()

        # Encrypt the password before storing
        encrypted_password = self.encrypt_password(password)

        # Store the entry in the database
        self.cursor.execute("INSERT INTO vault (service_name, username, password) VALUES (?, ?, ?)",
                            (service_name, username, encrypted_password))
        self.connection.commit()

        QMessageBox.information(self.ui, 'Success', 'Entry added successfully.')

        # Clear the entry values
        self.ui.service_name_entry.clear()
        self.ui.username_entry.clear()
        self.ui.password_entry.clear()

    def retrieve_password(self):
        service_name = self.ui.service_name_entry.text()

        # Retrieve the encrypted password from the database
        self.cursor.execute("SELECT password FROM vault WHERE service_name=?", (service_name,))
        result = self.cursor.fetchone()

        if result:
            encrypted_password = result[0]
            decrypted_password = self.decrypt_password(encrypted_password)
            QMessageBox.information(self.ui, 'Password', f'Retrieved decrypted password: {decrypted_password}')
        else:
            QMessageBox.warning(self.ui, 'Error', 'Entry not found.')

    def encrypt_password(self, password):
        encrypted_password = self.cipher_suite.encrypt(password.encode('utf-8'))
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        decrypted_password = self.cipher_suite.decrypt(encrypted_password).decode('utf-8')
        return decrypted_password

    def exit_application(self):
        # Close the database connection and exit the application
        self.connection.close()
        self.ui.close()

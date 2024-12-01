from cryptography.fernet import Fernet
import logging



'''

PrivacyManager Class: Handles encryption and decryption to ensure user data privacy.
Fernet Encryption: Uses symmetric encryption to protect data.
encrypt_data and decrypt_data Methods: Encrypts or decrypts the data with proper error handling for any issues.

'''
class PrivacyManager:
    def __init__(self, key):
        try:
            self.cipher = Fernet(key)
        except Exception as e:
            logging.error(f"Error initializing PrivacyManager: {e}")
            raise
        logging.basicConfig(level=logging.INFO)

    def encrypt_data(self, data):
        try:
            encrypted_data = self.cipher.encrypt(data.encode())
            logging.info("Data encrypted successfully")
            return encrypted_data
        except Exception as e:
            logging.error(f"Error encrypting data: {e}")
            return None

    def decrypt_data(self, encrypted_data):
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data).decode()
            logging.info("Data decrypted successfully")
            return decrypted_data
        except Exception as e:
            logging.error(f"Error decrypting data: {e}")
            return None



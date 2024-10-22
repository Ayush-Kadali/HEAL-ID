
import pymysql
from typing import List

class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connect()
        return cls._instance
    
    def connect(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="python",
            password="Password@123",
            database="heal_id"
        )
        self.cursor = self.connection.cursor()
        
    def get_valid_doctor_ids(self):
        self.cursor.execute("SELECT Doctor_ID FROM Doctors")
        return [str(row[0]) for row in self.cursor.fetchall()]

    def get_valid_aadhar_numbers(self):
        self.cursor.execute("SELECT Aadhar_number FROM Personal_Information")
        return [str(row[0]) for row in self.cursor.fetchall()]


import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    # Constructor method to establish a connection with the MySQL database
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="your_password",
                database="vehicle_management"
            )
            # Create a cursor object to interact with the database
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def executeQuery(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            # Commit the transaction to save changes to the database  
            self.connection.commit()
        except Error as e:
            print(f"Error executing query: {e}")
            
    # Method to fetch results from a SELECT query
    def fetchResults(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()
    
    # Method to close the cursor and connection to the database
    def close(self):
        self.cursor.close()
        self.connection.close()






# db_connection.py
import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="your_password",
                database="vehicle_management"
            )
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
        except Error as e:
            print(f"Error executing query: {e}")

    def fetch_results(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

    # CRUD Methods
    def add_vehicle(self, vehicle):
        query = """
        INSERT INTO vehicles (user_name, plate, brand, year, color, renavam)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (vehicle.user_name, vehicle.plate, vehicle.brand, vehicle.year, vehicle.color, vehicle.renavam)
        self.execute_query(query, params)

    def get_vehicle_by_id(self, vehicle_id):
        query = "SELECT * FROM vehicles WHERE id = %s"
        result = self.fetch_results(query, (vehicle_id,))
        return result or "Vehicle not found."

    def get_vehicle_by_plate(self, plate):
        query = "SELECT * FROM vehicles WHERE plate = %s"
        result = self.fetch_results(query, (plate,))
        return result or "Vehicle not found."

    def get_vehicles_by_user_name(self, user_name):
        query = "SELECT * FROM vehicles WHERE user_name = %s"
        result = self.fetch_results(query, (user_name,))
        return result or "No vehicles found for this user."

    def update_vehicle(self, vehicle_id, updated_vehicle):
        query = """
        UPDATE vehicles SET user_name=%s, plate=%s, brand=%s, year=%s, color=%s, renavam=%s
        WHERE id=%s
        """
        params = (
            updated_vehicle.user_name, updated_vehicle.plate,
            updated_vehicle.brand, updated_vehicle.year,
            updated_vehicle.color, updated_vehicle.renavam, vehicle_id
        )
        self.execute_query(query, params)

    def delete_vehicle(self, vehicle_id):
        query = "DELETE FROM vehicles WHERE id = %s"
        self.execute_query(query, (vehicle_id,))

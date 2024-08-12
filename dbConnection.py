import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    # Constructor method to establish a connection with the MySQL database
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="vehicle_management"
            )
            # Create a cursor object to interact with the database
            self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error connecting to MySQL: {e}")

    # Method to execute a query (INSERT, UPDATE, DELETE)
    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            # Commit the transaction to save changes to the database
            self.connection.commit()
        except Error as e:
            print(f"Error executing query: {e}")

    # Method to fetch results from a SELECT query
    def fetch_results(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()
    
    # Method to close the cursor and connection to the database
    def close(self):
        self.cursor.close()
        self.connection.close()

    # CRUD Methods

    # Method to add a new vehicle to the database
    def add_vehicle(self, vehicle):
        query = """
        INSERT INTO vehicles (user_name, plate, brand, year, color, renavam)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        # Parameters are passed from the vehicle object
        params = (vehicle.user_name, vehicle.plate, vehicle.brand, vehicle.year, vehicle.color, vehicle.renavam)
        # Execute the INSERT query
        self.execute_query(query, params)

    # Method to retrieve a vehicle by its ID
    def get_vehicle_by_id(self, vehicle_id):
        query = "SELECT * FROM vehicles WHERE id = %s"
        # Fetch the vehicle data based on its ID
        result = self.fetch_results(query, (vehicle_id,))
        return result or "Vehicle not found."

    # Method to retrieve a vehicle by its plate number
    def get_vehicle_by_plate(self, plate):
        query = "SELECT * FROM vehicles WHERE plate = %s"
        # Fetch the vehicle data based on its plate
        result = self.fetch_results(query, (plate,))
        return result or "Vehicle not found."
    
    def get_vehicles_by_color(self, color):
        query = "SELECT * FROM vehicles WHERE color = %s"
        result = self.fetch_results(query, (color,))
        return result or "Vehicle not found."

    def get_all_vehicles(self):
        query = "SELECT * FROM vehicles"
        result = self.fetch_results(query)
        return result or "No vehicles found."


    
    # Method to update the details of an existing vehicle
    def update_vehicle(self, vehicle_id, updated_vehicle):
        query = """
        UPDATE vehicles SET user_name=%s, plate=%s, brand=%s, year=%s, color=%s, renavam=%s
        WHERE id=%s
        """
        # Parameters are passed from the updated vehicle object and vehicle ID
        params = (
            updated_vehicle.user_name, updated_vehicle.plate,
            updated_vehicle.brand, updated_vehicle.year,
            updated_vehicle.color, updated_vehicle.renavam, vehicle_id
        )
        # Execute the UPDATE query
        self.execute_query(query, params)

    # Method to delete a vehicle from the database
    def delete_vehicle(self, vehicle_id):
        query = "DELETE FROM vehicles WHERE id = %s"
        # Execute the DELETE query based on the vehicle ID
        self.execute_query(query, (vehicle_id,))

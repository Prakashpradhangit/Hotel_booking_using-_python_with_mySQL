import mysql.connector

# Function to establish database connection
def connect_to_database():
    passw = input("Enter password: ")
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=passw,
            database="HotelDB"
        )
        if connection.is_connected():
            print("Connected to HotelDB.")
        return connection
    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)
        return None

# Function to create the table if it doesn't exist
def createTable(connection):
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS HotelBookData (
            id BIGINT PRIMARY KEY,
            Name VARCHAR(100) NOT NULL,
            m_no BIGINT NOT NULL,
            address TEXT NOT NULL
        )
        """
        cursor.execute(create_table_query)
        print("Checked table: HotelBookData is ready.")
    except mysql.connector.Error as e:
        print("Error during table creation:", e)

# Function to insert guest data
def insertData(connection):
    try:
        id = int(input("Enter ID of guest: "))
        name = input("Enter guest name: ")
        m_no = int(input("Enter mobile no: "))
        adres = input("Enter address: ")

        cursor = connection.cursor()
        insert_query = "INSERT INTO HotelBookData (id, Name, m_no, address) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert_query, (id, name, m_no, adres))
        connection.commit()
        print("Guest data inserted successfully")
    except mysql.connector.Error as e:
        print("Error during data insertion:", e)

# Function to extract all guest data
def extractData(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM HotelBookData")
        records = cursor.fetchall()
        
        if records:
            print("Guest records from HotelBookData:\n")
            for row in records:
                print(f" ID: {row[0]}, \n Name: {row[1]}, \n Mobile No: {row[2]}, \n Address: {row[3]}")
        else:
            print("No records found in HotelBookData.\n")
    except mysql.connector.Error as e:
        print("Error during data retrieval:", e)

# Function to delete guest data by ID
def deleteData(connection):
    try:
        guest_id = int(input("Enter the ID of the guest to delete: "))
        cursor = connection.cursor()
        cursor.execute("DELETE FROM HotelBookData WHERE id = %s", (guest_id,))
        connection.commit()
        
        if cursor.rowcount > 0:
            print(f"Guest with ID {guest_id} deleted successfully.")
        else:
            print(f"No guest found with ID {guest_id}.")
    except mysql.connector.Error as e:
        print("Error during data deletion:", e)

# Function to search for a guest by ID or Name
def searchGuest(connection):
    try:
        criterion = input("Search by 'id' or 'name'? ").strip().lower()
        cursor = connection.cursor()

        if criterion == "id":
            guest_id = int(input("Enter the ID of the guest: "))
            cursor.execute("SELECT * FROM HotelBookData WHERE id = %s", (guest_id,))
        elif criterion == "name":
            guest_name = input("Enter the name of the guest: ").strip()
            cursor.execute("SELECT * FROM HotelBookData WHERE Name = %s", (guest_name,))
        else:
            print("Invalid criterion. Please choose 'id' or 'name'.")
            return
        
        records = cursor.fetchall()
        if records:
            print("Guest records found:")
            for row in records:
                print(f"ID: {row[0]}, Name: {row[1]}, Mobile No: {row[2]}, Address: {row[3]}")
        else:
            print("No matching records found.")
    except mysql.connector.Error as e:
        print("Error during guest search:", e)

# Main menu for program operation
def main():
    connection = connect_to_database()
    if connection is None:
        print("Failed to connect to the database. Exiting program.")
        return

    createTable(connection)  # Ensure table exists
    
    while True:
        print("\nMenu")
        print("1. Add guest")
        print("2. Guest list")
        print("3. Delete guest")
        print("4. Search guest")
        print("5. Exit")
        
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            insertData(connection)
        elif choice == 2:
            extractData(connection)
        elif choice == 3:
            deleteData(connection)
        elif choice == 4:
            searchGuest(connection)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")

    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

# Run the program
main()

# Hotel_booking_using-_python_with_mySQL


## Description

This is a Python-based program to manage hotel guest data using a MySQL database. It allows the user to perform the following operations:
- Add guest details.
- View the list of all guests.
- Search for a guest by ID or name.
- Delete a guest record by ID.

The program ensures the required table, `HotelBookData`, is created automatically if it does not already exist. It uses the `mysql.connector` library for database interaction and features a user-friendly, menu-driven interface.

---

## Features

1. **Add Guest**  
   Add new guest details, including:
   - ID  
   - Name  
   - Mobile number  
   - Address  

2. **View Guest List**  
   Retrieve and display all guest records stored in the database.

3. **Search for Guests**  
   Search for a guest using:
   - ID  
   - Name  

4. **Delete Guest**  
   Delete a guest record by providing their ID.

5. **Database Table Auto-Check**  
   The program ensures the `HotelBookData` table exists. If not, it creates the table automatically when the program starts.

---

## Prerequisites

1. **Python**  
   Ensure Python 3.x is installed.

2. **MySQL**  
   Install MySQL Server and ensure it is running.

3. **MySQL Connector for Python**  
   Install the required library by running:  
   ```
   pip install mysql-connector-python
   ```

4. **Database Setup**  
   - Create a database named `HotelDB` in MySQL.  
     Example:
     ```sql
     CREATE DATABASE HotelDB;
     ```

---

## How to Use

1. **Clone the Repository**  
   Download the program files or clone the repository using:  
   ```
   git clone <repository-url>
   ```

2. **Run the Program**  
   Execute the Python file in your terminal:  
   ```
   python <filename>.py
   ```

3. **Enter Your MySQL Credentials**  
   - The program will prompt you to enter the MySQL root password.  
   - Ensure the database `HotelDB` is accessible.

4. **Follow the Menu**  
   - Select operations from the menu to manage guest data.

---

## Database Structure

The program uses a single table, `HotelBookData`, with the following structure:

| Column Name  | Data Type  | Description            |
|--------------|------------|------------------------|
| `id`         | INT        | Unique guest ID       |
| `Name`       | VARCHAR(50)| Name of the guest     |
| `m_no`       | BIGINT     | Guest's mobile number |
| `address`    | VARCHAR(100)| Address of the guest  |

---

## Sample Program Flow

1. **Launch the Program**  
   ```
   Connected to HotelDB.
   ```

2. **Menu Example**  
   ```
   Menu
   1. Add guest
   2. Guest list
   3. Delete guest
   4. Search guest
   5. Exit
   Enter choice:
   ```

3. **Insert Data**  
   ```
   Enter ID of guest: 1
   Enter guest name: John Doe
   Enter mobile no: 9876543210
   Enter address: 123 Elm Street
   Guest data inserted successfully.
   ```

---

## Future Enhancements

- Add validation for input fields (e.g., phone number format).  
- Include pagination for guest lists.  
- Implement a graphical user interface (GUI).

---

## License

This project is open-source and free to use. Contributions are welcome!
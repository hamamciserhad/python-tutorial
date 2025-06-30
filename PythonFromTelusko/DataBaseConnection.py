"""
Tutorial: Connecting to a MySQL Database using Python

This script demonstrates how to:
1. Establish a connection to a MySQL database.
2. Create a cursor to interact with the database.
3. Execute a SQL query to retrieve all rows from the "student" table.
4. Print each row from the query result.
5. Close the cursor after use.

Make sure:
- You have the 'mysql-connector-python' package installed.
- Your MySQL server is running and accessible.
- The 'telusko' database and 'student' table exist.
"""

import mysql.connector  # Import the MySQL connector module

# Step 1: Connect to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",     # The hostname or IP address of the MySQL server
    user="root",          # The username used to access the database
    passwd="",   # The password for the user, must be filled!
    database="telusko"    # The name of the database to connect to
)

# Step 2: Create a cursor object to execute SQL commands
mycursor = mydb.cursor()

# Step 3: Execute a SQL query to select all records from the 'student' table
mycursor.execute("SELECT * FROM student")

# Step 4: Fetch all results from the executed query
result = mycursor.fetchall()

# Step 5: Loop through the result and print each record
for i in result:
    print(i)

# Step 6: Close the cursor to free up resources
mycursor.close()

import sqlite3

# Connect to the SQLite database (it will create the file if it doesn't exist)
connection = sqlite3.connect('DatabaseFile.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a table called StudentInfo
cursor.execute('''
    CREATE TABLE IF NOT EXISTS StudentInfo (
        StudentID INTEGER PRIMARY KEY,
        FirstName TEXT NOT NULL,
        LastName TEXT NOT NULL
    )
''')

# Commit the changes to the database
connection.commit()

# Close the connection
connection.close()

print("Database and table created successfully.")

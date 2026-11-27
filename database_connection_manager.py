# Write a class that acts as a context manager for handling a database-style connection (Don’t do actual database connection, simply printing “Connected” and “Disconnected”). Use the with statement to ensure the connection is closed even if an error occurs.

class DatabaseConnection:
    def __enter__(self):
        print("Connected")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Disconnected")
        return False

with DatabaseConnection() as db:
    print("Performing database operations...")
    raise ValueError("Something went wrong")

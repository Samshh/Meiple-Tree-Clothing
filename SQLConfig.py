import pyodbc

# Replace these placeholders with your actual database details
server = 'your_server_name'
database = 'your_database_name'
username = 'your_username'
password = 'your_password'

# Create a connection
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

# Create a cursor
cursor = conn.cursor()
cursor.close()
conn.close()

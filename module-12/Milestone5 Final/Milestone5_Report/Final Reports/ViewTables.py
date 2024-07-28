import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="WillsonFinancial"
)
cursor = conn.cursor()

# List all tables
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

for (table_name,) in tables:
    print(f"\nData from {table_name}:")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Close connection
conn.close()

import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="WillsonFinancial"
)
cursor = conn.cursor()

tables = ["Employees", "Clients", "Assets", "Transactions", "Billing"]
for table in tables:
    cursor.execute(f"SELECT * FROM {table}")
    print(f"Data from {table}:")
    for row in cursor.fetchall():
        print(row)
    print("\n")

# Close connection
conn.close()

import mysql.connector
from datetime import datetime

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="WillsonFinancial"
)
cursor = conn.cursor()

# Report: Clients with Highest Total Asset Value
cursor.execute("""
    SELECT c.Name, SUM(a.Value) AS TotalAssets
    FROM Clients c
    JOIN Assets a ON c.ClientID = a.ClientID
    GROUP BY c.ClientID
    ORDER BY TotalAssets DESC
""")
total_assets_clients = cursor.fetchall()
print(f"Clients with Highest Total Asset Value Report (Run on {datetime.now()}):")
for row in total_assets_clients:
    print(f"Client: {row[0]}, Total Assets: {row[1]}")

# Close connection
conn.close()

import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="willsonfinancial"
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

top_clients = cursor.fetchall()
print("Clients with Highest Total Asset Value Report:")
for row in top_clients:
    print(f"Client: {row[0]}, Total Assets: {row[1]:.2f}")

# Close connection
conn.close()

import mysql.connector
from datetime import datetime, timedelta

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="willsonfinancial"
)
cursor = conn.cursor()

# Calculate date one month ago
one_month_ago = datetime.now() - timedelta(days=30)
print(f"Checking for transactions since: {one_month_ago}")

# Report: Clients with High Transaction Volume
cursor.execute("""
    SELECT c.Name, COUNT(t.TransactionID) AS TransactionCount
    FROM Clients c
    JOIN Transactions t ON c.ClientID = t.ClientID
    WHERE t.TransactionDate >= %s
    GROUP BY c.ClientID
    HAVING TransactionCount > 10
""", (one_month_ago,))

high_volume_clients = cursor.fetchall()
print("Clients with High Transaction Volume Report:")
for row in high_volume_clients:
    print(f"Client: {row[0]}, Transactions: {row[1]}")

# Close connection
conn.close()

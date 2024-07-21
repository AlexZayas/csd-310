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

# Calculate date six months ago
six_months_ago = datetime.now() - timedelta(days=6*30)
print(f"Checking for clients added since: {six_months_ago}")

# Report: New Clients Added Per Month
cursor.execute("""
    SELECT DATE_FORMAT(JoinDate, '%Y-%m') AS Month, COUNT(ClientID) AS NewClients
    FROM Clients
    WHERE JoinDate >= %s
    GROUP BY Month
    ORDER BY Month
""", (six_months_ago,))

new_clients = cursor.fetchall()
print("New Clients Added Per Month Report:")
for row in new_clients:
    print(f"Month: {row[0]}, New Clients: {row[1]}")

# Close connection
conn.close()

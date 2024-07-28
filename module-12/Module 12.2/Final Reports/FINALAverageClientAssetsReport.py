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

# Report: Average Client Assets
cursor.execute("""
    SELECT AVG(Value) AS AverageAssets
    FROM Assets
""")
avg_assets = cursor.fetchall()
print(f"Average Client Assets Report (Run on {datetime.now()}):")
for row in avg_assets:
    print(f"{row[0]:.2f}")

# Close connection
conn.close()
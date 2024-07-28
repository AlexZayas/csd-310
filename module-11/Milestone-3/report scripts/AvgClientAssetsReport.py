import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password",
    database="willsonfinancial"
)
cursor = conn.cursor()

# Report: Average Client Assets
cursor.execute("""
    SELECT AVG(Value) AS AverageAssets
    FROM Assets
""")
avg_assets = cursor.fetchall()
print("Average Client Assets Report:")
for row in avg_assets:
    print(f"Average Assets: {row[0]:.2f}")

# Close connection
conn.close()

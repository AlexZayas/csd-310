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

# Update join dates to ensure they are within the last six months
cursor.execute("""
    UPDATE Clients
    SET JoinDate = %s
    WHERE ClientID IN (1, 2, 3, 4, 5)
""", (datetime.now() - timedelta(days=60),))

conn.commit()

# Close connection
conn.close()

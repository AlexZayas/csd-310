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

# Update transaction dates to ensure they are within the last month
cursor.execute("""
    UPDATE Transactions
    SET TransactionDate = %s
    WHERE TransactionID IN (1, 2, 3, 4, 5)
""", (datetime.now() - timedelta(days=15),))

conn.commit()

# Close connection
conn.close()

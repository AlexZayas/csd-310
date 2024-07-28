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

# Drop tables in the correct order
tables = ["Transactions", "Assets", "Billing", "Clients", "Employees"]
for table in tables:
    cursor.execute(f"DROP TABLE IF EXISTS {table}")

# Create tables
tables_creation = {
    "Employees": """
        CREATE TABLE Employees (
            EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255),
            Position VARCHAR(255),
            EmploymentType VARCHAR(50),
            HireDate DATE
        )
    """,
    "Clients": """
        CREATE TABLE Clients (
            ClientID INT AUTO_INCREMENT PRIMARY KEY,
            Name VARCHAR(255),
            ContactInfo VARCHAR(255),
            JoinDate DATE,
            Status VARCHAR(50)
        )
    """,
    "Assets": """
        CREATE TABLE Assets (
            AssetID INT AUTO_INCREMENT PRIMARY KEY,
            ClientID INT,
            AssetType VARCHAR(255),
            Value DECIMAL(15, 2),
            ValuationDate DATE,
            FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
        )
    """,
    "Transactions": """
        CREATE TABLE Transactions (
            TransactionID INT AUTO_INCREMENT PRIMARY KEY,
            ClientID INT,
            TransactionDate DATE,
            Amount DECIMAL(15, 2),
            Description VARCHAR(255),
            TransactionType VARCHAR(50),
            FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
        )
    """,
    "Billing": """
        CREATE TABLE Billing (
            BillingID INT AUTO_INCREMENT PRIMARY KEY,
            ClientID INT,
            BillingDate DATE,
            Amount DECIMAL(15, 2),
            BillingMethod VARCHAR(50),
            FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
        )
    """
}

# Execute table creation
for table_name, table_sql in tables_creation.items():
    cursor.execute(table_sql)

# Insert initial data
initial_data = {
    "Employees": [
        ("Jake Willson", "Financial Advisor", "Full-Time", "2020-01-01"),
        ("Ned Willson", "Financial Advisor", "Full-Time", "2020-01-01"),
        ("Phoenix Two Star", "Office Manager", "Full-Time", "2020-02-01"),
        ("June Santos", "Compliance Manager", "Part-Time", "2020-03-01")
    ],
    "Clients": [
        ("John Doe", "johndoe@example.com", "2023-01-01", "Active"),
        ("Jane Smith", "janesmith@example.com", "2023-02-01", "Active"),
        ("Alice Johnson", "alicejohnson@example.com", "2023-03-01", "Active"),
        ("Bob Brown", "bobbrown@example.com", "2023-04-01", "Active"),
        ("Charlie Davis", "charliedavis@example.com", "2023-05-01", "Active"),
        ("Sophia Garcia", "sophiagarcia@example.com", "2023-06-01", "Active"),
        ("Michael Thompson", "michael@example.com", "2023-07-01", "Active"),
        ("Laura Adams", "laura@example.com", "2023-08-01", "Active"),
        ("Emily White", "emily@example.com", "2023-09-01", "Active"),
        ("Daniel Harris", "daniel@example.com", "2023-10-01", "Active"),
        ("Olivia Clark", "olivia@example.com", "2023-11-01", "Active"),
        ("Ethan Lewis", "ethan@example.com", "2023-12-01", "Active"),
        # Adding more clients for recent months
        ("Grace Kim", "gracekim@example.com", "2024-01-01", "Active"),
        ("Lucas Brown", "lucasbrown@example.com", "2024-02-01", "Active"),
        ("Mia Martinez", "miamartinez@example.com", "2024-03-01", "Active"),
        ("Noah Wilson", "noahwilson@example.com", "2024-04-01", "Active"),
        ("Ava Lee", "avale@example.com", "2024-05-01", "Active"),
        ("Oliver Taylor", "olivertaylor@example.com", "2024-06-01", "Active"),
    ],
    "Assets": [
        (1, "Cash", 50000.00, "2023-06-01"),
        (1, "Investments", 100000.00, "2023-06-01"),
        (2, "Real Estate", 200000.00, "2023-06-01"),
        (3, "Cash", 30000.00, "2023-06-01"),
        (4, "Investments", 150000.00, "2023-06-01"),
        (5, "Real Estate", 250000.00, "2023-06-01"),
        (6, "Investments", 110000.00, "2023-06-01")
    ],
    "Transactions": [
        (1, "2023-06-01", 1000.00, "Investment Purchase", "Debit"),
        (1, "2023-06-15", 500.00, "Dividend", "Credit"),
        (2, "2023-06-05", 2000.00, "Property Purchase", "Debit"),
        (3, "2023-06-10", 1500.00, "Cash Deposit", "Credit"),
        (4, "2023-06-20", 3000.00, "Stock Purchase", "Debit"),
        (5, "2023-06-25", 2500.00, "Rental Income", "Credit"),
        (6, "2023-06-30", 1100.00, "Fixed Fee", "Debit"),
        (1, "2023-07-01", 2000.00, "Investment Purchase", "Debit"),
        (1, "2023-07-02", 1000.00, "Dividend", "Credit"),
        (2, "2023-07-05", 3000.00, "Property Purchase", "Debit"),
        (2, "2023-07-15", 1500.00, "Cash Deposit", "Credit"),
        (3, "2023-07-20", 4000.00, "Stock Purchase", "Debit"),
        (3, "2023-07-25", 3500.00, "Rental Income", "Credit"),
        # Adding more transactions to ensure clients have more than 10 transactions
        (1, "2023-07-03", 200.00, "Investment Purchase", "Debit"),
        (1, "2023-07-04", 500.00, "Dividend", "Credit"),
        (2, "2023-07-06", 1000.00, "Property Purchase", "Debit"),
        (2, "2023-07-07", 1500.00, "Cash Deposit", "Credit"),
        (3, "2023-07-08", 700.00, "Stock Purchase", "Debit"),
        (3, "2023-07-09", 400.00, "Rental Income", "Credit"),
        (3, "2023-07-10", 900.00, "Stock Purchase", "Debit"),
        (3, "2023-07-11", 600.00, "Rental Income", "Credit"),
        (3, "2023-07-12", 800.00, "Stock Purchase", "Debit"),
    ],
    "Billing": [
        (1, "2023-06-30", 500.00, "Fixed Fee"),
        (2, "2023-06-30", 1000.00, "Percentage of Assets"),
        (3, "2023-06-30", 300.00, "Fixed Fee"),
        (4, "2023-06-30", 750.00, "Percentage of Assets"),
        (5, "2023-06-30", 1250.00, "Fixed Fee"),
        (6, "2023-06-30", 1100.00, "Fixed Fee")
    ]
}

# Insert data into tables
for table_name, data in initial_data.items():
    placeholders = ", ".join(["%s"] * len(data[0]))
    cursor.executemany(
        f"INSERT INTO {table_name} VALUES (NULL, {placeholders})",
        data
    )

conn.commit()

# Close connection
conn.close()

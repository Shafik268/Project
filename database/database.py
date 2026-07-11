import sqlite3
from config import DATABASE_PATH


# -----------------------------
# DATABASE CONNECTION
# -----------------------------
def create_connection():
    return sqlite3.connect(DATABASE_PATH)


# -----------------------------
# CREATE TABLES
# -----------------------------
def create_tables():

    conn = create_connection()
    cursor = conn.cursor()

    # Emergency Reports Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            contact TEXT NOT NULL,

            disaster TEXT NOT NULL,

            location TEXT NOT NULL,

            urgency TEXT NOT NULL,

            description TEXT NOT NULL

        )
    """)

    # Resources Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resources (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            resource_name TEXT NOT NULL,

            quantity INTEGER NOT NULL

        )
    """)

    # Shelters Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shelters (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            address TEXT NOT NULL,

            capacity INTEGER NOT NULL

        )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# INSERT REPORT
# -----------------------------
def insert_report(
    name,
    contact,
    disaster,
    location,
    urgency,
    description
):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO reports
        (
            name,
            contact,
            disaster,
            location,
            urgency,
            description
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        contact,
        disaster,
        location,
        urgency,
        description
    ))

    conn.commit()
    conn.close()


# -----------------------------
# DASHBOARD FUNCTIONS
# -----------------------------
def get_total_reports():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM reports")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_resources():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM resources")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_total_shelters():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM shelters")

    total = cursor.fetchone()[0]

    conn.close()

    return total


def get_recent_reports():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            disaster,
            location,
            urgency
        FROM reports
        ORDER BY id DESC
        LIMIT 5
    """)

    reports = cursor.fetchall()

    conn.close()

    return reports


# -----------------------------
# INITIALIZE DATABASE
# -----------------------------
if __name__ == "__main__":

    create_tables()

    print("Database initialized successfully!")

    # -----------------------------
# INSERT RESOURCE
# -----------------------------
def insert_resource(resource_name, quantity):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO resources
        (
            resource_name,
            quantity
        )

        VALUES (?, ?)
    """, (

        resource_name,
        quantity

    ))

    conn.commit()

    conn.close()

    # -----------------------------
# GET ALL RESOURCES
# -----------------------------
def get_all_resources():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT

            id,

            resource_name,

            quantity

        FROM resources

        ORDER BY id DESC

    """)

    resources = cursor.fetchall()

    conn.close()

    return resources

# -----------------------------
# TOTAL RESOURCE QUANTITY
# -----------------------------
def get_total_resource_quantity():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""

        SELECT
            COALESCE(SUM(quantity),0)

        FROM resources

    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total
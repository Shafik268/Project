import sqlite3
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DATABASE_PATH


def create_connection():
    return sqlite3.connect(DATABASE_PATH)


def create_tables():

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        contact TEXT NOT NULL,

        disaster TEXT NOT NULL,

        location TEXT NOT NULL,

        urgency TEXT NOT NULL,

        description TEXT,

        status TEXT DEFAULT 'Pending',

        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        resource_name TEXT NOT NULL,

        quantity INTEGER,

        category TEXT

    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shelters(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        address TEXT,

        capacity INTEGER,

        available_beds INTEGER

    )
    """)

    conn.commit()

    conn.close()


if __name__ == "__main__":

    create_tables()

    print("Database Created Successfully")


def insert_report(
    name,
    contact,
    disaster,
    location,
    urgency,
    description
):
    """Insert a report into the reports table."""
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

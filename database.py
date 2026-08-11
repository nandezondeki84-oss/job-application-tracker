import sqlite3

def create_database():
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            position TEXT NOT NULL,
            status TEXT NOT NULL,
            date_applied TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

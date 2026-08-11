import sqlite3


def add_application(company, position, status, date_applied):
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO applications (company, position, status, date_applied)
        VALUES (?, ?, ?, ?)
    """, (company, position, status, date_applied))

    connection.commit()
    connection.close()

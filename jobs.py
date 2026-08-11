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


def get_applications():
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, company, position, status, date_applied
        FROM applications
        ORDER BY id DESC
    """)

    applications = cursor.fetchall()
    connection.close()

    return applications

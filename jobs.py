def search_applications(company):
    connection = sqlite3.connect("jobs.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, company, position, status, date_applied
        FROM applications
        WHERE company LIKE ?
        ORDER BY id DESC
    """, (f"%{company}%",))

    applications = cursor.fetchall()
    connection.close()

    return applications

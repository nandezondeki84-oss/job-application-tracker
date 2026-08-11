from database import create_database
from jobs import add_application, get_applications

create_database()

print("\nWelcome to the Job Application Tracker!")

while True:
    print("\n1. Add application")
    print("2. View applications")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        company = input("Company name: ")
        position = input("Job title: ")
        status = input("Application status: ")
        date_applied = input("Date applied: ")

        add_application(company, position, status, date_applied)
        print("Application saved successfully!")

    elif choice == "2":
        applications = get_applications()

        if not applications:
            print("No applications found.")
        else:
            print("\nYour applications:")

            for application in applications:
                print(
                    f"ID: {application[0]} | "
                    f"Company: {application[1]} | "
                    f"Position: {application[2]} | "
                    f"Status: {application[3]} | "
                    f"Date: {application[4]}"
                )

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")

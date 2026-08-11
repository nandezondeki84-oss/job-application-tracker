from database import create_database
from jobs import add_application

create_database()

print("Welcome to the Job Application Tracker!")

company = input("Company name: ")
position = input("Job title: ")
status = input("Application status: ")
date_applied = input("Date applied: ")

add_application(company, position, status, date_applied)

print("Application saved successfully!")

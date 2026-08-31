import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])

def add_expense():
    category = input("Enter Category: ").title()

    while True:
        try:
            amount = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Invalid amount. Try again.")

    date = datetime.now().strftime("%d-%m-%Y")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense Added Successfully!")

def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\nDate\t\tCategory\tAmount")
        print("-"*40)

        next(reader)

        for row in reader:
            print(f"{row[0]}\t{row[1]}\t\t₹{row[2]}")

def total_expense():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal Expense = ₹{total}")

def category_expense():
    category_dict = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in category_dict:
                category_dict[category] += amount
            else:
                category_dict[category] = amount

    print("\nCategory Wise Expense")

    for key, value in category_dict.items():
        print(f"{key} : ₹{value}")
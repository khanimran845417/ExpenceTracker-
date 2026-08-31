from expense_manager import *

create_file()

while True:

    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category Wise Expense")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        category_expense()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
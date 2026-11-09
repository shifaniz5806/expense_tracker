
expenses = []

def add_expense(name, amount, category, date):
    expense_details = {
        "name": name,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense_details)
    print("Expense added successfully!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print(expense)


def sum_expenses(n):
    if n == 0:
        return 0

    return expenses[n - 1]["amount"] + sum_expenses(n - 1)


def searchBy_category():
    search = input("Enter the category you want to search: ")
    found = False

    for expense in expenses:
        if expense["category"].lower() == search.lower():
            print(expense)
            found = True

    if found == False:
        print("Expense not found.")


def highest_expense():
    if len(expenses) == 0:
        print("No expenses recorded.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("Highest expense:", highest)


def expense_summary():
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n===== EXPENSE SUMMARY =====")

    for category, total in summary.items():
        print(category, ": Rs.", total)


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("Choose an option:")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Calculate total expenses")
    print("4. Search expenses by category")
    print("5. Find highest expense")
    print("6. View expense summary")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        date = input("Enter expense date: ")

        add_expense(name, amount, category, date)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        n = len(expenses)

        if n == 0:
            print("No expenses recorded.")
        else:
            total = sum_expenses(n)
            print("Total expenses: Rs.", total)

    elif choice == "4":
        searchBy_category()

    elif choice == "5":
        highest_expense()

    elif choice == "6":
        expense_summary()

    elif choice == "7":
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

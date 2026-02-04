from datetime import datetime

FILE_NAME = "expenses.txt"


def add_expense():
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.\n")
        return

    category = input("Enter category: ")
    note = input("Enter note: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount},{note}\n")

    print("Expense added successfully.\n")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nDate | Category | Amount | Note")
            print("-" * 40)
            for line in file:
                date, category, amount, note = line.strip().split(",")
                print(f"{date} | {category} | {amount} | {note}")
            print()
    except FileNotFoundError:
        print("No expenses found.\n")


def view_total():
    total = 0
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                _, _, amount, _ = line.strip().split(",")
                total += float(amount)
        print(f"\nTotal Expenses: {total}\n")
    except FileNotFoundError:
        print("No expenses found.\n")


def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            view_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()

import json
import os
from datetime import datetime

# File to store expense data
DATA_FILE = "expenses.json"

# Load existing expenses from file
def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (e.g., Food, Transport, Entertainment): ").strip()
        description = input("Enter a short description: ").strip()
        
        new_expense = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "amount": amount,
            "category": category,
            "description": description,
        }
        
        expenses = load_expenses()
        expenses.append(new_expense)
        save_expenses(expenses)
        
        print("Expense added successfully!")
    
    except ValueError:
        print("Invalid input! Please enter a numeric amount.")

# Generate expense summary
def generate_summary():
    expenses = load_expenses()
    category_summary = {}
    monthly_summary = {}

    for expense in expenses:
        month = expense["date"][:7]  # YYYY-MM format
        category = expense["category"]
        amount = float(expense["amount"])

        # Monthly summary
        monthly_summary[month] = monthly_summary.get(month, 0) + amount

        # Category summary
        if category not in category_summary:
            category_summary[category] = 0
        category_summary[category] += amount

    # Display summaries
    print("\nExpense Summary:")
    print("-" * 30)
    print("Monthly Expenses:")
    for month, total in monthly_summary.items():
        print(f"{month}: ₹{total}")

    print("\nCategory-wise Expenses:")
    for category, total in category_summary.items():
        print(f"{category}: ₹{total}")

# Main menu
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expense Summary")
        print("3. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            generate_summary()
        elif choice == "3":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()

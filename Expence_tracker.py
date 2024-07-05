import json
from datetime import datetime

# File to store expenses
EXPENSE_FILE = 'expenses.json'

# Load existing expenses from file
def load_expenses():
    try:
        with open(EXPENSE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to file
def save_expenses(expenses):
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses, amount, description, category):
    expense = {
        'amount': amount,
        'description': description,
        'category': category,
        'date': datetime.now().strftime('%Y-%m-%d')
    }
    expenses.append(expense)
    save_expenses(expenses)

# Display overall summary
def display_overall_summary(expenses):
    total_expense = sum(expense['amount'] for expense in expenses)
    print(f'Total Expenses: ₹{total_expense:.2f}')

    category_summary = {}
    for expense in expenses:
        category = expense['category']
        if category not in category_summary:
            category_summary[category] = 0
        category_summary[category] += expense['amount']

    print('Expenses by Category:')
    for category, total in category_summary.items():
        print(f'  {category}: ₹{total:.2f}')

# Display category-wise summary
def display_category_summary(expenses, categories):
    print("Choose a category to view summary:")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    category_choice = int(input("Enter category number: "))

    if 1 <= category_choice <= len(categories):
        selected_category = categories[category_choice - 1]
        category_expenses = [expense for expense in expenses if expense['category'] == selected_category]
        
        total_expense = sum(expense['amount'] for expense in category_expenses)
        print(f'Total Expenses for {selected_category}: ₹{total_expense:.2f}')

        print(f'Expenses in {selected_category}:')
        for expense in category_expenses:
            print(f"  {expense['date']} - {expense['description']}: ₹{expense['amount']:.2f}")
    else:
        print("Invalid category choice.")

# Display monthly summary
def display_monthly_summary(expenses):
    monthly_summary = {}
    for expense in expenses:
        month = expense['date'][:7]  # Extract YYYY-MM
        if month not in monthly_summary:
            monthly_summary[month] = 0
        monthly_summary[month] += expense['amount']

    print('Expenses by Month:')
    for month, total in monthly_summary.items():
        print(f'  {month}: ₹{total:.2f}')

# Main function
def main():
    expenses = load_expenses()
    categories = ['Food', 'Transportation', 'Entertainment', 'Utilities', 'Other']

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount in ₹: "))
                description = input("Enter description: ")
                print("Choose a category:")
                for i, category in enumerate(categories, 1):
                    print(f"{i}. {category}")
                category_choice = int(input("Enter category number: "))
                if 1 <= category_choice <= len(categories):
                    category = categories[category_choice - 1]
                    add_expense(expenses, amount, description, category)
                    print("Expense added successfully.")
                else:
                    print("Invalid category choice.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            print("\nView Summary")
            print("1. Category-wise Summary")
            print("2. Monthly Summary")
            print("3. Overall Summary")
            summary_choice = input("Choose an option: ")

            if summary_choice == '1':
                display_category_summary(expenses, categories)
            elif summary_choice == '2':
                display_monthly_summary(expenses)
            elif summary_choice == '3':
                display_overall_summary(expenses)
            else:
                print("Invalid choice. Please try again.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

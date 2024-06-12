from category import Category
from income import Income
from expense import Expense

def main_menu():
    while True:
        print("Personal Finance Manager")
        print("1. Manage Categories")
        print("2. Manage Incomes")
        print("3. Manage Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manage_categories()
        elif choice == '2':
            manage_incomes()
        elif choice == '3':
            manage_expenses()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_categories():
    while True:
        print("Manage Categories")
        print("1. Add Category")
        print("2. View All Categories")
        print("3. Find Category by ID")
        print("4. Delete Category")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter category name: ")
            category = Category(name)
            category.save()
            print(f"Category {name} added.")
        elif choice == '2':
            categories = Category.get_all()
            for cat in categories:
                print(cat)
        elif choice == '3':
            id = int(input("Enter category ID: "))
            category = Category.find_by_id(id)
            print(category)
        elif choice == '4':
            id = int(input("Enter category ID: "))
            category = Category.find_by_id(id)
            if category:
                category.delete()
                print(f"Category {id} deleted.")
            else:
                print("Category not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_incomes():
    while True:
        print("Manage Incomes")
        print("1. Add Income")
        print("2. View All Incomes")
        print("3. Find Income by ID")
        print("4. Delete Income")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            source = input("Enter income source: ")
            date = input("Enter income date: ")
            amount = float(input("Enter income amount: "))
            category_id = int(input("Enter category ID: "))
            income = Income(source, date, amount, category_id)
            income.save()
            print(f"Income from {source} added.")
        elif choice == '2':
            incomes = Income.get_all()
            for income in incomes:
                print(income)
        elif choice == '3':
            id = int(input("Enter income ID: "))
            income = Income.find_by_id(id)
            print(income)
        elif choice == '4':
            id = int(input("Enter income ID: "))
            income = Income.find_by_id(id)
            if income:
                income.delete()
                print(f"Income {id} deleted.")
            else:
                print("Income not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_expenses():
    while True:
        print("Manage Expenses")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Find Expense by ID")
        print("4. Delete Expense")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter expense description: ")
            date = input("Enter expense date: ")
            amount = float(input("Enter expense amount: "))
            category_id = int(input("Enter category ID: "))
            expense = Expense(description, date, amount, category_id)
            expense.save()
            print(f"Expense {description} added.")
        elif choice == '2':
            expenses = Expense.get_all()
            for expense in expenses:
                print(expense)
        elif choice == '3':
            id = int(input("Enter expense ID: "))
            expense = Expense.find_by_id(id)
            print(expense)
        elif choice == '4':
            id = int(input("Enter expense ID: "))
            expense = Expense.find_by_id(id)
            if expense:
                expense.delete()
                print(f"Expense {id} deleted.")
            else:
                print("Expense not found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

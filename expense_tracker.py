import json
import time

class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

class ExpenseTracker: 
    def __init__(self):
        self.expenses = [] 
    
    def add_expense(self, expense):
        self.expenses.append(expense)
    
    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully.")
        else:
            print("Invalid expense index.")
    
    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found.")
        else:
            print("Expense List:")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: ${expense.amount:.2f}")
    
    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: ${total:.2f}")
    
    def save_expenses(self, filename):
        with open(filename, "w") as file:
            json.dump([vars(expense) for expense in self.expenses], file)
    
    def load_expense(self, filename):
        try:
            with open(filename, 'r') as file:
                expenses_data = json.load(file)
                self.expenses = [Expense(**expense_data) for expense_data in expenses_data]
        except FileNotFoundError:
            print("No saved expenses found.")

    def self_destruct_fallacy(self, seconds):
        while seconds > 0:
            print(f"Self destructing in: {seconds}")
            time.sleep(1)
            seconds -= 1
        print("***BOOOOOOM****")  

    def secret_menu(self):
        print("Just kidding")
        time.sleep(3)
        print("Accessing secret link..")
        time.sleep(3)
        print("Copy and paste link to reveal the wonders for yourself: https://svs.gsfc.nasa.gov/14576/")

def main():
    tracker = ExpenseTracker()
    tracker.load_expense("expenses.json")

    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. Total Expenses")
        print("5. Save and Exit")
        print("6. Surprise function..")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            date = input("Enter the date (MM-DD-YYYY): ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            expense = Expense(date, description, amount)
            tracker.add_expense(expense)
            print("Expense added successfully") 
        
        elif choice == "2":
            index = int(input("Enter the expense index to remove: ")) - 1
            tracker.remove_expense(index)

        elif choice == "3":
            tracker.view_expenses()
        
        elif choice == "4":
            tracker.total_expenses()
        
        elif choice == "5":
            tracker.save_expenses("expenses.json")
            print("Expenses saved. Goodbye!")

        elif choice == "6":
            tracker.self_destruct_fallacy(7)
            tracker.secret_menu()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
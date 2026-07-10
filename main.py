import json
import os

FILE = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        # Corrupted or unreadable file — start fresh instead of crashing
        return []


def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)


def get_amount():
    while True:
        raw = input("Amount (or 'done' to cancel): ")
        if raw.lower() == "done":
            return None
        try:
            return float(raw)
        except ValueError:
            print("Please enter a number (e.g. 12 or 12.50).")


def summary_expenses(expenses):
    category_totals = {}
    for e in expenses:
        category = e["category"]
        amt = e["amount"]
        category_totals[category] = category_totals.get(category, 0) + amt
    print("Spending By Category:", category_totals)


CATEGORIES = ["food", "travel", "games", "bills", "shopping", "other"]

def get_category():
    while True:
        cat = input(f"Category{CATEGORIES}:").strip().lower()
        if cat in CATEGORIES:
            return cat.capitalize()
        
        print("Pick from the above categories list ")
            
def view_all(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses,1):
        print(f"{i}. {e['item']} | {e['category']} | {e['amount']:.2f}")



def add_expenses(expenses):
    what = input("What did you spend on: ").strip()
    if not what:
        print("Item can't be empty.")
        return
    
    category = get_category()

    amount_value = get_amount()

    if amount_value is None:
        print("Entry cancelled.")
        return
    
    if amount_value > 10000:
        print("Suggestion: Save upto 20%")

    expenses.append({"item": what , "category": category , "amount": amount_value})
    save_expenses(expenses)
    print("Expenses saved.")
    
expenses = load_expenses()

while True:
    print("\n1) Add expenses 2) View all 3) Category summary 4) Exit ")

    choice = input("> ").strip()

    if choice == "1":
        add_expenses(expenses)
    elif choice == "2":
        view_all(expenses)
    elif choice == "3":
        summary_expenses(expenses)
    elif choice == "4":
        total = sum(e["amount"] for e in expenses)
        print(f"\nTotal spent: {total:.2f}")
        break
    else:
        print("Pick 1,2,3,4.")

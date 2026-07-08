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
            
expenses = load_expenses()

while True:
    what = input("\nWhat did you spend on? (type 'done' to finish): ").strip()
    if what.lower() == "done":
        break
    if not what:
        print("Item name can't be empty.")
        continue

    category = get_category()

    amount_value = get_amount()
    if amount_value is None:
        print("Entry cancelled.")
        continue

    expenses.append({"item": what, "category": category, "amount": amount_value})
    save_expenses(expenses)  # save after each add so you don't lose data on crash

total = sum(e["amount"] for e in expenses)
print(f"\nTotal spent so far: {total:.2f}")

if total > 10000:
    print("Suggestion: Save up to 20%")

summary_expenses(expenses)

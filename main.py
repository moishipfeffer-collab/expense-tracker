from datetime import *
# from expenses import *
from rich.console import Console
from rich.table import Table
expenses = [
    {"Date": "2026-08-10", "Title": "Notebook", "Category": "school", "Amount": 24.90},
    {"Date": "2026-08-11", "Title": "Coffee", "Category": "food", "Amount": 12.00},
]


def ask_for_expense(expenses: list):
    Title=input("title: ")
    Category=input("category: ")
    Amount=input("amaount: ")
    add_expense(expenses,Title,Amount,Category)

def add_expense(expenses: list, title: str, amount: float,category: str):
    today=date.today()
    expenses.append({"Date":today, "Title":title, "Category":category,"Amount":amount})


def show_expenses(expenses: list):
    tab=Table()
    tab.add_column("Date")
    tab.add_column("Title")
    tab.add_column("Category")
    tab.add_column("Amount")
    for expense in expenses:
        tab.add_row(str(expense["Date"]),expense["Title"],expense["Category"],f"{float(expense["Amount"]):.2f}")
    Console().print(tab)
    Console().print(calculate_total(expenses),style="red")

def calculate_total(expenses: list):
    total=0
    if expenses == []:
        return 0
    else:
        for expense in expenses:
            total += int(expense["Amount"])
    return f"total: {total}"


def main():
    show_expenses(expenses)
    while True:
        add=input("do you want to add a expanse? ")
        if add=="yes":
            ask_for_expense(expenses)
            show_expenses(expenses)
        else:
            break
main()









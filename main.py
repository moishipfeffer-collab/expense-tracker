from datetime import *
from expenses import *
from rich.console import Console
from rich.table import Table
import questionary


def ask_for_expense(expenses: list):
    Title=questionary.text("title: ").ask()
    Category=questionary.select("category: ",choices=["food", "travel","school","entertainment","other"]).ask()
    Amount=questionary.text("amaount: ").ask()
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
        tab.add_row(str(expense["Date"]),str(expense["Title"]),str(expense["Category"]),f"{float(expense["Amount"]):.2f}")
    Console().print(tab)
    Console().print(calculate_total(expenses),style="green")

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
        add=questionary.select("do you want to add a expanse? ",choices=["yes","no"]).ask()
        if add=="yes":
            ask_for_expense(expenses)
            show_expenses(expenses)
        else:
            break
main()









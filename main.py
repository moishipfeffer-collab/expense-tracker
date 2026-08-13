from datetime import *
from expenses import *

def ask_for_expense(expenses: list):
    Title=input("title: ")
    Category=input("category: ")
    Amount=input("amaount: ")
    add_expense(expenses,Title,Amount,Category)

def add_expense(expenses: list, title: str, amount: float,category: str):
    today=date.today()
    expenses.append({"Date":today, "Title":title, "Category":category,"Amount":amount})


def show_expenses(expenses: list):
    for expense in expenses:
        print(f"{expense["Date"]} | {expense["Title"]} | {expense["Category"]} | {expense["Amount"]}")
    print(calculate_total(expenses))

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









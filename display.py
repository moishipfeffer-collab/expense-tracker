from datetime import *
from rich.console import Console
from rich.table import Table
from expense_tracker.config import CURRENCY,MONTHLY_BUDGET


def add_expense(expenses: list, title: str, amount: float,category: str):
    today=date.today()
    expenses.append({"Date":today, "Title":title, "Category":category,"Amount":amount})


def show_table(expenses: list):  
    tab=Table()
    tab.add_column("Date")
    tab.add_column("Title")
    tab.add_column("Category")
    tab.add_column("Amount")
    for expense in expenses:
        tab.add_row(str(expense["Date"]),str(expense["Title"]),str(expense["Category"]),f"{float(expense["Amount"]):.2f}{CURRENCY}")
    Console().print(tab)
    total=(calculate_total(expenses))
    Console().print(f"total: {total}",style="blue")
    if check_total(total):
        Console().print("you are breaking out of the mould",style="red")


def calculate_total(expenses: list):
    total=0
    if expenses == []:
        return 0
    else:
        for expense in expenses:
            total += int(expense["Amount"])
    return total

def check_total(total):
    if total>int(MONTHLY_BUDGET):
        return True

def show_catgory_total(expenses: list,category: str):
    print(calc_report(expenses)[category])
   
def show_report(expenses: list):
    print(calc_report(expenses))
    total=(calculate_total(expenses))
    if check_total(total):
        Console().print("you are breaking out of the mould",style="red")


def calc_report(expenses: list):
    total_report={}
    food=0
    travel=0
    school=0
    entertainment=0
    other=0
    for expense in expenses:
        match expense["Category"]:
            case "food":
                food+=float(expense["Amount"])
            case "travel":
                travel+=float(expense["Amount"])
            case "school":
                school+=float(expense["Amount"])
            case "entertainment":
                entertainment+=float(expense["Amount"])
            case "entertainment":
                other+=float(expense["Amount"])
        total_report={"food":food,"travel":travel,
                      "school":school,
                      "entertainment":entertainment,
                      "other":other}
    return total_report
def show_message():
    print(f"expens added successfully!")  












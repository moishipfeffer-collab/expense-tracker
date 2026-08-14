from display import *
from storage import *
import typer
app=typer.Typer()
expenses=load_expenses()
@app.command()
def add(title: str,amount: float,category: str):
    add_expense(expenses,title,amount,category)
    save_expenses(expenses)
    show_message()
@app.command()
def list():
    show_table(expenses)

@app.command()
def category(category):
    show_report(expenses,category)

@app.command()
def report():
    show_report(expenses)

if __name__ == "__main__":
    app()
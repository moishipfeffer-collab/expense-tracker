import yaml

def save_expenses(expenses):
    with open("expenses.yaml","w") as file:
        yaml.safe_dump(expenses,file)

def load_expenses():
    try:
        with open ("expenses.yaml","r") as file:
            expenses=yaml.safe_load(file)
            if expenses is None:
                return []
            return expenses
    except FileNotFoundError:
        return []
        



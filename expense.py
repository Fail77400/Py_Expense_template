from PyInquirer import prompt
from prompt_toolkit.validation import ValidationError, Validator
import csv
from user import add_user

class userValidator(Validator):
    ## Used to check if user exist in our users.csv
    def validate(self, current):
        with open('users.csv', 'r+', newline='') as users:
            reader = csv.reader(users, quoting=csv.QUOTE_MINIMAL)  
            ok = False
            for row in reader:
                for user in row:
                    if current.text == user:
                        ok = True
            if ok == False:
                raise ValidationError(message='please enter a valid user', cursor_position=len(current.text))

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
        "validate": lambda val: val.isnumeric(),
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "validate": userValidator
    },
    {
        "type":"input",
        "name":"involved",
        "message":"New Expense - involveds",
        "validate": userValidator
    }
]


def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a+', newline='') as expense, open('users.csv', 'r+', newline='') as users:
        writer = csv.writer(expense, quoting = csv.QUOTE_MINIMAL)
        writer.writerow([infos['amount'], infos['label'], infos['spender'], infos['involved']])
        print("Expense Added !")
    return True

def show_status(*args):
    with open('expense_report.csv','r+', newline='') as expense:
        reader = csv.reader(expense, quoting = csv.QUOTE_MINIMAL)
        users = []
        for row in reader:
            if row[2] not in users:
                users.append(row[2])
        print(users)
        global_balance = []
        for user in users:
            balance = 150000
            for row in reader:
                print(row)
                if user == row[2]:
                    balance -= row[0]
            global_balance.append([user, balance])
        print(global_balance)
    return True

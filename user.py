from PyInquirer import prompt
import csv 

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"What's your name ?",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    option = prompt(user_questions)
    with open('users.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting = csv.QUOTE_MINIMAL)
        writer.writerow([option['name']])
        print(option['name'] + ' added !')
    return
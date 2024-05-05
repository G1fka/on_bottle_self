import datetime, json
# import pdb

from bottle import post, request
import re

pattern = r"[a-zA-Z]+[a-zA-Z0-9.\-_]{1,50}@[a-zA-Z]{3,10}(\.{1}[a-z]{2,5})+"  # Регулярное выражение

@post('/home', method='post')  # Обработка POST-запроса
def my_form():
    username = request.forms.get('USERNAME')  # Получение логина
    question = request.forms.get('QUEST')  # Получение вопроса
    mail = request.forms.get('ADRESS')  # Получение электронной почты

    if username == '' or mail == '' or question == '':  # Проверка на пустые поля
        return "Fill all the spaces"

    if len(question) <= 3:
        return "Questions must be at least 3 symbols!"

    if re.fullmatch(r"[0-9]+", question):
        return "Question can't contain only digits!"

    # dictionary = {mail: {username, question}}
    # pdb.set_trace()

    if check(mail):  # Проверка на соответствие шаблону
        with open('data.txt') as file:
            try:
                data = json.load(file)
            except:
                data = {}

        if mail in data.keys():
            if username != data[mail][0]:
                return f"User with this email already exists!"
            if question in data[mail]:
                return f"Thanks, {username}! The answer have been asked before"
            data[mail].append(question)
        else:
            data[mail] = [username, question]

        with open('data.txt', 'w') as file:
            json.dump(data, file)
        return f"Thanks, {username}! The answer will be sent to the mail {mail} | Access Date: {datetime.date.today()}"
    return "Invalid email!"

def check(mail: str) -> bool:
    if re.fullmatch(pattern, mail):
        return True
    return False

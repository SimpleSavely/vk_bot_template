from flask import Flask, render_template, request, json, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from settings import *
from behavior import *
import message_handler
import vk_api

app = Flask(__name__)

# Подключение к бд, тупо шаблон
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
                                                                                                        username="perfectrum",
                                                                                                        password="qwertyuiop",
                                                                                                        hostname="perfectrum.mysql.pythonanywhere-services.com",
                                                                                                        databasename="perfectrum$Main",
                                                                                                            )
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Функция определения бд
lm = SQLAlchemy(app)

# Класс для работы с таблицей Last_messages
class Last_message(lm.Model):
    __tablename__ = "Last_messages"

    # Названия колонок и типы значений в них
    id = lm.Column(lm.Integer,primary_key=True)
    user_id = lm.Column(lm.Integer)
    message = lm.Column(lm.String(4096))

@app.route('/', methods=['POST'])
def processing():
    data = json.loads(request.data)

    if data['type'] == 'confirmation':
        return confirmation_token

    elif data['type'] == 'message_new':
        user_id = data['object']['user_id']
        if user_id > 0:   # если пришло сообщение от пользователя
            body = data['object']['body']

            check = Last_message.query.filter_by(user_id=user_id).all()

            if len(check) == 0:
                tab = Last_message(user_id=user_id,message=start_message_id) # Присваиваем каждому столбцу значение
                lm.session.add(tab) # Добавляем в таблицу
                lm.session.commit() # Закрываем транзакцию
                last_message = start_message_id
            elif len(check) == 1:
                last_message = check[0].message


            # сюда будем вписывать реакции на сообщения пользователя
            if behavior[last_message]['type'] == 0:
                message = message_handler.simple(data, last_message)
                Last_message.query.filter_by(user_id=user_id).update({'message':message})
                lm.session.commit()


        return 'ok'

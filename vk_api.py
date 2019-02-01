import requests
import vk, json

from settings import *

session = vk.Session()
api = vk.API(session, v=5.0)

def get_button(label, color):
    button = {
        'action': {
            'type': 'text',
            'label': label
        },
        'color': color
    }
    return button

empty_keyboard = {
    "one_time": False,
    "buttons": []
    }
empty_keyboard = json.dumps(empty_keyboard, ensure_ascii=False).encode('utf-8')
empty_keyboard = str(empty_keyboard.decode('utf-8'))

def get_keyboard(labels):
    keyboard = {
        'one_time': False,
        'buttons': [[get_button(label=l, color='primary')] for l in labels]
        }
    keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
    keyboard = str(keyboard.decode('utf-8'))
    return keyboard

def send_message(user_id, token, message, labels=[], attachment=""):
    if labels == []:
        api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment, keyboard=empty_keyboard)
    else:
        api.messages.send(access_token=token, user_id=str(user_id), message=message, attachment=attachment, keyboard=get_keyboard(labels))

error_message = 'Я вас не понимаю.'

start_message_id = 'familiarity'
first_message_id = 'familiarity'

behavior = {
    'familiarity': {
        'text': 'Привет! Я шаблонный бот, созданный пользователями https://vk.com/perfectrum и https://vk.com/simplesavely. Можете посмотреть мои исходники или написать мне что-нибудь в базу данных.',
        'type': 0,
        'expect': ['Покажи исходники', 'Запиши в БД'],
        'children': ['code', 'db']
        },
    'options': {
        'text': 'Можете посмотреть мои исходники или написать мне что-нибудь в базу данных.',
        'type': 0,
        'expect': ['Покажи исходники', 'Запиши в БД'],
        'children': ['code', 'db']
        },
    'code': {
        'text':'Репозиторий с моими исходниками лежит по ссылке: ',
        'type': 0,
        'expect':['назад'],
        'children':['options']
        },
    'db':{
        'text':'Что мне записать?',
        'type': 1,
        'expect':[],
        'children':['got_it']
            },
    'got_it': {
        'text': 'Записал, спасибо!',
        'type': 0,
        'expect': ['Назад'],
        'children': ['options']
        }
    }

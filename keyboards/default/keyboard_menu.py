from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='О нас'),
            KeyboardButton(text='Контакты'),
        ],
        [
            KeyboardButton(text='Онлайн запись'),
        ],
        [
            KeyboardButton(text='Адрес'),

        ]
    ],
    resize_keyboard=True
)


doctors_menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='Елена'),
            KeyboardButton(text='Александр'),
        ],
        [
            KeyboardButton(text='Виталий'),
            KeyboardButton(text='Инна'),
        ],
        [
            KeyboardButton(text='Анна'),
            KeyboardButton(text='Назад')
        ],

    ],
    resize_keyboard=True
)


elena_menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text='10.00'),
            KeyboardButton(text='15.00'),
        ],
        [
            KeyboardButton(text='18.00'),
            KeyboardButton(text='19.00'),
        ],
        [
            KeyboardButton(text='20.00'),
            KeyboardButton(text='Назад')
        ],

    ],
    resize_keyboard=True
)

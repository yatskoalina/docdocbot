from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ikb_menu2 = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Сообщение', callback_data='Сообщение'),
                                        InlineKeyboardButton(text='Ссылка', url='https://www.youtube.com/watch?v=v1F3yluMWbk')
                                    ]

                                ])
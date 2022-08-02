from aiogram import types

from filters import IsPrivate
from loader import dp
from utils.db_api import quick_commands as commands
from utils.misc import rate_limit


@rate_limit(limit=15)
@dp.message_handler(IsPrivate(), text='Онлайн запись')
async def command_start(message: types.Message):
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привет{user.first_name}\n'
                                 f'Ты уже зарегистрирован')
        elif user.status == 'banned':
            await message.answer('Вы в бане')
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active')
        await message.answer('Вы зарегистрированы')


@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/ban')
async def get_ban (message: types.Message):
    await commands.update_status(message.from_user.id, 'baned')
    await message.answer('Бан')

@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/unban')
async def get_unban (message: types.Message):
    await commands.update_status(message.from_user.id,'active')
    await message.answer('Разбан')

@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/profile')
async def get_unban (message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await message.answer(f'Айди - {user.user_id}\n'
                         f'first_name - {user.first_name}\n'
                         f'last_name - {user.last_name}\n'
                         f'username - {user.username}\n'
                         f'status - {user.status}')


from aiogram import types

from keyboards.default import kb_menu
from loader import dp

from filters import IsPrivate
from utils.misc import rate_limit


@rate_limit(limit=15)
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'Выбери действие', reply_markup=kb_menu)
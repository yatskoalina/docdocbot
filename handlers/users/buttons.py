from aiogram import types

from keyboards.default import kb_menu
from keyboards.default.keyboard_menu import doctors_menu, elena_menu
from loader import dp


@dp.message_handler(text='О нас')
async def buttons_test(message: types.Message):
    await message.answer('Если вы находитесь в поисках высококвалифицированного врача,'
                         ' который использует в работе только новое современное оборудование — добро пожаловать в медицинский центр!'
                         ' Мы уже более 26 лет оказываем широкий спектр медицинских услуг по по диагностике и лечению заболеваний.')

@dp.message_handler(text='Контакты')
async def buttons_test(message: types.Message):
    await message.answer(f'+375-44-444-44-44\n+375-33-333-33-33')

@dp.message_handler(text='Онлайн запись')
async def buttons_test(message: types.Message):
    await message.reply('Выберите врача', reply_markup=doctors_menu)

@dp.message_handler(text='Адрес')
async def buttons_test(message: types.Message):
    await message.answer('Минская, 22')

@dp.message_handler(text='Назад')
async def buttons_test(message: types.Message):
    await message.reply('Меню', reply_markup=kb_menu)


@dp.message_handler(text='Елена')
async def buttons_test(message: types.Message):
    await message.reply('Запись к Елене', reply_markup=elena_menu)

@dp.message_handler(text='10.00')
async def buttons_test(message: types.Message):
    await message.answer('Вы записаны!')


@dp.message_handler(text='18.00')
async def buttons_test(message: types.Message):
    await message.answer('Вы записаны!')

@dp.message_handler(text='20.00')
async def buttons_test(message: types.Message):
    await message.answer('Вы записаны!')

@dp.message_handler(text='15.00')
async def buttons_test(message: types.Message):
    await message.answer('Вы записаны!')

@dp.message_handler(text='19.00')
async def buttons_test(message: types.Message):
    await message.answer('Вы записаны!')



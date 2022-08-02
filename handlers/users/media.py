from aiogram.types import ContentType, Message, InputFile, MediaGroup

from loader import dp


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    chat_id = message.from_user.id


    photo_url = 'sf'
    photo_bytes = InputFile(path_or_bytesio='media/photo1.jpg')

    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes)

@dp.message_handler(text='/album')
async def send_album(message: Message):
    album = MediaGroup()

    photo_bytes = InputFile(path_or_bytesio='media/photo1.jpg')


    album.attach_photo(photo=photo_bytes, caption='Котик')


    await message.answer_media_group(media=album)
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters.command import Command
from transliterate import translit

TOKEN = os.getenv('TOKEN')
bot = Bot(token='7471125756:AAEHw_ZVFA1_8-8i2P15jYKaUTT_t-LP7Ow')
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет,{user_name}! Введи свое ФИО'
    logging.info(f'{user_name} {user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)

@dp.message()
async def send_transliteration(message: types.Message):
    text = message.text
    transliterated_text = translit(text, 'ru', reversed=True)
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    logging.info(f'{user_name} {user_id}: {text} -> {transliterated_text}')
    response_text = f'Ваше ФИО на английском: {transliterated_text}'
    await message.answer(response_text)
if __name__ == '__main__':
    dp.run_polling(bot)

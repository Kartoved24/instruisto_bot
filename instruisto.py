from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from config import TOKEN_API
from random import random

HELP_COMMAND  = """
<strong>/help</strong> - <em>список команд</em>
<strong>/start</strong> - <em>запустить бота</em>
<strong>/contact</strong> - <em>связаться с разработчиком</em>"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
kb = ReplyKeyboardMarkup()
kb.add(KeyboardButton('/help'))


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode='HTML', reply_markup=kb)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    pass

@dp.message_handler(commands=['contact'])
async def contact(message: types.Message):
    pass



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

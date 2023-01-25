from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN_API
from random import random

HELP_COMMAND = """
/help - список комманд
/start - запустить бота"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
ikb = InlineKeyboardMarkup(row_width=2)
ikb1 = InlineKeyboardButton(text='bla',
                            url='ya.ru')
ikb.add(ikb1)

@dp.message_handler(commands=['links'])
async def send_links(message: types.Message):
    await bot.send_message(text='Ссылки',
                           reply_markup=ikb)

if __name__ == '__main__':
    executor.start_polling(dp)

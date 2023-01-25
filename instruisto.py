from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN_API
from random import random

HELP_COMMAND = """Привет, эсперантист! Я бот-преподаватель языка <strong>Эсперанто</strong>. Я помогу тебе выучить этот прекрасный язык, расскажу много интересного и полезного об Эсперанто. Ознакомься с моими командами ниже:

<strong>/help</strong> - <em>список команд</em>
<strong>/start</strong> - <em>запустить бота</em>
<strong>/contact</strong> - <em>связаться с разработчиком</em>
<strong>/links</strong> - <em>полезные ссылки</em>"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/help')).add(KeyboardButton('/start')).add(KeyboardButton('/contact')).add(KeyboardButton('/links'))

ikb = InlineKeyboardMarkup(row_width=2)
ikb1 = InlineKeyboardButton(text='Связаться с разработчиком',
                            url='https://t.me/kartoved')
ikb.add(ikb1)

ikb_links = InlineKeyboardMarkup(row_width=1)
dictionary_button = InlineKeyboardButton(text='Словарь Кондратьева',
                            url='rueo.ru')
chat_button = InlineKeyboardButton(text='Чат эсперантистов в Telegram',
                            url='https://t.me/Esperantujoo')
ikb_links.add(dictionary_button, chat_button)


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode='HTML', reply_markup=kb)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode='HTML', reply_markup=kb)

@dp.message_handler(commands=['contact'])
async def contact(message: types.Message):
    await message.answer(text='Пиши мне про баги и слова благодарности 🥳',
                         reply_markup=ikb)

@dp.message_handler(commands=['links'])
async def get_useful_links(message: types.Message):
    await message.answer(text='Полезные ссылки',
                         reply_markup=ikb_links)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from keyboards import *

HELP_COMMAND = """Привет, эсперантист! Я бот-преподаватель языка <strong>Эсперанто</strong>. Я помогу тебе выучить этот прекрасный язык, расскажу много интересного и полезного об Эсперанто. Ознакомься с моими командами ниже:

<strong>/help</strong> - <em>список команд</em>
<strong>/start</strong> - <em>запустить бота</em>
<strong>/contact</strong> - <em>связаться с разработчиком</em>
<strong>/links</strong> - <em>полезные ссылки</em>"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode='HTML', reply_markup=kb)

@dp.message_handler(commands=['contact'])
async def contact_command(message: types.Message):
    await message.answer(text='Пиши мне про баги и слова благодарности 🥳',
                         reply_markup=ikb)

@dp.message_handler(commands=['links'])
async def get_useful_links_command(message: types.Message):
    await message.answer(text='Полезные ссылки',
                         reply_markup=ikb_links)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

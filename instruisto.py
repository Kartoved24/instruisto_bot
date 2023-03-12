from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hspoiler
import json
from config import TOKEN_API
from keyboards import *

HELP_COMMAND = """Привет, эсперантист! Я бот-преподаватель языка <strong>Эсперанто</strong>. Я помогу тебе выучить этот прекрасный язык, расскажу много интересного и полезного об Эсперанто. Ознакомься с моими командами ниже:

<strong>/help</strong> - <em>список команд</em>
<strong>/start</strong> - <em>запустить бота</em>
<strong>/contact</strong> - <em>связаться с разработчиком</em>
<strong>/links</strong> - <em>полезные ссылки</em>"""

bot = Bot(TOKEN_API, parse_mode='HTML')
dp = Dispatcher(bot)

# импортируем список слов из общего неизменяемого списка слов в личный изменяемый список слов

with open('list_of_unstudied.json') as file_of_unstudied:
    list_of_unstudied = json.load(file_of_unstudied)
    print(list_of_unstudied)


def add_to_studied_words(new_word):
    with open('list_of_studied_words.json', 'a', encoding='utf=8') as file_of_studied:
        json.dump(new_word, file_of_studied, ensure_ascii=False)

def delete_word_from_unstudied():
    with open('list_of_unstudied.json', 'w', encoding='utf-8') as file_of_unstudied:
        json.dump(list_of_unstudied, file_of_unstudied, ensure_ascii=False)


@dp.message_handler(commands=['start', 'help'])
async def start_command(message: types.Message):
    await message.answer(text=HELP_COMMAND,  reply_markup=kb)


@dp.message_handler(commands=['contact'])
async def contact_command(message: types.Message):
    await message.answer(text='Пиши мне про баги и слова благодарности 🥳',
                         reply_markup=ikb)


@dp.message_handler(commands=['links'])
async def get_useful_links_command(message: types.Message):
    await message.answer(text='Полезные ссылки',
                         reply_markup=ikb_links)


@dp.message_handler(commands='training')
async def get_one_word(message: types.Message):
    new_word = list_of_unstudied.pop(0)
    add_to_studied_words(new_word)
    list_of_keys = list(new_word)
    await message.answer(text=f'Как будет <strong>"{list_of_keys[0]}"</strong> на Эсперанто?\n\
Ответ: <b>{hspoiler(new_word[list_of_keys[0]])}</b>\n\
Пример предложения:\n <em>{hspoiler(new_word[list_of_keys[1]])}</em>', reply_markup=ikb_guess)
    delete_word_from_unstudied()



@dp.callback_query_handler()
async def forgot_word(callback: types.CallbackQuery):
    if callback.data == 'remember':
        await callback.answer('красавчик')
    elif callback.data == 'forget':
        await callback.answer('ну и лох')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

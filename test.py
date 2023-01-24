from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN_API
from random import random

HELP_COMMAND = """
/help - список комманд
/start - запустить бота"""

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=['give'])
async def give_cat(message: types.Message):
    await message.reply(text='Лови малыша Грогу!')
    await bot.send_sticker(message.from_user.id, sticker='CAACAgIAAxkBAAEHaBJjzyGJyPHvKfo5XCejPoL92CHOYAACeAIAAladvQr8ugi1kX0cDC0E')

if __name__ == '__main__':
    executor.start_polling(dp)

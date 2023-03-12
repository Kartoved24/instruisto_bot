from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/help')).add(KeyboardButton('/start')
                                    ).add(KeyboardButton('/contact')).add(KeyboardButton('/links'))

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

ikb_guess = InlineKeyboardMarkup(row_width=2)
remember_btn = InlineKeyboardButton(text='Помню',
                                    callback_data='remember',)
forget_btn = InlineKeyboardButton(text='Забыл',
                                  callback_data='forget',)
ikb_guess.add(remember_btn, forget_btn)
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

tg_bot_token = '5163185542:AAG96jJfS85lftHx4F1BBozDTJBLncC1h28'

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

page = 1
main_request = requests.get(f'https://rickandmortyapi.com/api/character?page'
                            f'={page}')
all_data = main_request.json()
characters_raw = all_data['results']
next_page_url = all_data['info']['next']
prev_page_url = all_data['info']['prev']
characters = {}
characters_names = []


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    button1 = KeyboardButton('1️⃣')
    button2 = KeyboardButton('2️⃣')
    button3 = KeyboardButton('3️⃣')
    markup4 = ReplyKeyboardMarkup().row(
        button1, button2, button3
    ).add(KeyboardButton('Средний ряд'))
    button4 = KeyboardButton('4️⃣')
    button5 = KeyboardButton('5️⃣')
    button6 = KeyboardButton('6️⃣')
    markup5 = ReplyKeyboardMarkup()
    markup5.row(button4, button5)
    markup5.insert(button6)
    await message.answer("Rick and Morty", reply_markup=markup5)



# for name in characters_raw:
#     characters_names.append((name['name']))
# for id in characters_raw:
#     characters[id['id']] = id

executor.start_polling(dp)
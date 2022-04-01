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
    markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
    ).add(
        KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
    )
    await message.answer("Rick and Morty", reply_markup=markup_request)



# for name in characters_raw:
#     characters_names.append((name['name']))
# for id in characters_raw:
#     characters[id['id']] = id

executor.start_polling(dp)
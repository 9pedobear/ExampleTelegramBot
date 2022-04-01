import requests
from pprint import pprint as pp
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

tg_bot_token = '5163185542:AAG96jJfS85lftHx4F1BBozDTJBLncC1h28'

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

page = input("Введите номер страницы: ")
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
    await message.answer("Rick and Morty")


for name in characters_raw:
    characters_names.append((name['name']))

for id in characters_raw:
    characters[id['id']] = id


executor.start_polling(dp)
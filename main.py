import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.utils.markdown import text, bold
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


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
    inline_btn_1 = InlineKeyboardButton('Первая кнопка!',
                                        callback_data='button1')
    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
    await message.answer("Rick and Morty", reply_markup=inline_kb1)

@dp.callback_query_handler()
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')


# for name in characters_raw:
#     characters_names.append((name['name']))
# for id in characters_raw:
#     characters[id['id']] = id

executor.start_polling(dp)
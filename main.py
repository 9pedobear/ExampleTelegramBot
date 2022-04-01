import requests
from pprint import pprint as pp

page = input("Введите номер страницы: ")
main_request = requests.get(f'https://rickandmortyapi.com/api/character?page'
                            f'={page}')

all_data = main_request.json()
characters_raw = all_data['results']
next_page_url = all_data['info']['next']
prev_page_url = all_data['info']['prev']
characters = {}
characters_names = []

for name in characters_raw:
    characters_names.append((name['name']))

pp(characters_names)


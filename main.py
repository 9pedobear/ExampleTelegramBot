import requests
from pprint import pprint as pp

page = input("Введите номер страницы: ")
main_request = requests.get(f'https://rickandmortyapi.com/api/character?page'
                            f'={page}')

all_data = main_request.json()
characters_raw = all_data['results']
pp(characters_raw)


import requests


page = input("Введите номер страницы: ")
main_request = requests.get(f'https://rickandmortyapi.com/api/character?page'
                            f'={page}')

print(main_request.json())
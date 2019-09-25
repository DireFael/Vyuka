# Přednáška 3.

import json

from utils import vypis_tah
#import utils


'''
for tah in range(1,6):

		vysledek = vypis_tah(tah)
		print(f'Celkovy vysledek tahu č.{tah} je {vysledek}')
'''
'''
name_file = 'data'

file_path = f'{name_file}.json'

with open(file_path, 'r') as file_handler:
	json_data = json.load(file_handler)


for item in json_data:

	vek = json_data[item]['vek']
	pohlavi = json_data[item]['pohlavi']
	stav = json_data[item]['stav']

	print(f'Jméno: {item}')
	print(f'	Věk: {vek}')
	print(f'	Pohlaví: {pohlavi}')
	print(f'	Stav: {stav}')

#print(json_data)
'''

file_path = 'temp_data.txt'

with open(file_path, 'r') as file_handler:
	file_data = file_handler.read()
	file_handler.close()

print(file_data)


with open(file_path, 'r') as file_handler:
	for line in file_handler:
		print(line)

	file_handler.close()


with open(file_path, 'r') as file_handler:
	file_data = file_handler.readlines()

	print(file_data)

	for item in file_data:
		data = item.strip('\n')
		print(data)

#print(file_data)


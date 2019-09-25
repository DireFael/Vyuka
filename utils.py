#utils lib

import random

def vypis_tah(tah):

	vysledek = 0

	for i in range(1,4):
		cislo = random.randint(1,30)
		vysledek += cislo
		print(f'Hodil si č.{cislo} v sadě č.{i} v tahu č.{tah}')

	return vysledek


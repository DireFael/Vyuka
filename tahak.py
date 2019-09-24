# Tahák.py
# Tento soubor slouží jako vyukový tahák pro úplné začátky programování v python 3.6+
# Soubor je neustále ve vývoji a mohou se v něm nacházet chyby.
# Případné chyby či podměty co do souboru přidat hlaste na emailu
# Autor: Martin K. <graffitys@gmail.com>



##########################################################################################################################
##########                                             Datové typy                                              ##########
##########################################################################################################################

# Obecně můžeme dělíme datové typy na dvě podmnožiny. Na jednoduché datové typy a strukturované datové typy.
# Jednoduché datové typy umožnují uchovávat pouze jednu hodnotu daného typu
# Strukturované datové typy umožnují uchovávat více hodnot či se do sebe zanořovat. Umožňují uchovávat i rozdílné hodnoty

# Jednoduché datové typy:

# String -> textový řetězec. Text musí být uvozen do '' či do ""
text = 'Ahoj, jak se máš?'

# Integer -> celé číslo.
cislo = 10

# Float -> číslo s plovoucí řádovou čárkou.
desetine_cislo = 7.6

# Boolean -> logická hodnota. Může nabývat dvou hodnot True(pravda, 1), False(nepravda, 0)
logicka = True



# Strukturované datové typy:


# Array/List -> pole je seřazená sturktura proměnných. Je ohraničenoho [] a jednotlivé prvky jeho vnitřní struktury jsou odděleny čárkou(,). Prvky v poli můžou být jakéhokoliv datového typu
pole = [] # inicializace prázdného pole
plne_pole = ['Pepa', 'Jana', 'Michal', 'Iveta'] # inicializace naplněného pole

# Jelikož je pole seřazená struktura přistupuje se k jeho prvkům pomocí indexace(idex pozice). V pythonu se indexuje od 0. Tedy první prvek je 0
plne_pole[0] # výsledek bude Pepa
pole_pole[2] # výsledek bude Iveta

# Pole je dynamické a je možno do něj kdykoliv přidávat nové hodnoty. Pomocí funkce append, která nohou hodnotu přidá nakonec pole
plne_pole.append('Olda')

# K odebrání poslední položky pole pak slouží fuknce pop. Ta vytáhne poslední položku vypíše ji a smaže z pole
plne_pole.pop() # Vypise Olda a smaze ho z pole

# Pro vypsání konkretního počtu prvků z pole se používá operand :.
plne_pole[1:3] # Vypise vsechny prvky od 2 do 3 prvek
plne_pole[2:] # Vypise veschny prvky jejich index je vetši než 1


# Tuple -> velmi podobná struktura Listu. Je ohraničena () a jednotlivé prvky jeho vnitřní struktury jsou odděleny čárkou(,). Tuple je však pouze pro čtení -> krom inicialize není možné do něj zapisovat a přepisovat jeho hodnoty.
tuple = () # inicializace prázdného tuplu
plny_tuple = ('Pepa', 'Jana', 'Michal', 'Iveta') # inicializace naplněného tuplu

# Jelikož je tuple seřazená struktura přistupuje se k jeho prvkům pomocí indexace(idex pozice). V pythonu se indexuje od 0. Tedy první prvek je 0
plny_tuple[0] # výsledek bude Pepa
plny_tuple[2] # výsledek bude Iveta

# Pro vypsání konkretního počtu prvků z pole se používá operand :.
plny_tuple[1:3] # Vypise vsechny prvky od 2 do 3 prvek
plny_tuple[2:] # Vypise veschny prvky jejich index je vetši než 1


# Dictionary -> slovník je neseřazená struktura proměnných. Je ohraničena {} a jednotlivé prvky jeho vnitřní struktury jsou pak odděleny čárkou(,). Prvky v dictu mohou být jakéhokoliv typu. Jelikož není slovník seřazený přístupuje se k němu přes klíč. prvek tedy pak vypadá následovně -> <key>: <value>, <key> by měl by unikatní vrámci celého slovínku.
dicto = {} # inicializace prázného slovníku
plne_dicto = {'Pepa': 'muž', 'Jana': 'žena', 'Michal': 'muž', 'Iveta': 'žena'}

# Přítup je tedy výhradně přes klíč. A jsou dvě možnosti jak k nim přistupovat. Se znalostí klíče a nebo se znalostí hodnoty.
# Přístup se znalostí klíče:
plne_dicto['Pepa'] # výsledek bude muž

# Přístup se znalostí hodnoty:
for item in plne_dicto:
	if plne_dicto[item] == 'muž':
		print(item)
# vytiskne Pepa a Michal

plne_dicto.keys() # vypíše Pepa, Jana, Michal, Iveta
plne_dicto.value() # vypíše muž, žena, muž, žena

# přidání nového prvku do slovníku
plne_dicto['Tereza'] = 'žena'

# editace prvku ve slovníku
plne_dicto['Iveta'] = 'muž'


##########################################################################################################################
##########                                       Operace s datovýma typama                                      ##########
##########################################################################################################################


#Integer:
a = 10
b = 20

res = a + b   # Součet -> 30
res = a - b   # Rozdíl -> -10
res = a * b   # Násobení -> 200
res = a ** b  # Mocnina -> 100000000000000000000
res = a ** -b # Odmocnina -> 1e-20 POZOR!!! výsledek už není int ale float
res = a / b   # Dělení -> 0.5 POZOR!!! výsledek už není int ale float
res = a // b  # Celočíselné dělení -> 0
res = a % b   # Zbytek po dělení -> 10
a += b        # Do a uloží a + b -> 30
a -= b        # Do a uloží a - b -> 200


#Float:
a = 1.2
b = 2.1

res = a + b   # Součet -> 3.3
res = a - b   # Rozdíl -> -0.9000000000000001
res = a * b   # Násobení -> 2.52
res = a ** b  # Mocnina -> 1.4664951016517147
res = a ** -b # Odmocnina -> 0.6818979476124394
res = a / b   # Dělení -> 0.5714285714285714
res = a // b  # Celočíselné dělení -> 0.0
res = a % b   # Zbytek po dělení -> 1.2

#Integer a Float:
a = 3
b = 2.1

res = a + b   # Součet -> 5.1 (Float)
res = a - b   # Rozdíl -> 0.8999999999999999 (Float)
res = a * b   # Násobení -> 6.300000000000001 (Float)
res = a ** b  # Mocnina -> 10.04510856630514 (Float)
res = a ** -b # Odmocnina -> 0.6818979476124394
res = a / b   # Dělení -> 0.5714285714285714
res = a // b  # Celočíselné dělení -> 0.0
res = a % b   # Zbytek po dělení -> 1.2




# TODO práce se strigem (operace, formátování, funkce(split,lower, upper, isdigit))
# TODO práce se listem/tuplem (seřazení, revert)
# TODO Ukázka zavořování listu a dictu

# TODO while cyklus
# TODO for cyklus

# TODO input

# TODO funkce bez returnu
# TODO funkce s returnem

# TODO parametry(povinné a nepovinné)

# TODO importy

# TODO vlastní knihovna
# TODO práce se soubory

# TODO objekt

# TODO TBA (sockety atd...)

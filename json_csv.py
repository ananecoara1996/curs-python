import json
from random import randint as rand


# with open("exemplu_json2.json", "r") as my_file:
#     date = json.load(my_file)

# print(date)
# print(type(date))
# print(json.dumps(date, indent=4))

# #Vreau sa afisez in felul urmator <nume> are <x> ani si <y> copii

# nume = date['nume']
# varsta =date.get('varsta')
# numar_copii = len(date['copii'])
# oras = date['adresa']['tara']

# print(f"{nume} are {varsta} ani si {numar_copii} copii")
# print(f"{nume} este din {oras}")


# my_dict = {
#     "nume": "Ion Popescu",
#     "varsta": 30,
#     "casatorit": True,
#     "copii": ["Ana", "Mihai"],
#     "adresa": {
#         "strada": "Strada Exemplu 123",
#         "oras": "Bucuresti",
#         "tara": "Romania"
#     },
#     "telefon": None
# }

# #Vreau sa scriu acest dictionar intr-un fisier numit ion_popescu\

# with open("ion_popescu.json", "w") as my_file:
#     json.dump(my_dict, my_file, indent=4)

# #sa mai adaugam o persoana in fisier

# with open("ion_popescu.json", "r") as my_file:
#     date = json.load(my_file)

# print(json.dumps(date, indent=4))

# date['copii'].append('Mihaela')
# date['telefon'] = '0734112748'

# print(json.dumps(date, indent=4))

# with open('ion_popescu.json', 'w') as my_file:
#     json.dump(date, my_file, indent=4)


# with open('exemplu_json1.json', 'r') as my_file:
#     date = json.load(my_file)

# print(type(date))

# for element in date:
#     # element['copii'] = rand(0,5)
#     element.update({'copii': rand(0,5)})

# #print(json.dumps(date, indent=4))
# #date[3] = rand(0,5)

# with open('exemplu_json1.json', 'w') as my_file:
#     json.dump(date, my_file, indent=4)

import csv

# with open("exemplu_csv.csv", "r", newline='') as my_file:
#     reader = csv.reader(my_file)
#     my_csv = []
#     for row in reader:
#         print(row)
#         my_csv.append(row)

# print(my_csv)
# print(my_csv[-1])
# #print(type(reader))


with open('exemplu_csv2.csv', 'w', newline='') as my_file:
    writer = csv.writer(my_file)
    writer.writerow(['nume', 'varsta', 'oras'])
    writer.writerow(['Ion Popescu', '30', 'Bucuresti'])
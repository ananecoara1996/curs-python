dictionarul_meu = {'Ana':18, 'Maria':20, 'Marian':45}
print(type(dictionarul_meu))

varsta = dictionarul_meu['Ana']

print(type(varsta))
print(varsta)

x = dictionarul_meu.get('Maria')
print(x)

dictionarul_meu['Marian'] = 30
print(dictionarul_meu)

dictionarul_meu['Anton'] = 56

print(dictionarul_meu)

print(dictionarul_meu.keys())


for element in dictionarul_meu.keys():
    print(element)

print()

for element in dictionarul_meu.values():
    print(element)

print()

for key, value in dictionarul_meu.items():  # le parcurge pe ambele si afiseaza
    print(key, value)

buletin1 = {'Prenume':'Ana', 'CNP':123, 'Varsta':18}
buletin1 ['Nume Familie'] = 'Ionescu'

print(buletin1)

print(buletin1.pop('Prenume'))
print(buletin1)

print(buletin1.popitem())
print(buletin1)

print(buletin1.get('Nume'))

buletin1.update({'Nume': 'Ana'})
print(buletin1)

buletin1.update([('Nume Familie', 'Ionescu'), ('salariu', 50)])
buletin1.update({'Nume': 'Maria'})
print(buletin1)

'''
CNP - Key unica
    {*Nume
     *Prenume
     *varsta
     *masina { *marca
               * vin
               *tip_combustibil
    
                }
    
    }
'''

# dict_mare = {
#     1234: {
#         'nume': 'Popescu',
#         'prenume': 'Ionut',
#         'varsta': 20,
#         'masina': {
#             'marca':'bmw',
#             'vin': 234556,
#             'tip_c':'Benzina'

#         }
#     },
#     1223: {
#         'nume': 'Ionescu',
#         'prenume': 'Anton',
#         'varsta': 25,
#         'masina': {
#             'marca':'audi',
#             'vin': 234556,
#             'tip_c':'Benzina'

#         }
#     }
# }


x = dict_mare[1223]['masina'].get('tip_c')
print(x)

dict_mare[1223]['masina']['tip_c']= ' GPL'
print(dict_mare)

dict_mare.get(1234).get('masina').update({'tip_c': 'electric'})
print(dict_mare)

import json
print(json.dumps(dict_mare, indent=4))

buletin1 = {'Prenume':'Ana', 'CNP':123, 'Varsta':18}
print(buletin1.get('masina', 'negasit'))

print(buletin1.setdefault('masina', 'Nu are masina'))
print(buletin1)

d = {}
print(d)
d.setdefault('fructe', [])
print(d)
d.setdefault('fructe', []).append('Mar')
print(d)
d.setdefault('fructe', []).append('Banana')
print(d)

for fruct in ['mar', 'banana', 'portocala']:
    d.setdefault('fructe', []).append(fruct)

print(d)

patr = [x**2 for x in range(5)]
print(patr)

patrate = {element:element**2  for element in range(5) }
print(patrate)
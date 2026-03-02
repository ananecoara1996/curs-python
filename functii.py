# def func_basic():
#     print("Salut din functie!")
#     return [1, 2, 3]

# var = func_basic()
# print(var)
# print(func_basic())

# print(func_basic())

# def afiseaza_nume(nume, prenume):
#     print(f'Salut {nume} {prenume}!')

# afiseaza_nume('Ana' , 'Maria')

# def afiseaza_nume(nume = 'Popescu', prenume = 'Ana'):
#     print(f'Salut {nume} {prenume}!')

# afiseaza_nume('Ionescu')


# var1 = 1
# var2 = 2
# var3 = 3

# def func(par1, par2, par3 = True):
#     print(par1, par2, par3)

# func(var1, var2)

# def operatii(val1, val2):

#     return val1 + val2, val1 - val2, val1 * val2


# print(type(operatii(10, 20)))
# print(operatii(10, 20))
# adunare, scadere, inmultire = operatii(10, 20)

# print(adunare)
# print(scadere)
# print(inmultire)


# def functie_extra(param1, param2):
#     rezultat = param1 + param2
#     print(rezultat)
#     var = 10 + rezultat
#     print(var)

# functie_extra(10, 20)
 
# var = 15

# def functie_extra(param1, param2):
#     global var
#     var = param1 + param2
#     print(var)

# functie_extra(100, 200)

# var = var +1000
# print(var)


# x = 300

# def myfunc():
#   global x
#   x = 200
#   print(x)

# myfunc()

# print(x)

# def aduna(lista_elemente):
#     suma = 0
#     for element in lista_elemente:
#         suma += element

#     return suma

# def produs(lista_elemente):
#     produsul = 1
#     for element in lista_elemente:
#         produsul *= element
    
#     return produsul


# def suma_liste(func, lista_cu_liste):
#     suma_totala = 0
#     for lista in lista_cu_liste:
#         print(lista)
#         print(func(lista))
#         suma_totala += func(lista)

#     return suma_totala


# lista = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# print("Suma sumelor elementelor din liste este: ", suma_liste(aduna, lista))
# print("Suma produselor elementelor din liste este: ", suma_liste(produs, lista))

# dictionar = {}
# sorted(dictionar, key=dictionar.get)


# def suma_elemente(par1, par2, *args):
#     print(par1)
#     print(par2)
#     print(args)
#     #return sum(args)

# print(suma_elemente(10, 7))
# print(suma_elemente(10, 11, 12, 13))

# def suma_elemente_2(par1, par2, **kwargs):
#     print(par1)
#     print(par2)
#     print(kwargs)


# suma_elemente_2(par1 = 10, par2 = 20, par3 = 30, par4 = 40)

# def suma_kwargs(**kwargs):
#     # kwargs este un dicționar, ex: {'a': 10, 'b': 20}
#     # kwargs.values() extrage doar numerele: [10, 20]
#     print(kwargs)
#     total = sum(kwargs.values())
#     return total

# # Apelarea funcției
# rezultat = suma_kwargs(mere = 10, pere = 5, banane = 20)
# print(f"Suma totală este: {rezultat}") # Output: Suma totală este: 35

# [DEBUG]
# [INFO] 

def logare(*mesaje, **optiuni):
    # print(mesaje)
    # print(optiuni)
    nivel = optiuni.get('nivel', 'INFO')
    separator = optiuni.get('separator', ' ')
    log_final = separator.join(str(mesaj) for mesaj in mesaje)
    print(f"[{nivel}] {log_final}")

action = "Start program"
user = 'Anisoara'

logare(f'Action: {action}', f"User: {user}", nivel = "DEBUG", separator = ' | ')
print()
logare("Eroare la conexiune", 404, nivel = "ERROR", separator = " | ")


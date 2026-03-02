zile = ("Luni", "Marti", "Miercuri", "Joi", "Vineri", "Sambata", "Duminica")
print(zile[3])

print(zile.count("Luni"))
print(zile.index("Vineri"))

zile_lucratoare = zile[0:5]
print(zile_lucratoare)

# zile_lucratoare[0] = "Luni" ->eroare

for element in zile_lucratoare:
    if element == "i":
        print(element)

zile_i = tuple(zi for zi in zile if "i" in zi)
print(zile_i)

tuple_numere = (1, 2, 3, 4)
print(tuple_numere)
tuple_numere = list(tuple_numere)
print(tuple_numere)
tuple_numere.append(5)
print(tuple_numere)
tuple_numere = tuple(tuple_numere)
print(tuple_numere)


#unpacking tuples
tuple_ceva = ('Ana', 'Ionescu', '25')
prenume, nume, varsta = tuple_ceva

print(prenume)
print(nume)
print(varsta)


#sets
#set nu accepta duplicate
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)
print(my_set)

lista_mea = [1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7, 7, 7]   
print(lista_mea)
lista_mea = set(lista_mea)
lista_mea = list(set(lista_mea))
print(lista_mea)

my_set = {1,2,3,4,5,6,7,8}
print(my_set)

print(my_set.pop())
print(my_set)
print(my_set.pop())
print(my_set)

set1 = {1, 2, 3, 4, 5}
print(set1)
set2 = {3, 4, 7, 8, 9}
set3 = {1, 2, 3, 4, 5, 6, 7}
print(set2)
#set1.update(set2)
#print(set1)

print(set1.union(set2))
print(set1)
print(set2)

print(set1.difference(set2))
print(set2.difference(set1))

print(set1.intersection(set2))
print(set1.issubset(set2))
print(set1.issubset(set3))
print(set3.issuperset(set2))

print({x**2 for x in range(10) if x % 2 == 0})

lista = [1, 2, 3, 3, 3, 4]
frz_set = frozenset(lista)
print(frz_set)
l = list (frz_set)
print(l)
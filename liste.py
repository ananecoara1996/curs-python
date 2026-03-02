# fructe = ['banane', 'mere', 'pere', 'kiwi']

# print(fructe)

# print(fructe[1])

# fructe[0] = 'capsune'

# print(fructe)

# print(len(fructe))
# fructe.remove('mere')
# print(fructe)

# print(fructe[1][-1])

# print(fructe[0][0:4])

# elementul = fructe[0]
# caractere = elementul[0:4]
# print(caractere)

# print(fructe[-1].upper())

# lista_smechera = [1, 2, 3, 'kiwi', 'bere', ['Mariana', 'Ionela', 'Marius']]
# print(len(lista_smechera))
# print(lista_smechera[-1][-2][-3:])

# print(len(lista_smechera[4]))

# lista_smechera.append(4.6)

# print(lista_smechera)

# lista_smechera.insert(3, 3.5)

# print(lista_smechera)

# lista_smechera.remove('bere')
# print(lista_smechera)

# lista_smechera.pop(2)
# print(lista_smechera)

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 6]

# lista1.append(lista2)
# print(lista1)

# lista1.extend(lista2)
# print(lista1)

# lista1.sort()
# print(lista1)
# lista1.reverse()
# print(lista1)

# print(lista1.index(4))

# print(lista1.count(2))

# lista_noua = lista1 + fructe
# print(lista_noua)

# ex_sorted = sorted(lista1)
# print(lista1)
# print(ex_sorted)

# lista_mea = list('ananas')
# print(lista_mea)

# for index, valoare in enumerate(fructe):
#     print(f'la pozitia {index} se afla {valoare}')
# for valoare in fructe:
#     print(valoare)

# x = [1, 2, 3, 9]
# y = [4, 5, 6, 10]

# for a, b in zip(x, y):
#     print(f"elementele impachetate sunt {a} - {b}")

# nume = ["Ana", "Maria", "Marcel"]
# varsta = [32, 54, 18]

# for element_nume, element_varsta in zip(nume, varsta):
#     print(f"{element_nume} are {element_varsta} ani")

# # any() -> cel putin un element este True
# # all() -> toate elementele sunt True

# lista1 = [False, False, False, False]
# lista2 = [1, 2, 3, 4]

# print(any(lista1))
# print(any(lista2))
# print(all(lista1))
# print(all(lista2))


# #Sa se genereze un program care genereaza o lista cu numere pare intre 1-10 inclusiv si o afiseaza. 

# lista = range(1, 11)
# lista_pare = []
# for x in range(1, 11):
#     if x % 2 == 0: 
#         lista_pare.append(x)
#     else:
#         continue

# print(lista_pare)

# # lista_mea -> [element **2]


# lista_mea = [x**2 for x in lista if x % 2 == 0 ]
# print(lista_mea)

# lista_initiala = [3, 5, 7, 15, 21, 72, 56, 99]
# lista_speciala = [] #numerele divizibile cu 3 si cu 5 

# lista_speciala = [element for element in lista_initiala if element % 3 == 0 and element % 5 == 0]
# print(lista_speciala)

# # verificati daca cel putin un element din lista_initiala este divizil si cu 3 si cu 5

# flag = any([x % 3 == 0  and x % 5 == 0 for x in lista_initiala])
# print(flag)

# # #Exercitiul 19 ?
# # '''Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# # Exemplu: [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]] si elementul 1 -> apare de 4 ori'''

# lista_elemente = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]
# element = 1 

# count = 0 
# index = 0

# while index < len(lista_elemente):
#     if isinstance(lista_elemente[index], list):
#         lista_elemente.extend(lista_elemente[index])
#     else: 
#         if lista_elemente[index] == element:
#             count +=1
    
#     index +=1



# str1 = 'ceva'
# str2 = str1

# print(id(str1))
# print(id(str2))

# str2 = str2 + 'inca_ceva'
# print(str1)
# print(str2)

# print(id(str1))
# print(id(str2))

# list1 = [1, 2, 3, 4]
# list2 = list1

# print(id(list1))
# print(id(list2))

# list2[0] = 10 

# print(id(list1))
# print(id(list2))

# print(list1)
# print(list2)


# list1 = [1, 2, 3, 4]
# list2 = list1.copy()
# print(id(list1))
# print(id(list2))

# list2[0] = 10 
# print(list1)
# print(list2)


# import copy



# lis1 = [1, 2, [3, 4]]
# lis2 = copy.deepcopy(lis1)

# print(id(lis1))
# print(id(lis2))

# lis2[0] = 20
# lis2[2][0] = 10

# print(lis1)
# print(lis2)

# print(id(lis1[2]))
# print(id(lis2[2]))


lista = [1, 2, 3, [1, 3, 5], 6, [1, [1, 2], 3]]

lista_simpla = [1, 2, 3, 4, 5, 1, 7, 1]

lista_noua = [ 'A', 2, 3, ['A', 3, 5], 6, ['A', ['A', 2], 3] ]

def frecventa_nr(lista_numere, nr_cautat):
    counter = 0
    for element in lista_numere:
        if isinstance(element, list):
            counter += frecventa_nr(element, nr_cautat)   # daca elementul este o lista chemam functia din nou care verifica in lista noua
        elif element == nr_cautat:
            counter += 1
        else:
            pass

    return counter

print(frecventa_nr(lista_noua, 'A'))



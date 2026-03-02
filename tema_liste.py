# #Exercitiul 1
# # Sa se afiseze toate puterile lui 2 aflate intre un interval dat de utilizator.
# # Exemplu: 10, 50 -> 16, 32

# a = int(input("Introduceti limita inferioara (a): "))
# b = int(input("Introduceti limita superioara (b): "))

# print(f"Puterile lui 2 în intervalul [{a}, {b}] sunt:")

# # Initializam prima putere a lui 2 (2^0 = 1)
# putere = 1
    
# # Folosim o bucla while pentru a genera puterile
# while putere <= b:
# # Verificam daca puterea curenta este in interiorul intervalului
#     if putere >= a:
#         print(putere)
        
# # Trecem la urmatoarea putere a lui 2
#     putere *= 2

# #Exercitiul 3
# #Creează o listă cu 7 numere întregi, apoi afișează suma și media elementelor fara a utiliza functiile sum() si avg().
# #Exemplu: [1,2,3,4,5,6,7] -> suma=28, media=4.0

# my_list = [1, 2, 3, 4, 5, 6, 7]

# suma = 0

# for n in my_list:
#     suma +=n
#     media = suma / len(my_list)
    
# print(f"Suma numerelor este: {suma}")
# print(f"Media este: {media}")

# #Exercitiul 4 
# #Primește o listă de la tastatură (elemente separate prin spațiu) și afișează lista inversată.
# #Exemplu: input: 1 2 3 4 5 -> output: [5,4,3,2,1]

# lista = input ("Introduceti elementele din lista: ").split()
# lista_inversata = lista[::-1]
# print(lista_inversata)

# #Exercitiul 5
# #Afișează toate elementele de pe poziții impare dintr-o listă dată.
# #Exemplu: [10,20,30,40,50,60] -> 20,40,60

# lista = [10, 20, 30, 40, 50, 60]

# elemente_pare = lista[1::2]

# print(elemente_pare)

# #Exercitiul 6
# #Înlocuiește toate aparițiile unui element dat cu altă valoare într-o listă.
# #Exemplu: [1,2,3,2,4], inlocuieste 2 cu 5 -> [1,5,3,5,4]

# lista = [1, 2, 3, 2, 4]
# lista2 = []

# for element in lista:
#     if element == 2:
#         lista2.append(5)
#     else:
#         lista2.append(element)

# print (lista2)

# #Exercitiul 7
# #Afișează elementul maxim și minim dintr-o listă fără a folosi funcțiile max/min.
# #Exemplu: [3,1,4,1,5,9,2] -> max=9, min=1

# numere = [3, 1, 4, 1, 5, 9, 2]

# #Initializam min si max cu primul element din lista
# maxim = numere[0]  
# minim = numere[0]

# #Parcurgem lista incepand cu al doilea element
# for element in numere:
#     if element > maxim:
#         maxim = element
#     if element < minim:
#         minim = element

# print(f"Elementul maxim este: {maxim}")
# print(f"Elementul minim este: {minim}")


# #Exercitiul 8 
# #Elimină toate elementele pare dintr-o listă de numere.
# #Exemplu: [1,2,3,4,5,6] -> [1,3,5]

# lista = [1, 2, 3, 4, 5, 6]

# lista_impara = []

# for element in lista:
#     if element % 2 !=0:
#         lista_impara.append(element)

# print(lista_impara)

# #Exercitiul 9
# #9) Primește o listă de stringuri și construiește o nouă listă cu stringurile care conțin litera 'a'.
# #Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'masina']

# lista = ['ana', 'mere', 'casa', 'masina']

# lista_noua = [cuvant for cuvant in lista if 'a' in cuvant]  #itereaza prin fiecare element din lista initiala 

# print(lista_noua)

# #Exercitiul 10 
# #Verifică dacă o listă este palindrom (se citește la fel de la stânga la dreapta și invers).
# # Exemplu: [1,2,3,2,1] -> True, [1,2,3,4] -> False

# lista = [1, 2, 3, 4, 3, 2, 1]

# lista= lista[::-1]

# print (lista)

# #Exercitiul 11 ?
# #Interclasează două liste de aceeași lungime într-o singură listă.
# # Exemplu: [1,2], [3,4] => [1,3,2,4]

# lista1 = [1, 2]
# lista2 = [3, 4]

# lista_noua = lista1 + lista2
# print(lista_noua)

# #Exercitiul 12
# #Creează o listă de liste [index, valoare] pentru fiecare element dintr-o listă dată.
# # Exemplu: [10,20,30] -> [[0,10],[1,20],[2,30]]

# lista = [10, 20, 30]

# lista_indexata = [[index, valoare] for index, valoare in enumerate(lista)]

# print(lista_indexata)

# #Exercitiul 13
# # #Primește o listă de numere și elimină toate elementele care apar de mai mult de o dată (păstrează doar elementele unice). Fara a folosi set().
# # Exemplu: [1,2,2,3,4,4,5] -> [1,3,5]

# numere = [1, 2, 2, 3, 4, 4, 5]

# elemente_unice = []

# for n in numere:
#     if n not in elemente_unice:
#         elemente_unice.append(n)

# print(numere)
# print(elemente_unice)

# #Exercitiul 14
# #Primește o listă de numere și grupează elementele în două liste: una cu numere negative, alta cu numere pozitive și zero.
# # Exemplu: [10,-1,2,-3,0,4,-5] -> negative: [-1,-3,-5], pozitive_si_zero: [10,2,0,4]

# lista_numere = [10, -1, 2, -3, 0, 4, -5]

# pozitive_si_zero = []
# negative = []

# for numar in lista_numere:
#     if numar >= 0:
#         pozitive_si_zero.append(numar)
#     else:
#         negative.append(numar)

# print(f"Numerele pozitive si zero sunt: {pozitive_si_zero}")
# print(f"Numerele negative sunt: {negative}") 

# #Exercitiul 15  ?
# #Primește o listă de stringuri și sorteaz-o crescător după numărul de vocale din fiecare string.Fara a folosi functia sort() sau sorted().
# # Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'mere', 'masina']

# lista = ['ana', 'mere', 'casa', 'masina']

# vocale = "aeiouAEIOU"

# # Implementare Bubble Sort
# for i in range(len(lista)):
#     for j in range(i+1, len(lista)):
#     # Comparăm numărul de vocale al elementelor adiacente
#         if numar_vocale(lista[j]) > numar_vocale(lista[j + 1]):
#             # Interschimbăm elementele dacă nu sunt în ordinea corectă
#             lista[j], lista[j + 1] = lista[j + 1], lista[j]


# print("Lista sortată după numărul de vocale:")


# #Exercitiul 16 
# # Primește o listă de liste (matrice) și calculează suma elementelor de pe diagonala principală (doar dacă matricea este pătratică).
# # Exemplu: [[1,2,3],[4,5,6],[7,8,9]] -> 15 (1+5+9)

# matrice = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# suma_diagonala_principala = matrice[0][0] + matrice [1][1] + matrice [2][2]

# print(suma_diagonala_principala)


# #Exercitiul 17
# #Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga numele "Ionut" si sa se afiseze.

# lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]

# print(lista[1][1][0:5])

# #Exercitiul 18
# # Se da lista: [[10, 5, 29], ["Marian", "Ionut", "Marcel], [10.2, 7.5, 3.4]]. Sa se extraga litera "r" din numele "Marcel" si sa se afiseze.

# lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]

# print(lista[1][2][2])

# #Exercitiul 19 ?
# '''Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# Exemplu: [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]] si elementul 1 -> apare de 4 ori'''

lista = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]

text_lista = str(lista)

print(text_lista)

rezultat = text_lista.count('1')

element_cautat = 1 

print(f"Elementul {element_cautat} apare de {rezultat} ori.")

# total = 0

# for element in lista:
#         if isinstance(element):
#             # Dacă elementul este o listă, apelăm funcția recursiv
#             total += lista(element, list)
#         elif element == 1:
#             # Dacă am găsit elementul căutat
#             total += 1

# element_cautat = 1

#print(f"Elementul {element_cautat} apare de {total} ori.") 


# #Exercitiul 20
# '''Scrieti un program care sa genereze un numar aleator intre 1 si 100.
# Utilizatorul trebuie sa ghiceasca numarul, iar programul sa ii ofere indicatii daca numarul introdus este mai mare sau mai mic decat cel generat.
# Programul se termina cand utilizatorul ghiceste numarul corect sau daca introduce cuvantul exit. La final se afiseaza numarul de incercari facute.'''

import random
numar_aleator = random.randint(1, 100)

incercari = 0
ghicit = False

print("Am generat un numar intre 1 și 100.")
print("Introduceti 'exit' pentru a termina jocul.")

while not ghicit:
    introducere = input("\nIntroduceti numarul: ")

# Verificam daca utilizatorul doreste sa iasa
    
    

# Validăm daca introducerea este un numar
    numar_introdus = int(introducere)
    incercari += 1
        
# 3. Oferim indicații (mai mare/mic)
    if numar_introdus < numar_aleator:
        print("Prea mic! Mai încearcă.")
    elif numar_introdus > numar_aleator:
        print("Prea mare! Mai încearcă.")
    else:
        ghicit = True
        print(f"Felicitări! Ai ghicit numărul {numar_aleator}!")

# 4. Afișăm numărul de încercări la final
print(f"Ai făcut {incercari} încercări.")

# #Exercitiul 21
# '''Sa se scrie un program primeste date in urmatorul format: "Nume: Ionescu Prenume: Ion" pana cand se introduce
# caracterul #. Programul trebuie sa stocheze toate datele citite, iar la final sa le afiseze in ordine alfabetica
# in functie de numele de familie.'''




'''
-----------------------------------------------------------------------------------------------------------------
Tema 2 -Liste
-----------------------------------------------------------------------------------------------------------------
'''

#Exercitiul 1
#Creeaza o lista cu patratele numerelor de la 0 la 9. Ex: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

lista_patrate = [element**2 for element in range(10)]

print(f"Lista cu patratele numerelor de la 0 la 9 este: {lista_patrate}")

#Exercitiul 2
#Creeaza o lista cu toate numerele pare intre divizibile cu 3 dintre 1 si 50 inclusiv. Ex: [6, 12, 18, 24, 30, 36, 42, 48]

lista_numere = [element for element in range(51) if element % 2 == 0 and element % 3 == 0 ]

print(f"Lista cu toate numerele pare divizibile cu 3 in intervalul 1 si 50 este: {lista_numere}")

#Exercitiul 3
#Dintr-o lista cu cuvinte creeaza o lista cu lungimile fiecarui cuvant. Ex: ['ana', 'maria', 'ion', 'marioara', '1468912'] -> [3, 5, 3, 8, 7]

lista = ['ana', 'maria', 'ion', 'marioara', '1468912']

lista_noua = [len(element) for element in lista]

print(f"Lista noua cu lungimile fiecarui cuvant este: {lista_noua}")

#Exercitiul 4
#Dintr-o lista cu numere de la 1 la 25, creeaza o lista cu patratele numerelor care sunt divizibile cu 4 si cu 6. Ex: [144, 576, 1296, 2304]

lista_patrate = [element**2 for element in range(1, 26) if element % 4 == 0  and element % 6 == 0]

print(f"Lista patratelor numerelor care sunt divizibile cu 4 si cu 6 este: {lista_patrate}")

#Exercitiul 5
#Creeaza o lista cu toate vocalele dintr-un text dat. 
# Ex: 'Aceasta este o propozitie de test.' -> ['A', 'e', 'a', 'a', 'e', 'o', 'o', 'i', 'i', 'e', 'e']

propozitie = 'Aceasta este o propozitie de test.'
vocale = "aeiouAEIOU"

lista_vocale = [element for element in propozitie if element in vocale]

print(f"Lista vocalelor este: {lista_vocale}")



# Folositi any pentru rezolvarea urmatoarelor exercitii:

# Exercitiul 1
# Verifica daca intr-o lista de numere exista cel putin un numar par. Ex: [1, 3, 5, 7, 8] -> True

lista_numere = [1, 3, 5, 7, 8]

exista_numar_par = any(element % 2 == 0 for element in lista_numere)

if exista_numar_par:
    print("Lista contine cel putin un numar par.")
else:
    print("Lista nu contine niciun numar par.")

#Exercitiul 2
#Verifica daca intr-o lista de cuvinte exista cel putin un cuvant care sa contina litera 'z'. Ex: ['ana', 'maria', 'ioana', 'zebra'] -> True

lista_cuvinte = ['ana', 'maria', 'ioana', 'zebra']

exista_z = any('z' in element.lower() for element in lista_cuvinte)

if exista_z:
    print("Exista cel putin un cuvant care sa contina litera 'z' ", exista_z)
else:
    print("Nu exista nici un cuvant cu litera 'z'")


#Exercitiul 3
#Verifica daca intr-o lista de numere exista cel putin un numar negativ. Ex: [4, 5, -1, 3, 0] -> True

lista_numere = [4, 5, -1, 3, 0]

numar_negativ = any(numar < 0 for numar in lista_numere)

if numar_negativ:
    print("Exista cel putin un numar negativ ", numar_negativ)
else:
    print("Nu exista numere negative")

#Exercitiul 4
#Verifica daca intr-o lista de stringuri exista cel putin un string care sa fie gol. Ex: ['ana', '', 'maria'] -> True

lista = ['ana', '', 'maria']

string_gol = any(element == '' for element in lista)

print(string_gol)

#Exercitiul 5
#Verifica daca intr-o lista de caractere exista cel putin o vocala mare (A, E, I, O, U). Ex: ['a', 'b', 'C', 'D', 'E'] -> True


lista_vocale = ['a', 'b', 'C', 'D', 'E']

lista_vocale_mari = ['A', 'E', 'I', 'O', 'U']

lista_noua = any(element in lista_vocale_mari for element in lista_vocale)

print(lista_noua)
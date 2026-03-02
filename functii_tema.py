# #Exercitiul 1
# #Scrie o funcție care primește un nume și afișează "Salut, <nume>!".

# def afiseaza_nume(nume):
#     print(f"Salut, {nume} !")
    
# afiseaza_nume("Ana")
# afiseaza_nume("Maria")


# #Exercitiul 2
# #Scrie o funcție care primește două numere și returnează suma lor.

# def suma():
#     a = int(input("Valoarea lui a este: "))
#     b = int(input("Valoarea lui b este: "))
#     sum = a + b
#     print(sum)

# print(f'Suma celor 2 numere este: {suma()}')


# #Exercitiul 3
# #Scrie o funcție care primește două numere și returnează suma, diferența și produsul lor (returnează un tuple).

# def operatii_numere(a, b):
#     suma = a + b
#     diferenta = a - b
#     produs = a * b

#     return suma, diferenta, produs

# a = 10
# b = 4

# rezultate = operatii_numere(a, b)


# print(f"Suma: {rezultate[0]}")
# print(f"Diferența: {rezultate[1]}")
# print(f"Produsul: {rezultate[2]}")
# print(f"Tuplul returnat: {rezultate}")

# s, d, p = operatii_numere(10, 5)

# print(f'Suma este: {s}')
# print(f'Diferenta este: {d}')
# print(f'Produsul este: {p}')


# #Exercitiul 4
# #Scrie o funcție care primește un număr și returnează True dacă este par, altfel False.

# def numar_par(numar):
#     if numar % 2 == 0:
#         return True
#     else:
#         return False

# print(numar_par(16))
# print(numar_par(55))

# #Exercitiull 5
# #Scrie o functie care primeste ca parametru un numar si modifica valoarea unei variabile globale cu valoarea numarului la patrat.

# VARIABILA_GLOBALA = 2

# def calcul_patrat(numar):
#     global VARIABILA_GLOBALA
#     VARIABILA_GLOBALA = numar ** 2
    

# print(f"Inainte de apel: {VARIABILA_GLOBALA}")
# calcul_patrat(9)
# print(f"Dupa apel: {VARIABILA_GLOBALA}") 


# #Exercitiul 6
# #Scrie o funcție care primește o listă de numere și returnează suma tuturor numerelor.

# def lista_numere(numere):
#     return sum(numere)

# #lista = [1|3|4|6|9|75]
# #rezultat = lista_numere(lista)

# #[1, 2, 3, 4, 5]

# #print(f'Suma numerelor din lista este : {rezultat}')
# sir_input = input("Introduceți lista [ex: 1|3|4]: ")
# lista_sparta = sir_input.split("|")
# print(lista_sparta)
# lista_noua = [int(i.strip()) for i in lista_sparta]
# print(lista_noua)

# rezultat = lista_numere(lista_noua)
# print(f'Suma numerelor din lista este : {rezultat}')



# #Exercitiul 7
# #Scrie o funcție care primește un string și returnează stringul inversat.

# def string_inversat(my_string = 'Are are mere.'):
#     return my_string[::-1]

# print(f'Stringul inversat este: {string_inversat()}')

# #Exercitiul 8
# #Scrie o funcție care primește o listă de stringuri și returnează o listă cu lungimile fiecărui string.

# def lista_stringuri(lista_cuvinte):
#     return [len(cuvant) for cuvant in lista_cuvinte]


# cuvinte = ["Ana", "mere", "pere", "Maria"]
# print(lista_stringuri(cuvinte))


# #Exercitiul 9
# #Scrie o funcție care primește doua liste de numere si returneaza o lista cu numerele comune celor doua liste.

# def functii_comune(lista1, lista2):
#     numere_comune = [numar for numar in lista1 if numar in lista2]
#     return numere_comune

# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = [2, 3, 4, 8, 9, 11]

# print(functii_comune(lista1, lista2))

# #Exercitiul 10 
# # Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza numele persoanei cu cea mai mica varsta.

# def persoana_cu_varsta_mica(dictionar_persoane):

#     nume_persoana_varsta_mica = min(dictionar_persoane, key = dictionar_persoane.get)
#     varsta_mica = min(dictionar_persoane.values())
#     return nume_persoana_varsta_mica
    
# def varsta_cea_mai_mica(varste_persoane):
#     varsta_mica = min(varste_persoane.values())
#     return varsta_mica


# persoane = {
#     'Ioana': 34,
#     'Maria': 23,
#     'Anton': 45,
#     'Marius': 29,
#     'Mihaela': 34
# }

# persoana_specificata = persoana_cu_varsta_mica(persoane)
# varsta_specificata = varsta_cea_mai_mica(persoane)

# print(f'Persoana cu varsta cea mai mica este: {persoana_specificata} si are {varsta_specificata} ani. ')


# #Exercitiul 11
# #Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza un dictionar cu persoanele care au varsta peste 18 ani.

# def adulti(dictionar_persoane):
#     persoane_adulte = {nume: varsta for nume, varsta in dictionar_persoane.items() if varsta > 18}
#     return persoane_adulte

# persoane = {
#     'Gicu': 6,
#     'Ioana': 34,
#     'Maria': 23,
#     'Anton': 45,
#     'Marius': 29,
#     'Mihaela': 34
# }

# persoane_cu_varsta_peste_18_ani = adulti(persoane)
# print(f'Persoanele care au varsta peste 18 ani sunt: {persoane_cu_varsta_peste_18_ani} .')

# persoane = {}

# def filtru(persoane):
#     rezultat = {}
#     for nume, varsta in persoane.items():
#         if int(varsta) > 18:
#              rezultat[nume, varsta] = varsta
#     return rezultat

# while True:
#     date = input("Introdu date: ")
#     print(date)
#     if 'x' in date:
#         break
#     perechi_date = date.split()
#     print(perechi_date)
#     nume = perechi_date[2]
#     varsta = perechi_date[-1]
#     print(nume)

#     print(varsta)
#     persoane[nume] = varsta

# print(persoane)
# print(filtru(persoane))

# #Exercitiul 12
# #Scrie o functie care primeste o lista de numere si un numar n, si returneaza o lista cu numerele mai mici decat n.

# def functie_numere(lista, n):
#     lista_numere_mici = []
#     for numar in lista:
#         if numar < n:
#             lista_numere_mici.append(numar)
#     return lista_numere_mici
        

# lista_numere = [1, 2, 3, 4, 5, 6, 7, 5, 4, 6, 8, 10]
# numar_introdus = 10

# print(f'Lista cu numere mai mici decat {numar_introdus} este: {functie_numere(lista_numere, numar_introdus)}')
    

# #Exercitiul 13
# #Scrie o functie care primeste o lista de numere si returneaza cel mai mic numar, cel mai mare numar si media aritmetica a numerelor din lista.

# def operatii_cu_liste(numere):
#     media = int(sum(numere) / len(numere))
#     return min(numere), max(numere), media

# lista_numere = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# rezultate = operatii_cu_liste(lista_numere)

# print (f'Cel mai mic numar din lista este: {rezultate[0]}')
# print (f'Cel mai mare numar din lista este: {rezultate[1]}')
# print (f'Media aritmetica a numerelor din lista este: {rezultate[2]} ')


# #Exercitiul 14
# #Scrie o functie care primeste o lista de numere si returneaza un dictionar cu frecventa fiecarui numar in lista (cheia este numarul, valoarea este frecventa)

def functie_frecventa_aparitie(lista_numere):
    frecventa = {}
    for numar in lista_numere:
        if numar in frecventa:
            frecventa[numar] += 1
        else:
            frecventa[numar] = 1
    return frecventa


lista = [1, 2, 3, 2, 1, 3, 2, 2, 4, 5, 4]

print(f'Dictionarul cu frecventa fiecarui numar din lista este: {functie_frecventa_aparitie(lista)}')



# #Exercitiul 15
# # Scrie o functie care primeste o lista de numere si returneaza o lista care contine numerele fara duplicate.

# def elimina_duplicate(lista_numere):
#     elemente_unice = []
#     for numar in lista_numere:
#         if numar not in elemente_unice:
#             elemente_unice.append(numar)
#     return elemente_unice


# lista = [1, 2, 3, 2, 2, 3, 4, 5, 6, 6, 6, 7, 8]

# print(f'Lista care contine numere fara duplicate este: {elimina_duplicate(lista)}')


# #Exercitiul 16
# #Scrie o functie care primeste o lista de numere si returneaza o lista doar cu numerele prime.

# def elemente_prime(lista_numere):
#     numere_prime = []
#     for numar in lista_numere:
#         if numar % 2 == 0:
#             numere_prime.append(numar)
#     return numere_prime

# lista = [2, 3, 4, 5, 6, 7, 6, 8, 13, 14, 20]

# print(f'Lista cu numerele prime este: {elemente_prime(lista)}')


#Exercitii_cu_functii


#Ex1: Calculul Ariei: Scrie o funcție care primește lungimea laturii unui pătrat și returnează aria acestuia.

# def calculeaza_aria(latura):
#     aria = latura ** 2
#     return aria
  
# rezultat = calculeaza_aria(5)

# print(f"Aria patratului este: {rezultat}")


# #Ex2: Convertor de Temperatură: Creează două funcții: una care transformă gradele Celsius în Fahrenheit și alta invers.

# #Formula: temp_Fahrenheit = (grade_Celsius * float(1.8)) + 32


# def temperatura_Celsius(grade_Celsius):
#     temp_Fahrenheit = (grade_Celsius * float(1.8)) + 32
#     return temp_Fahrenheit


# rezultat_Fahrenheit = temperatura_Celsius(20)
# print(f"Temperatura in Fahrenheit este: {rezultat_Fahrenheit}")

# def temperatura_Fahrenheit(grade_Fahrenheit):
#   temp_Celsius = float((grade_Fahrenheit - 32) / 1.8)
#   return temp_Celsius 

# rezultat_Celsius = temperatura_Fahrenheit(68)
# print(f"Temperatura in grade Celsius este: {rezultat_Celsius}")

# #Ex3: Maximul a trei numere: Scrie o funcție care primește trei numere ca argumente și îl returnează pe cel mai mare.

# def cel_mai_mare_numar(a, b, c):
#     return max(a, b, c)

# print(cel_mai_mare_numar(7, 3, 4))

# #Ex4: Verificare Interval: Scrie o funcție care verifică dacă un număr dat se află într-un interval specificat (ex: între 10 și 50). 

# def verifica_numar(numar):
#     if numar in range(10, 51, 1):
#         print("Numarul se afla in intervalul specificat")
#     else:
#         print("Numarul nu se afla in interval")
#     return numar

# numar_ales = verifica_numar(10)

# print(numar_ales)  


# #Ex5: Write a Python program to calculate the sum of a list of numbers using recursion.

# def suma_numere(lista_numere):
#     if len(lista_numere) == 1: 
#         return lista_numere[0] #If the list has only one element, return that element
#     else:
#         return lista_numere[0] + suma_numere(lista_numere[1:])


# lista = [2, 4, 6, 8, 10, 12, 14, 16, 20]
# rezultat = suma_numere(lista)

# print(f"Suma numerelor din lista este: {rezultat}")


# #Ex6: Sum of Nested Lists Using Recursion

# lista_imbricata = [1, 2, [3,4], [5,6]]

# def suma_elemente_lista_imbricata(numere_lista):
#     suma = 0
#     for element in numere_lista:
#         if type(element) != type([]):
#             suma = suma + element
#         else:
#             suma = suma + suma_elemente_lista_imbricata(element)
    
#     return suma


# print(suma_elemente_lista_imbricata(lista_imbricata))

# #Ex7: Factorial Using Recursion

# def factorial(numar):
#     if numar <= 1:
#         return 1b
#     else:
#         return numar * factorial(numar - 1)

# print(factorial(5))


# #Ex8 Sum of Digits of an Integer Using Recursion

# def suma_digits(numar):
#     if numar == 0:
#         return 0
#     else:
#         # If 'n' is not 0, calculate the sum of the last digit (n % 10) and
#         # recursively call the sumDigits function on the remaining digits (n / 10)
#         return numar % 10 + suma_digits(int(numar / 10))
    

# print(suma_digits(34597))

# # 
# # Employee salary calculation

# def calculate_salary(hours_worked, hourly_rate, bonus=0):
#     if hours_worked < 0 or hourly_rate < 0 or bonus < 0:
#         return "Invalid input"
#     else:
#         salary = (hours_worked * hourly_rate) + bonus
#         return round(salary, 2)
# print(calculate_salary(40, 300))       # Output: 600.0
# print(calculate_salary(40, 15, 100))  # Output: 700.0

# #
# #Calculating discounts in a store

# def apply_discount(price, discount_percent):
#     if price < 0 or discount_percent < 0 or discount_percent > 100:
#         return "Invalid input"
#     else:
#         discount_amount = (discount_percent / 100) * price
#         return round(price - discount_amount, 2)
# # Example usage
# print(apply_discount(120, 20))  # Output: 96.0
# print(apply_discount(50, 10))   # Output: 45.0
# print(apply_discount(200, 50))  # Output: 100.0


# count = 1
# while count <= 10:
#     print(count)
#     if count == 3:
#         break
#     count += 1  # Increase count by 1 each 


# def cel_mai_lung_cuvant(propozitie):
#     cuvinte = propozitie.split()  # Split sentence into words
#     cel_mai_lung = cuvinte[0]    #Assume the first word is the longest
#     for cuvant in cuvinte:
#         if len(cuvant) > len(cel_mai_lung):  
#             cel_mai_lung = cuvant
#     return cel_mai_lung


# propozitie = input("Introduceti o propozitie: ")
# print("Cel mai lung cuvant din propozitie este: ", cel_mai_lung_cuvant(propozitie))


# #Inversarea unui șir de caractere

# def inverseaza_string(text):
#     # Folosim slicing [start:stop:step] cu pasul -1
#     return text[::-1]

# # Testare
# cuvant = "python"
# print(f"Original: {cuvant} -> Inversat: {inverseaza_string(cuvant)}")

# #Filtrare și Sortare Listă
# #Pentru acest exercițiu, vom folosi o list comprehension (o metodă rapidă și "pythonic" de a crea liste) și metoda .sort() sau funcția sorted().

# def filtreaza_si_sorteaza(lista_numere):
#     # Filtrăm doar numerele mai mari de 0
#     numere_pozitive = [n for n in lista_numere if n > 0]
    
#     # Returnăm lista sortată crescător
#     return sorted(numere_pozitive)

# # Testare
# numere_mixte = [10, -5, 3, -1, 0, 45, -12, 7]
# rezultat = filtreaza_si_sorteaza(numere_mixte)
# print(f"Lista initiala: {numere_mixte}")
# print(f"Lista filtrata si sortata: {rezultat}")


# #Quick Sort

# def quick_sort(arr):
#     # Cazul de bază: o listă cu 0 sau 1 elemente este deja sortată
#     if len(arr) <= 1:
#         return arr
    
#     # Alegem pivotul (aici, elementul din mijloc)
#     pivot = arr[len(arr) // 2]
    
#     # Împărțim elementele în 3 categorii
#     stanga = [x for x in arr if x < pivot]    # Mai mici decât pivotul
#     mijloc = [x for x in arr if x == pivot]   # Egale cu pivotul
#     dreapta = [x for x in arr if x > pivot]   # Mai mari decât pivotul
    
#     # Sortăm recursiv stânga și dreapta, apoi le unim
#     return quick_sort(stanga) + mijloc + quick_sort(dreapta)

# # Test:
# lista = [3, 6, 8, 10, 1, 2, 1]
# print(quick_sort(lista)) # Rezultat: [1, 1, 2, 3, 6, 8, 10]



#Exercitiul 1
#Scrie o funcție recursivă care calculează factorialul unui număr.
#Ex: pentru n = 5, 5 x 4 x 3 x 2 x 1 = 120

def calculeaza_factorial(numar):
    if numar <= 1:
        return 1
    else:
        return numar * calculeaza_factorial(numar - 1)


numar = 5

print(f"Factorial de {numar} este {calculeaza_factorial(numar)}" )


#Exercitiul 2
# Scrie o funcție recursivă care calculează suma numerelor de la 1 la n.
#Ex: pentru n=5, returnează 15 (1+2+3+4+5)

def calculeaza_suma(n):
    if n == 1:
        return 1
    else:
        return n + calculeaza_suma(n - 1)

n = 78

print(f"Suma numerelor este: {calculeaza_suma(n)}")


#Exercitiul 3 
#Scrie o functie recursiva care calculeaza cate cifre are un numar dat.
#Ex: pentru 1234 returneaza 4

def calculeaza_cifre(numar):
    numar = abs(numar)
    if numar == 0:
        return 0
    else:
         return (numar % 10) + calculeaza_cifre(int(numar // 10))
    

numar = 123456

print(f"Suma cifrelor din numarul ales este: {calculeaza_cifre(numar)}")

#Exercitiul 4
#Scrie o functie recursiva care calculeaza adancimea(cate liste nivele de liste sunt) unei liste imbricate.
#Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 3

def calculeaza_adancime(lista):
    if not isinstance(lista, list):
        return 0

    if  not lista:
        return 0
    
    return 1 + max(calculeaza_adancime(element) for element in lista)

lista1 = [1, 2, [3, 4, [5, 6]], 7]
lista2 = [[[[[1]]]]] 
lista3 = [1, [2, 3], 4]
lista4 = []

print(f"Adancimea listei imbricate este: {calculeaza_adancime(lista1)}")
print(f"Adancimea listei imbricate este: {calculeaza_adancime(lista2)}")
print(f"Adancimea listei imbricate este: {calculeaza_adancime(lista3)}")
print(f"Adancimea listei imbricate este: {calculeaza_adancime(lista4)}")

#Exercitiul 5
#Scrie o functie recursiva care calculeaza suma tuturor elementelor dintr-o lista imbricata.
#Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 28

def suma_elemente_lista_imbricata(numere_lista):
    suma = 0

    for element in numere_lista:
        if type(element) != type([]):
            suma = suma + element
        else:
            suma = suma + suma_elemente_lista_imbricata(element)
    
    return suma

lista_imbricata = [1, 2, [3, 4, [5, 6]], 7]
print(F"Suma tuturor elementelor  din lista imbricata este: {suma_elemente_lista_imbricata(lista_imbricata)}")


def suma_pare_imbricata(lista):
    suma = 0
    
    for element in lista:
        if isinstance(element, list):
            suma += suma_pare_imbricata(element)
        else:
            if isinstance(element, (int, float)) and element % 2 == 0:
                suma += element
                
    return suma

lista = [1, [2, 3], [4, [5, 6]], 8]
print(F"Suma elementelor  pare din lista imbricata este: {suma_pare_imbricata(lista)}")


def suma_divizibile_3(lista):
    suma = 0
    for element in lista:
        if isinstance(element, list):
            suma += suma_divizibile_3(element)
        elif isinstance(element, (int, float)) and element % 3 == 0:
            suma += element
    return suma

lista = [1, [2, 3], [4, [5, 6]], 8]
print(F"Suma elementelor divizibile cu 3 din lista imbricata este: {suma_divizibile_3(lista)}")



def suma_negative(lista):
    suma = 0
    for element in lista:
        if isinstance(element, list):
            suma += suma_negative(element)
        elif isinstance(element, (int, float)) and element < 0:
            suma += element
    return suma


lista = [1, [-2, 3], [4, [-5, 6]], 8]
print(F"Suma elementelornegative din lista imbricata este: {suma_negative(lista)}")

#Tema dictionare

#Exercitiul 1
# Creeaza un dictionar care sa contina numele si varsta a 5 persoane.

persoane = {
    'Ioana': 34,
    'Maria': 23,
    'Anton': 45,
    'Marius': 29,
    'Mihaela': 34
}

print(persoane)


#Exercitiul 2
#Afiseaza varsta unei persoane specifificate de utilizator.

nume_cautat = input("Introduceti numele persoanei pentru care vreti sa aflati varsta: ")

varsta = persoane.get(nume_cautat, "Numele nu a fost gasit in dictionar.")

print(f"Varsta lui {nume_cautat} este: {varsta}")

#Exercitiul 3
#Afiseaza cea mai mare si cea mai mica varsta din dictionar.

varsta_mare = max(persoane.values())
varsta_mica = min(persoane.values())

print(f'Cea mai mare varsta din dictionar este: {varsta_mare}')
print(f'Cea mai mica varsta din dictionar este: {varsta_mica}')

#Exercitiul 4
#Adauga 3 noi persoane in dictionar.

persoane.update({'Ana': 29, 'Daniela': 34, 'Mihai': 18})
print(persoane)

#Exercitiul 5
#Afiseaza varsta medie a persoanelor din dictionar.

varsta_medie = sum(persoane.values()) / len(persoane)

print(f'Varsta medie a persoanelor din dictionar este: {varsta_medie}')

#Exercitiul 6
#Sterge o persoana specificata de utilizator din dictionar.

persoana_specificata = input("Introduceti numele persoanei pe care vreti sa o stergeti din dictionar: ")

persoane.pop(persoana_specificata)
print(persoane)


#Exercitiul 7
#Afiseaza toate persoanele cu varsta peste o valoare specificata de utilizator.

varsta_specificata = int(input("Introduceti o varsta: "))

for nume, varsta in persoane.items():
    if varsta > varsta_specificata:
        print(f"{nume}: {varsta} ani")
    else:
        print("Nu sunt persoane cu aceasta varsta!")


#Exercitiul 8
#Afiseaza toate persoanele din dictionar in urmatorul format: "Nume: <nume_persoana>, Varsta: <varsta_persoana>".

# Parcurgem dictionarul si formatam afisarea

for nume, varsta in persoane.items():
    print(f"Nume: {nume}, Varsta: {varsta}")


#Exercitiul 9
#Verifica daca o persoana specificata de utilizator exista in dictionar.

persoana_specificata = input("Introduceti numele persoanei: ")

if persoana_specificata in persoane:
    print("Persoana a fost gasita!")
else:
    print("Persoana nu a fost gasita in dictionar!")


#Exercitiul 10
#Actualizeaza varsta unei persoane specificate de utilizator.

persoana_specificata = input("Introduceti numele persoanei: ")
varsta_noua = int(input(f"Introduceti noua varsta pentru {persoana_specificata}: "))

persoane.update({persoana_specificata: varsta_noua})

print(persoane)

#Exercitiul 11 
#Afiseaza numarul total de persoane din dictionar.

numar_total_persoane = len(persoane)

print(f'Numarul total de persoane din dictionar este: {numar_total_persoane}')

#Exercitiul 12
#Creeaza o lista cu toate numele persoanelor din dictionar si afiseaza-le.


lista_nume = list(persoane.keys())

print(lista_nume)

#Exercitiul 13
#Creeaza un nou dictionar care sa contina doar persoanele cu varsta peste 18 ani.


adulti = {nume: varsta for nume, varsta in persoane.items() if varsta > 18}

print(f"Persoanele cu varsta peste 18 ani sunt: {adulti}")


#Exercitiul 14 
#Creeaza o lista care contine toate varstele din dictionar, fara duplicate, si afiseaz-o.


varste_unice = list(set(persoane.values()))

print(varste_unice)


#Exercitiul 15 
#Afiseaza persoana cu cea mai apropiata varsta de o valoare specificata de utilizator.

adauga_varsta = int(input("Introduceti varsta pe care o doriti: "))

nume_apropiat = None
diferenta_minima = float('inf') # Initializam cu o valoare foarte mare

for nume, varsta in persoane.items():
    diferenta = abs(varsta - adauga_varsta)
    
    if diferenta < diferenta_minima:
        diferenta_minima = diferenta
        nume_apropiat = nume

print(f"Cea mai apropiata persoana de varsta {adauga_varsta} este {nume_apropiat} si are {persoane[nume_apropiat]} de ani.")

#SAU

#Functia key evalueaza varsta corespunzatoare fiecarei chei

nume_apropiat = min(persoane, key=lambda nume: abs(persoane[nume] - adauga_varsta))
varsta_apropiata = persoane[nume_apropiat]


print(f"Cea mai apropiata persoana de varsta {adauga_varsta} este {nume_apropiat} si are {persoane[nume_apropiat]} de ani.")


#Exercitiul 16 
#Afiseaza toate persoanele grupate dupa decadele varstei (0-9, 10-19, 20-29, etc.)

grupate = {}

for nume, varsta in persoane.items():
    # Calculam decada (ex: 34 // 10 = 3, apoi 3 * 10 = 30)
    decada = int(varsta // 10) * 10
    interval = f"{decada}-{decada + 9}"
    
    if interval not in grupate:
        grupate[interval] = []
    
    grupate[interval].append(nume)   # Adaugam numele in lista corespunzatoare decadei

for interval, nume_persoane in sorted(grupate.items()):
    print(f"Decada {interval}: {', '.join(nume_persoane)}")


#Exercitiul 17 
#Afiseaza persoanele sortate alfabetic dupa nume.


lista_nume = list(persoane.keys())

lista_nume = sorted(persoane.keys())

print(lista_nume)


#Exercitiul 18 
#Afiseaza persoanele sortate dupa varsta, de la cea mai mica la cea mai mare. (Utilizati functia sorted pentru a rezolva acest exercitiu).
#(Folositi functia sorted() si pentru cheia de sortare (key) accesati valorile dictionarului).

varste_sortate = sorted(persoane.items(), key=lambda item: item[1])  # Spune programului să ignore ordinea numelor și să compare doar cifrele (vârstele)

for nume, varsta in varste_sortate:
    print(f"{nume}: {varsta} ani")

#Exercitiul 19
# Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
#Creeaza un dictionar care sa contina numele persoanelor ca si chei si varstele ca si valori.

dictionarul_meu = {
    'Ana':12,
    'Ion':15,
    'Maria':12,
    'George':15,
    'Elena':14
}

print(dictionarul_meu)

text = "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani"

cuvinte = text.replace(",", "").split()

persoane = {}

# Parcurgem cuvintele si cautam structura "Nume are Varsta"
for element in range(len(cuvinte)):
    if cuvinte[element] == "are":
        nume = cuvinte[element-1]
        varsta = int(cuvinte[element+1])
        persoane[nume] = varsta

print(persoane)


#Exercitiul 20
#Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
#Creeaza un dictionar care sa stocheze frecventa literelor din text si afiseaza-l. Exemplu: {'a': 7, 'n': 3, ... }.

text = "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani"

frecventa = {}

for caracter in text.lower():
    if caracter.isalpha():
        if caracter in frecventa:
            frecventa[caracter] +=1
        else:
            frecventa[caracter] = 1

print(frecventa)


# frecventa = {}: Inițializăm un dicționar gol.
# for numar in lista_numere:: Parcurgem fiecare număr din lista primită.
# if numar in frecventa:: Verificăm dacă numărul a fost deja adăugat în dicționar.
# frecventa[numar] += 1: Dacă există, creștem valoarea (frecvența) cu 1.
# else: frecventa[numar] = 1: Dacă nu există, adăugăm numărul în dicționar cu frecvența 1. 
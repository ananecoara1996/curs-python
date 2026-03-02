#Tema Vacanta

#Exercitiul 1
#Creează două variabile cu valori numerice și afișează suma lor.

variabila_a = 10 
variabila_b = 20

suma = variabila_a + variabila_b

print(suma)

#Exercitiul 2
#Afișează produsul a două numere introduse de la tastatură.

x = int(input('Valoarea lui x este: '))
y = int(input('Valoarea lui y este: '))

produs = x * y

print(produs)


#Exercitiul 3
#Primește un nume de la tastatură și afișează-l cu litere mari.

nume = input("Introduceți un nume: ")

print(nume.upper())


#Exercitiul 4 
#Afișează lungimea unui string introdus de la tastatură.

my_str = input("Introduceti un sir de caractere: ")

print(my_str)
print(len(my_str))


#Exercitiul 5
#Verifică dacă un număr este par sau impar.

numar = int(input ("Introduceti un numar : "))

if numar % 2 == 0: 
    print("Numarul este par! ")
else:
    print("Numarul este impar! ")


#Exercitiul 6
#Primește un text și un caracter, afișează de câte ori apare caracterul în text.

text = " Acesta este un exemplut de text."
caracter_cautat = 'e'

numar_aparitii = text.count(caracter_cautat)

print (f"Caracterul cautat '{caracter_cautat}' apare in text de {numar_aparitii} ori.")


#Exercitiul 7
#Afișează ultimul caracter dintr-un string introdus de la tastatură.

str_introdus = input("Introduceti un sir de caractere: ")

print(str_introdus)

ultimul_caracter = str_introdus[-1]

print(ultimul_caracter)


#Exercitiul 8
#Primește un număr și afișează dacă este pozitiv, negativ sau zero.

numar_introdus = float(input("Introduceti un numar: "))

if numar_introdus > 0: 
    print("Numarul introdus este pozitiv!")
elif numar_introdus < 0:
    print("Numarul introdus este negativ!")
else:
    print("Numarul introdus este zero!")


#Exercitiul 9
#Afișează toate caracterele unui string, câte unul pe linie.

text = " Afara ninge linistit! "

for char in text:
    print(char)


#Exercitiul 10 
# Primește două numere și afișează cel mai mare dintre ele.

numar_a = input("Introduceti valoarea numarului a: ")
numar_b = input("Introduceti valoarea numarului b: ")

if numar_a > numar_b: 
    print("Numarul a este mai mare decat numarul b ")
    print(numar_a)
elif numar_a < numar_b:
    print("Numarul a este mai mic decat numarul b ")
else:
    print("Numerele sunt egale!")


#Exercitiul 11  
# Primește trei numere și afișează cel mai mic dintre ele.

numar_1 = int(input("Introduceti o valoare pentru numar_1: "))
numar_2 = int(input("Introduceti o valoare pentru numar_2: "))
numar_3 = int(input("Introduceti o valoare pentru numar_3: "))


if numar_1 <= numar_2 and numar_1 <= numar_3:
    minim = numar_1
elif numar_2 <= numar_1 and numar_2 <= numar_3:
    minim = numar_2
else:
    minim = numar_3

#print(min(numar_1,numar_2,numar_3))

print(f"Cel mai mic numar este: {minim}")


#Exercitiul 12
#Primește un text și verifică dacă este palindrom.

text_introdus = input("Introduceti un text: ")
text_inversat = text_introdus[::-1]
print(text_inversat)

if text_introdus == text_inversat:
    print("Este palindrom!")
else:
    print("Nu este palindrom!")


#Exercitiul 13 
#Primește o parolă și verifică dacă are cel puțin 8 caractere și conține o cifră.

parola = input("introduceti o parola de la tastatura pentru verificare: ")

print (len(parola))

if (len(parola)) >= 8 and  any(char.isdigit() for char in parola):
    print("Parola este valida!")
else:
    print("Parola nu este valida!")


#Exercitiul 14
#Primește un text și construiește un nou string numai cu vocalele din el.

text_nou = input("Introduceti un nou text: ")

vocale = 'aeiouAEIOU'
rezultat = ''.join([char for char in text_nou if char in vocale])

print("Vocalele sunt:", rezultat)


#Exercitiul 15
#Primește un număr n și afișează toate numerele pare de la 0 la n (inclusiv).

n = int(input ("Introduceti o valoare pentru n: "))

for i in range(n + 1):
    if i % 2 == 0:
        print(i)


#Exercitiul 16
#Primește un text și afișează doar literele mici din el.

text_cu_litere_mici_si_mari = "Textul acesta contine SI liteRe mici Si LITERE mari. "

text_litere_mici = "".join(char for char in text_cu_litere_mici_si_mari if char.islower() or char.isspace())

print(f"Textul care contine doar litere mici: {text_litere_mici}")


#Exercitiul 17
#Primește două numere și afișează toate numerele între ele (inclusiv), în ordine crescătoare.

numar_1 = 4 
numar_2 = 78

while numar_1 <= numar_2:
    print(numar_1)
    numar_1 +=1 


#Exercitiul 18
#Primește un text și afișează fiecare cuvânt pe o linie nouă.

text = 'Acesta este un text.'

cuvant = text.split()

for char in cuvant:
    print(char)


#Exercitiul 19
#Primește un număr și afișează tabla înmulțirii pentru acel număr (de la 1 la 10).

numar = int(input("Introduceti un număr pentru tabla inmultirii: "))

print(f"Tabla inmultirii pentru {numar} este: ")

for i in range(1, 11):
    rezultat = numar *i
    print(f"{numar} x {i} = {rezultat}")


#Exercitiul 20
#Primește un text și verifică dacă toate caracterele sunt litere mici.

text = 'Acesta este un text.'

if text.islower():
    print("Textul contine doar caractere sunt cu litere mici.")
else:
    print("Textul contine atat caractere cu litere mari, cat si caractere cu litere mici.")


#Exercitiul 21
#Primește un text și afișează-l inversat.

text_introdus = 'Acesta este un exemplu de text.'

text_inversat = text_introdus[::-1]

print(text_inversat)

#Exercitiul 22
#Primește o propoziție și numără câte cuvinte conține.

propozitie = "Ianuarie este o luna de iarna. "

cuvinte_propozitie = propozitie.split()

print(cuvinte_propozitie)

numar_cuvinte = len(cuvinte_propozitie)

print(f"Propozitia are {numar_cuvinte} cuvinte. ")


#Exercitiul 23 
#Primește un text și înlocuiește toate spațiile cu caracterul "_".

text = "Ianuarie este o luna de iarna."

text_inlocuit = text.replace(' ', '_')

print(text_inlocuit)

#Exercitiul 24
#Primește un număr și afișează suma cifrelor sale.

numar = input("Introduceti o valoare pentru numarul n: ")

suma = sum(int(cifra) for cifra in numar if cifra.isdigit()) 

print(f"Suma cifrelor numarului {numar} este: {suma}")


#Exercitiul 25
#Primește un text și afișează doar caracterele care sunt cifre.

text_1 = "Acest text contine 2334 cifre. "

doar_cifre = ""

for char in text_1:
    if char.isdigit():
        doar_cifre += char

print(doar_cifre)


#Exercitiul 26
#Primește un text și verifică dacă începe și se termină cu aceeași literă.

text = "Acesta este un exemplu de textA"

if text.startswith('A') and text.endswith('A'):
    print("Textul incepe si se termina cu aceeasi litera.")
else:
    print("Textul nu incepe si nu se termina cu aceeasi litera.")
    

#Exercitiul 27
#Primește un text și afișează toate caracterele distincte din el.

text = input("Introduceti textul: ")
caractere_unice = set(text)

print("Caracterele distincte sunt:", "".join(caractere_unice))

#Exercitiul 28
#Primește un text și afișează literele care apar de exact două ori.

text = input("Introduceti un text: ")
litere_repetate = ""

for char in text:
    if text.count(char) == 2 and char not in litere_repetate:
        litere_repetate +=char

print (f"Literelele repetate de doua ori sunt: {litere_repetate}")

#Exercitiul 29
#Primește un număr n și afișează toți divizorii săi.

numar = int(input("Introduceti un numar: "))

print (f"Divizorii numarului {numar} sunt: ")

for i in range (1, numar+1):
    if numar % i == 0:
        print (i)


#Exercitiul 30
#Primește un text și verifică dacă are cel puțin o literă mare, una mică și o cifră.

text = "Acest text Are si Litere mari, LiterE mici si 34 de cifre. "

capital = False
lower = False
digit = False

for char in text:
    if char.isupper():
        capital = True
    if char.islower():
        lower = True
    if char.isdigit():
        digit = True
if not (capital and digit and lower):
    print("Sa adaugam altceva!")

#Exercitiul 31
'''Fizz Buzz: Primește un număr n și afișează numerele de la 1 la n. 
Pentru multiplii de 3, afișează "Fizz", pentru multiplii de 5, afișează "Buzz", iar pentru multiplii de ambele, afișează "FizzBuzz".'''

n = input ("Introduceti un numar:")

for x in range(1, n+1):
    if x % 3 == 0 and x % 5 ==0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("buzz")
    elif x % 3 == 0:
        print ("fizz")


#Exercitiul 32
#Primește un text și afișează-l cu fiecare cuvânt inversat, dar în aceeași ordine. (Exemplu: "Ana are mere" -> "anA era erem")

text = "Ana are mere."
cuvinte = text.split()
lista_inversata = []

for cuvant in cuvinte:
    lista_inversata.append(cuvant[::-1])

print(lista_inversata)

rezultat = " ".join(lista_inversata)
print(rezultat)
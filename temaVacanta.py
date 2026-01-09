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

for caracter in text:
    print(caracter)


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

numar_1 = input("Introduceti o valoare pentru numar_1: ")
numar_2 = input("Introduceti o valoare pentru numar_2: ")
numar_3 = input("Introduceti o valoare pentru numar_3: ")

if (numar_1 < numar_2) and (numar_1 < numar_3):
    print(f'Numarul 1 este cel mai mic dintre toate si are valoarea: {numar_1}')


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

if (len(parola)) >= 8 and  any(is.digit)
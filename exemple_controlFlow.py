# x = 15

# if x % 3 == 0 and x % 5 ==0:
#     print("FizzBuzz")
# elif x % 5 == 0:
#     print("buzz")
# elif x % 3 == 0:
#     print ("fizz")
# else:
#     print("Afisam altceva!")

# numar_1 = int(input("Valoarea_1: "))
# numar_2 = int(input("Valoarea_2: "))

# while numar_1 <= numar_2:
#     print(numar_1)
#     numar_1 +=1 


# text = "Acesta este un exemplu de textA"

# if text.startswith('A') and text.endswith('A'):
#     print("Textul incepe si se termina cu aceeasi litera.")
# else:
#     print("Textul nu incepe si nu se termina cu aceeasi litera.")
   
text = "Acest text Are si Litere mari, LiterE mici si 34 de cifre. "

print(text)

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

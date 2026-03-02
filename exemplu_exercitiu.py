# print("Meniu Interactiv Calculator")
# print("1. Adunare")
# print("2. Scadere")
# print("3. Inmultire")
# print("4. Impartire")
# print("5. Iesire din program")

# optiune = input("Introduceți optiunea (1-5): ")

# if optiune == '5':
#       print("Iesire din program")

# elif optiune in ('1', '2', '3', '4'):
#       num1 = float(input("Introduceți primul număr: "))
#       num2 = float(input("Introduceți al doilea număr: "))
#       if optiune == '1':
#             rezultat = num1 + num2
#             print(f"Rezultatul adunarii: {rezultat}")
#       if optiune == '2':
#             rezultat = num1 - num2
#             print(f"Rezultatul scaderii: {rezultat}")
#       if optiune == '3':
#             rezultat = num1 * num2
#             print(f"Rezultatul inmultirii: {rezultat}")
#       if optiune == '4':
#             rezultat = num1 / num2
#             print(f"Rezultatul impartirii: {rezultat}")
      
# else:
#       print("Optiune invalida. Va rugam alegeti o optiune intre 1 și 5.")    

text = "Ana are mere."
cuvinte = text.split()
lista_inversata = []

for cuvant in cuvinte:
    lista_inversata.append(cuvant[::-1])

print(lista_inversata)

rezultat = " ".join(lista_inversata)
print(rezultat)


# a = 14
# b = 12

# if a < b: 
#     print ("numarul a este mai mic decat b ")
# elif a > b: 
#     print ("numarul a este mai mare decat b ")
# else:
#     print("Numerele a si b sunt egale")


# if a < b and a % 2 == 0:
#     print("a este mai mic decat b si a este numar par")

# if a < b:
#     print("a este mai mic decat b")
# if a % 2 == 0:
#         print("a este si numar par")

my_str = 'mama are 10 pere'

for char in my_str:
    print(char)

print(my_str.split())

for cuvant in my_str.split():
    #print(cuvant)
    lungime_str = len(cuvant)
    #print(lungime_str)
    print(f'{cuvant} -> {lungime_str} litere')
    
text = ''

for char in my_str:
    if char.isdigit():
        text += char

print("Cifrele sunt:" + text)  

for numar in range(2,4,2):
    print(numar)

numar = 1
limita = 5
while numar <=limita:
    print(numar)
    numar +=1
import logging
logging.basicConfig(
     level=logging.DEBUG,
     filename='app.log', 
     format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)s - %(message)s')

# logging.debug('Acesta este un mesaj de DEBUG')
# logging.info('Acesta este un mesaj de tip info')
# logging.critical('Acesta este un mesaj critic')
# logging.warning('Acesta este un mesaj de warning')
# logging.error('error message')

#se citesc 2 numere de laa tastatura si se calculeaza suma lor.
#Programul ruleaza pana la introducerea tastei x.


# def aduna(nr1, nr2):
#     suma = nr1 + nr2
#     return suma

# logging.info('Application started')
# while True:
#     try:
#         nr1 = int(input('Introduceti numarul 1: '))
#         nr2 = int(input('Introduceti numarul 2: '))
#         logging.debug(f'Numerele introduse sunt: {nr1} si {nr2}')
#         aduna(nr1, nr2)
#         print("Suma este: ",aduna(nr1, nr2))
#         if nr1 == 'x' or nr2 =='x':
#             break
#     except ValueError:
#         logging.error('Unul dintre numere nu este integer: ')
#         print("Te rog sa introduci doar numere sau litera 'x' pentru a inchide.")

# logging.info('Application closed')



#Avem o lista cu elementele [10, -5, 5, 12, 20, 30, -6]

# def data_processor(lista):
#     logging.info('incepere procesare')
#     for index, value in enumerate(lista):
#         if value < 0: 
#           logging.warning(f"Valoare negativa {value} la pozitia {index}")
#         else:
#           logging.debug(f"Valoarea citita: {value}")
#           processing_result = value / 2
#           print(f"Processed result:{processing_result}")
#           logging.debug(f"Processing result: {processing_result}")
# logging.info('Procesare finalizata')
    


# date = [10, -5, 5, 12, 20, 30, -6]
# data_processor(date)

# import math


# def calcul_logaritm(x):
#     assert x > 0, f'Numarul introdus trebuie sa fie pozitiv (valoarea introdusa: {x})'
#     logaritm = math.log(x)
#     return logaritm

# print(calcul_logaritm(10))
# print(calcul_logaritm(-1))

# print(10 / 0)


# try:
#     print(10 / 0)
# except Exception as exceptie:
#     print(exceptie)

import traceback

# while True:
#      x = input("Introduceti numar: ")
#      if x == 'x':
#           break

#      try:
#           print(10 / 0)
#      except Exception as exceptie:
#           print('A aparut o eroare la impartire!')
#           traceback.print_exc()
#           print(f'Exceptia aparuta este: {exceptie}')


def functia_a(x):
    return functie_b(x)

def functie_b(y):
    return functie_c(y)

def functie_c(z):
    return 10 / z

while True:
     x = input("Introduceti numar: ")
     if x == 'x':
          break

     try:
          rezultat = functia_a(int(x))
     except Exception as exceptie:
          print('A aparut o eroare la apelarea functiei a!')
          traceback.print_exc()
          print(f'Exceptia aparuta este: {exceptie}')
     else:
          print(rezultat)
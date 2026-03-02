#import random as rand
from random import randint as r

def calcul():
    a = r(1, 5)
    b = r(1, 5)
    return a + b 

print(calcul())


#import sys 


# def afiseaza_nume(nume, prenume):
#     print(f'Nume: {nume}, Prenume: {prenume}')

# def main():
#     lista_argumente = sys.argv
#     print(sys.argv)
#     afiseaza_nume(lista_argumente[1], lista_argumente[2])

# if __name__ == '__main__':
#     main()

import argparse

my_parser = argparse.ArgumentParser(description= 'Afiseaza nume frumos')

my_parser.add_argument('--nume', type=str, default='Necoara', help='Nume de familie')
my_parser.add_argument('--prenume', type=str, help='Prenumele de familie')

args = my_parser.parse_args()
print(f'Nume: {args.nume}, Prenume: {args.prenume}')
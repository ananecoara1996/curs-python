from random import randint as rand
import operations as op
import string_utils as st
import geometry 
from geometry import area, perimeter

def main():
    
    num1 = rand(1, 100)
    num2 = rand(1, 100)
    
    print(f"Numerele generate sunt: {num1} si {num2}\n")

    rezultat_adunare = op.adunare(num1, num2)
    rezultat_scadere = op.scadere(num1, num2)
    rezultat_inmultire = op.inmultire(num1, num2)
    rezultat_impartire = op.impartire(num1, num2)

    print(f"Rezultatul adunarii celor 2 numere este: {rezultat_adunare}")
    print(f"Rezultatul scaderii celor 2 numere este: {rezultat_scadere}")
    print(f"Rezultatul inmultirii celor 2 numere este: {rezultat_inmultire}")
    print(f"Rezultatul impartirii celor 2 numere este: {rezultat_impartire}")

    text_introdus = input("Introduceti un text: ")
    cuvant = input("Introduceti un cuvant: ")
    text_inversat = st.inversare(text_introdus)
    cuvant_palindrom = st.este_palindrom(cuvant)
    print(f"Inversul lui '{text_introdus}' este: {text_inversat}")
    print(f"Cuvantul {cuvant} este palindrom si arata asa: {cuvant_palindrom}")


    r = rand(1, 10)  
    latura_patrat = rand(1, 10) 
    lungime_drept = rand(1, 10) 
    latime_drept = rand(1, 10) 

    print(f"Valorile generate sunt: raza={r}, latura_patrat={latura_patrat}, Lungime_dreptunghi={lungime_drept}, latime_dreptunghi={latime_drept}")

    print(f"Arie Cerc: {area.cerc(r)}")
    print(f"Arie Patrat: {area.patrat(latura_patrat)}")
    print(f"Arie Dreptunghi: {area.dreptunghi(lungime_drept, latime_drept)}")

    print(f"Perimetru Cerc: {perimeter.cerc(r)}")
    print(f"Perimetru Patrat: {perimeter.patrat(latura_patrat)}")
    print(f"Perimetru Dreptunghi: {perimeter.dreptunghi(lungime_drept, latime_drept)}")


if __name__ == "__main__":
    main()


#Sa se creeze un pachet numit "geometry" care sa contina doua module: "area" si "perimeter". Modulul "area" sa contina functii pentru calcularea ariei unui cerc, 
# patrat si dreptunghi, iar modulul "perimeter" sa contina functii pentru calcularea perimetrului acelorasi forme geometrice.
#Din fisierul principal, sa se importe pachetul si sa se execute fiecare functie cu valori generate aleatoriu.

import math as m

def cerc(raza):
    perimetru_cerc = 2 * m.pi * raza
    return perimetru_cerc

def patrat(latura):
    perimetru_patrat = 4 * latura
    return perimetru_patrat

def dreptunghi(lungime, latime):
    perimetru_dreptunghi = 2 * (lungime + latime)
    return perimetru_dreptunghi
    
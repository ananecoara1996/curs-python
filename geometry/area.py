#Sa se creeze un pachet numit "geometry" care sa contina doua module: "area" si "perimeter". Modulul "area" sa contina functii pentru calcularea ariei unui cerc, 
# patrat si dreptunghi, iar modulul "perimeter" sa contina functii pentru calcularea perimetrului acelorasi forme geometrice.
#Din fisierul principal, sa se importe pachetul si sa se execute fiecare functie cu valori generate aleatoriu.

import math as m

def cerc(raza):
    aria_cerc = m.pi * (raza ** 2)
    return aria_cerc

def patrat(latura):
    aria_patrat = latura ** 2
    return aria_patrat

def dreptunghi(lungime, latime):
    aria_dreptunghi = lungime * latime
    return aria_dreptunghi


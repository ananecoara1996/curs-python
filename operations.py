#Sa se creeze un modul numit "operations" care sa contina functii pentru adunare, scadere, inmultire si impartire a doua numere.
#Din fisierul principal, sa se importe modulul si sa se execute fiecare operatie cu doua numere generate aleatoriu.


def adunare(a, b):
    suma = a + b
    return suma

def scadere(a, b):
    scadere = a - b
    return scadere

def inmultire(a, b):
    produs = a * b 
    return produs

def impartire(a, b):
    if b == 0:
        return "Eroare la impartirea cu zero"
    return a / b

print(adunare(4, 5))
print(scadere(7, 5))
print(inmultire(2, 3))
print(impartire(6, 3))


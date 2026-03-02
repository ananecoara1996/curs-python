#------------------------------------------------------------------------------
#Exercitii cu tuple

#Exercitiul 1
#Creează un tuplu care conține numele a trei fructe și afișează-le pe ecran.
#Exemplu: ('măr', 'banană', 'cireașă') -> măr, banană, cireașă

tuple_fructe = ('mar', 'banana', 'cireasa')
print(f"Fructele din tuple sunt: \n{tuple_fructe[0]}, {tuple_fructe[1]}, {tuple_fructe[2]}")


#Exercitiul 2
# Se da tuplul: fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi').
# Afișează al doilea și al patrulea fruct din tuplu.

fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
print(f"Al doilea fruct din tuplu este {fructe[1]}, iar al patrulea fruct din tuplu este {fructe[3]}")

#Exercitiul 3
# Afișează tuplul inversat.

fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')
print(fructe[::-1])

#Exercitiul 4
# Verifică dacă 'kiwi' este în tuplu și afișează un mesaj corespunzător.

fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')

if 'kiwi' in fructe:
    print("Kiwi este in tuplu.")
else:
    print("Kiwi nu este in tuplu.")

#Exercitiul 5
# Creează un tuplu nou care conține doar fructele de la pozițiile(index) pare din tuplul original.

fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')

fructe_pare = fructe[::2]
print(fructe_pare)

#Exercitiul 6
#Afișează lungimea fiecarui element din tuplu.

fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')

#fructe_lungime = [len(fruct) for fruct in fructe]

for fruct in fructe:
    print(f"Lungimea fructului '{fruct}' din tuplu este: {len(fruct)}")

#Exercitiul 7
#Concatenează tuplul cu un alt tuplu care conține alte două fructe și afișează rezultatul.

fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')

fructe_exotice = ('ananas', 'mango', )
fructe += fructe_exotice
print(fructe)

#Exercitiul 8
#Adauga un fruct nou 'ananas' in tuplu.

fructe = ('măr', 'banană', 'cireașă', 'portocală', 'kiwi')

lista_fructe = list(fructe)

lista_fructe.append('ananas')

fructe = tuple(lista_fructe)

print(fructe)

#Exercitiul 9
#Se da tuplul: ('măr', 'banană', 'cireașă'). Faceti unpacking pentru a extrage fiecare element in variabile separate si afisati-le.

tuplu_fructe = ('măr', 'banană', 'cireașă')
print(tuplu_fructe)

fruct_1, fruct_2, fruct_3 = tuplu_fructe
print(fruct_1)
print(fruct_2)
print(fruct_3)

#-------------------------------------------------------------------------
#Exercitii cu sets 

#Exercitiul 1
#Creează un set care conține numele a cinci culori și afișează-le pe ecran.

set_culori = {'verde', 'albastru', 'rosu', 'galben', 'portocaliu'}

print(set_culori)

#Exercitiul 2
#Adaugă o culoare nouă în setul de mai sus și afișează setul actualizat.

set_culori = {'verde', 'albastru', 'rosu', 'galben', 'portocaliu'}
set_culori.add('negru')
print(set_culori)

#Exercitiul 3
#Elimină o culoare din set și afișează setul actualizat.

set_culori = {'verde', 'albastru', 'rosu', 'galben', 'portocaliu'}
print(set_culori)
set_culori.remove('rosu')
print(f"Setul actualizat este: {set_culori}")

#Exercitiul 4 
#Verifică dacă o anumită culoare (de exemplu, 'albastru') este în set și afișează un mesaj corespunzător.

set_culori = {'verde', 'albastru', 'rosu', 'galben', 'portocaliu'}

if 'albastru' in set_culori:
    print("Culoarea 'albastru' exista in set.")
else:
    print("Culoarea nu exista in set.")

#Exercitiul 5
#Creează un alt set cu alte trei culori și afișează elementele comune din cele două seturi.

set_culori = {'verde', 'albastru', 'rosu', 'galben', 'portocaliu'}

set_nou = {'albastru', 'rosu', 'gri'}

culori_comune = set_culori.intersection(set_nou)

print(f"Culorile comune sunt: {culori_comune}")

#Exercitiul 6
#Afișează toate culorile din primul set care nu sunt în al doilea set.

set_culori = {'verde', 'albastru', 'rosu', 'galben', 'portocaliu'}

set_nou = {'albastru', 'rosu', 'gri'}

print(f"Culorile care se afla in primul set si nu sunt in al doilea set sunt: {set_culori.difference(set_nou)}")
print(f"Culorile care se afla in al doilea set si nu sunt in primul set sunt: {set_nou.difference(set_culori)}")

#Exercitiul 7
# Se da lista: [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]. Eliminati duplicatele din lista,
# astfel incat fiecare element sa apara o singura data.

lista_mea = [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]

lista_noua = set(lista_mea)

print(lista_noua)


#-----------------------------------------------------

'''Se dau urmatoarele expresii matematice:
((a + b) * (c - d) + e) / f - (g * (h + i)) -> corect deschise si inchise
((a + b) * (c - d) + e) / f - )g * (h + i)( -> incorect deschise si inchise
Sa se verifice daca parantezele sunt corect deschise si inchise.'''

exp1 = "((a + b) * (c - d) + e) / f - (g * (h + i))"
exp2 = "((a + b) * (c - d) + e) / f - )g * (h + i)("

def verifica_paranteze(expresie):  
    stiva = []
    for caracter in expresie:                            #Parcurgem expresia caracter cu caracter
        if caracter == '(':                              #Daca gasim o paranteza deschisa ( 
            stiva.append(caracter)                       #o adaugam in stiva
        elif caracter == ')':                            #Daca gasim o paranteza inchisa )
            if not stiva:                                #verificam daca stiva este goala
                return "incorect deschise si inchise"    #Daca este goala, inseamna ca avem o paranteza inchisa fara una deschisa(incorect).
            stiva.pop()                                  #scoatem ultimul element din stiva
    
    return "corect deschise si inchise" if not stiva else "incorect deschise si inchise"

print(f"{exp1} -> {verifica_paranteze(exp1)}")
print(f"{exp2} -> {verifica_paranteze(exp2)}")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)



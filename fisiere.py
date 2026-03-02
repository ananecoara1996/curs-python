# def suma(numar1, numar2):
#     suma = numar1 + numar2
#     return suma

# print(suma(5, 4))

# mesaj = "Salut! "
# nume_fisier = "fisierul_meu.text"

# my_file = open("fisierul_meu.text", 'w')
# my_file.write(mesaj)
# my_file.close()


# my_file = open(nume_fisier, 'r')
# data = my_file.readlines()
# print(data[0])


# mesaj1 = "Ana are mere"
# mesaj2 = "Matei este nazdravan"
# mesaj3 = "Matei se uita la desene"

# my_file = open(nume_fisier, 'a')
# my_file.write(mesaj1 + "\n")
# my_file.write(mesaj2 + "\n")
# my_file.write(mesaj3 + "\n")
# my_file.close()





# my_file = open(nume_fisier, "r") 
# linii_fisier = my_file.read()
# linie_noua = linii_fisier.replace("Ana", "Ionela")

# my_file = open(nume_fisier, "w")
# my_file.write(linie_noua)
# my_file.close()


# with open("fisierul_meu.text", 'r') as file:
#     text = file.read()

# text = text.replace('Ana', 'Ionela')

# with open("fisierul_meu.text", 'w') as file:
#     file.write(text)
#     print("Modificarea a fost facuta")


# with open("fisierul_meu.text", 'r') as file:
#     for line in file:
#         print(line)

# with open('fisierul_meu.text', 'r', encoding="utf-8") as input_file, open('temp.txt','w') as output_file:
#     for line in input_file:
#         output_file.write(line[::-1])
#     print('Rescriere fisier reusita!')


# import os



# print(os.listdir("C:\Users\anane\Documents\GitHub\curs-python\exemplu_exercitiu.py"))
# my_path = os.path.join("C:\Users\anane\Documents\GitHub\curs-python\exemplu_exercitiu.py\ceva")
# print(my_path)
# print(os.path.isdir(my_path))
# print(os.path.isfile(my_path))

# #sa verificam daca in exemplu_project ->data -> file1.py


# continut_proiect = os.listdir(r"C:\Users\anane\Documents\GitHub\curs-python")
# print(continut_proiect)


# path_proiect = r"C:\Users\anane\Documents\GitHub\curs-python"
# continut_proiect = os.listdir(path_proiect)
# if 'ceva' in continut_proiect:
#     print('Folderul este gasit!')
#     path_ceva = os.path.join(path_proiect, 'ceva')
#     continut_ceva = os.listdir(path_ceva)
#     print(continut_ceva)

# else:
#     print('Folderul ceva nu exista, deci nu avem fisier txt pe care sa il citim')

# # for nume in elemente:
# #     if nume.endswith('.txt'):
# #         new_path = os.path.join(path_ceva, nume)
# #         if os.path.isfile(new_path):
# #             with open (new_path, 'r') as my_file:
# #                 print(my_file.read())

# path_proiect = r"C:\Users\anane\Documents\GitHub\curs-python"
# for root, dirs, files in os.walk(path_proiect):
#     print(root, dirs, files)

# try:
#     with open('macarena.txt', 'r') as my_file:
#         print(my_file.read())
# except Exception as my_exception:
#     print(my_exception)
#     print('Fisierul macarena.txt nu exista')
# else:
#     print('Fisierul deschis cu succes!')
    


#Exercitiul 1 
#Sa se scrie un program care parcurge recursiv un folder specificat de utilizator si afiseaza numele tuturor fisierelor cu extensia ".py".

import os

def gaseste_fisiere_python(folder_path):
    try:
        for root, dirs, files in os.walk(folder_path):
             for file in files:
                if file.endswith(".py"):
                    print(os.path.join(root, file))
    except FileNotFoundError:
        print("Eroare: Folderul specificat nu exista.")
    except PermissionError:
        print("Eroare: Nu aveti permisiunea de a accesa acest folder.")


#Exercitiul 2
#Sa se scrie un program care parcurge recursiv un folder specificat de utilizator si afiseaza calea absoluta a tuturor fisierelor ".txt".

def afiseaza_fisiere_txt_recursiv(folder_path):
    try:
    # os.walk parcurge recursiv (root, subdirectories, files)
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # Verificăm extensia
                if file.lower().endswith(".txt"):
                # Construim calea completă și o transformăm în cale absolută
                    file_path = os.path.join(root, file)
                    print(os.path.abspath(file_path))
    except FileNotFoundError:
        print("Eroare: Folderul specificat nu exista.")
    except PermissionError:
        print("Eroare: Nu aveti permisiunea de a accesa acest folder.")
    except Exception as my_exception:
        print(my_exception)
    

#Exercitiul 3
#Sa se scrie un program care parcurge recursiv un folder si scrie intr-un fisier calea absoluta catre toate fisierele gasite in folderul respectiv.



#Exercitiul 4
#Sa se scrie un program care parcurge recursiv un folder si afiseaza numarul total de fisiere si directoare din acel folder.

def numara_elemente_recursiv(cale_director):
    numar_fisiere = 0
    numar_directoare = 0

    try:
        # Parcurgem elementele din directorul curent
        for element in os.listdir(cale_director):
            cale_completa = os.path.join(cale_director, element)
            
            if os.path.isdir(cale_completa):
                # Dacă este director, îl numărăm și apelăm funcția recursiv
                numar_directoare += 1
                fisiere, directoare = numara_elemente_recursiv(cale_completa)
                numar_fisiere += fisiere
                numar_directoare += directoare
            else:
                # Dacă este fișier, îl numărăm
                numar_fisiere += 1
    except PermissionError:
        # Ignorăm folderele pentru care nu avem drepturi de acces
        pass
    except Exception as my_exception:
        print(my_exception)

    return numar_fisiere, numar_directoare

#Exercitiul 5
#Sa se scrie un program care primeste un folder si o extensie de fisier de la utilizator si parcurge recursiv folderul
#pentru a afisa numele tuturor fisierelor care au acea extensie.



if __name__ == "__main__":
    #Ex 1
    cale_utilizator = input("Introduceti calea catre folder: ")
    gaseste_fisiere_python(cale_utilizator)

    #Ex2
    director = input("Introduceti calea folderului: ")
    afiseaza_fisiere_txt_recursiv(director)

    #Ex4
    cale = input("Introduceti calea folderului: ")
    fisiere, directoare = numara_elemente_recursiv(cale)
    print(f"Total fisiere: {fisiere}")
    print(f"Total directoare: {directoare}")
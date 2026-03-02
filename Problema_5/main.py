'''Se da urmatoarea structura de directoare care contine informatii despre elevii dintr-o scoala:
school_files/high_school/classA - contine fisiere CSV cu informatii despre elevii de la filologie
school_files/high_school/classB - contine fisiere JSON cu informatii despre elevii de la mate-info 
 Sa se scrie un program care parcurge recursiv structura de directoare "school_files" si:
Afiseaza toti elevii din clasele de Filologie (ClassA) care au nota peste 90 la Istorie
Afiseaza toti elevii din clasele de Mate-Info (ClassB) care au media mai mica decat 80
Calculeaza media generala a tuturor claselor de Filologie
Afiseaza clasele de Mate-info in ordine crescatoare a mediei generale pe clasa
Afiseaza elevii cu cea mai mare medie din fiecare clasa
Convertește fisierele csv in care sunt salvate informatiile despre elevii de la Filologie in fisiere json.
Convertește fisierele json in care sunt salvate informatiile despre elevii de la Mate-Info in fisiere csv.
'''


import csv
import json
import os

classA = "Problema_5\high_school\classA"
classB = "Problema_5\high_school\classB"

print(os.listdir(classA))

# for file_name in os.listdir(classA):
#     complete_path = os.path.join(classA, file_name)
#     print(complete_path)

#     with open(complete_path, "r", newline="") as my_file:
#         dict_reader = csv.DictReader(my_file)
#         for row in dict_reader:
#             if int(row['History']) >= 90:
#                 print(row)

for file_name in os.listdir(classB):
    complete_path = os.path.join(classB, file_name)
    
    with open(complete_path, "r") as my_file:
        date_elevi = json.load(my_file)

        for elev in date_elevi:
            nume = elev['name']
            nota = elev['grades']
            print(nota)
            media = int(nota['math'] + nota['english'] + nota['science'])/3
            if media <= 80:
                print(f"{nume} are {media}")

for file_name in os.listdir(classA):
    complete_path = os.path.join(classA, file_name)
    print(complete_path)
    with open(complete_path, "r") as my_file:
        reader = csv.DictReader(my_file)
        lista_medii = []
        for row in reader:
            medie_elev = (int(row['Geography']) + int(row['English']) + int(row['History']))/3
            lista_medii.append(medie_elev)
            media_clasei = sum(lista_medii)/len(lista_medii)
            print(medie_elev)
            print(media_clasei)



            
        



'''Sa se scrie un program care tine evidenta elevilor dintr-o scoala. Programul trebuie sa dispuna de un meniu care ne pune la dispozitie urmatoarele optiuni:
		a. Adaugare elev
		b. Afisarea elevilor existenti
		c. Modificare informatii elev existent
		d. Stergere elev
		e. Cautare elev dupa nume si prenume
		f. Afisare elevi in ordinea mediilor
		g. Afisare elevi cu media peste 8
		h. Afisare elevi in ordine alfabetica (dupa nume)

	Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
    Nume
    Prenume
    Nota romana
    Nota matematica
    Nota engleza
    Media
'''

def afiseaza_meniu():
    print("Program evidenta elevi")
    print("1. Adauga elev")
    print("2. Afisarea elevilor existenti")
    print("3. Modificare informatii elev existent")
    print("4. Stergere elev")
    print("5. Cautare elev dupa nume si prenume")
    print("6. Afisare elevi in ordinea mediilor")
    print("7. Afisare elevi cu media peste 8")
    print("8. Afisare elevi in ordine alfabetica (dupa nume)")
    print("9. Iesire")

def adauga_elev(lista_elevi):
    nume = input("Nume elev: ")
    prenume = input("Prenume: ")
    nota_romana = input("Nota la romana: ")
    nota_matematica = input("Nota la matematica: ")
    nota_engleza = input("Nota la engleza: ")
    media = float(input("Media generala: "))
    elev = {"nume": nume, "prenume": prenume, "medie": media, "nota romana": nota_romana, "nota matematica": nota_matematica, "nota engleza": nota_engleza}
    lista_elevi.append(elev)
    print(f"Elevul {nume} a fost adaugat.")

# def afiseaza_elevi(lista_elevi):
#     if not lista_elevi:
#         print("Nu exista elevi inregistrati.")
#         return print("--- LISTA ELEVI ---")
#     for i, elev in enumerate(lista_elevi, 1):
#         print(f"{i}. {elev['nume']} | Clasa: {elev['clasa']} | Medie: {elev['medie']}")


elevi = []

while True:

    afiseaza_meniu()
    optiune = input("Alegeti o optiune: ")

    if optiune == "1":
        adauga_elev(elevi)
        print(elevi)
         
        # elif optiune == "2":
        #     if not elevi:
        #         print("\nNu există elevi înregistrați.")
        #     else:
        #         print("\nLista Elevi:")
        #         for i, elev in enumerate(elevi, 1):
        #             print(f"{i}. Nume: {elev['nume']} | Clasa: {elev['clasa']} | Medie: {elev['medie']}")

        # elif optiune == "3":
        #     cautat = input("Introduceți numele elevului căutat: ")
        #     gasit = False
        #     for elev in elevi:
        #         if elev['nume'].lower() == cautat.lower():
        #             print(f"Elev găsit: Clasa {elev['clasa']}, Medie {elev['medie']}")
        #             gasit = True
        #             break
        #     if not gasit:
        #         print("Elevul nu a fost găsit.")

        # elif optiune == "4":
        #     de_sters = input("Numele elevului de șters: ")
        #     initial_len = len(elevi)
        #     elevi = [e for e in elevi if e['nume'].lower() != de_sters.lower()]
            
        #     if len(elevi) < initial_len:
        #         print(f"Elevul {de_sters} a fost eliminat.")
        #     else:
        #         print("Elevul nu a fost găsit.")

        # elif optiune == "5":
        #     print("Programul se închide. La revedere!")
        #     break
        # else:
        #     print("Opțiune invalidă. Încercați din nou.")
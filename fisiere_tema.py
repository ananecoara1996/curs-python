#Exercitiul 1
#Sa se scrie un program care citeste de la tastatura informatii despre persoane (nume, prenume, varsta, oras)
#si le salveaza intr-un fisier text numit "persoana.txt" in formatul: "Nume Prenume, Varsta, Oras".


# def salveaza_persoane():
#     with open("persoana.txt", "a") as fisier:
        
#         while True:

#             print("Introduceti datele persoanei:")
            
#             nume = input("Nume: ")
#             if nume == 'stop':
#                 break
#             prenume = input("Prenume: ")
#             varsta = input("Varsta: ")
#             oras = input("Oras: ")
            
#             linie = f"{nume} {prenume}, {varsta}, {oras}\n"
            
#             fisier.write(linie)
#             print("Datele au fost salvate")


#Exercitiul 2
#Sa se scrie un program care citeste un fisier text numit "date.txt" si afiseaza numarul de linii, cuvinte si caractere din fisier.        

def fisier_date():
    try:
        with open("date.txt", "r") as fisier:

            continut = fisier.read()
        
            nr_caractere = len(continut)
            nr_cuvinte = len(continut.split())
            nr_linii = len(continut.splitlines())
            print(f"Date despre fisier:")
            print(f"Linii: {nr_linii}")
            print(f"Cuvinte: {nr_cuvinte}")
            print(f"Caractere: {nr_caractere}")
    except FileNotFoundError:
        print("Fisierul date.txt nu a fost gasit.")        


#Exercitiul 3
#Se da urmatorul fisier "produse.txt" care contine informatii despre produse.
#Sa se scrie un program care citeste informatiile despre produse din fisierul "produse.txt"
#si calculeaza pretul total al stocului pentru fiecare produs.

# def fisier_produse():
#     with open ("produse.txt", "r") as fisier:

#         continut = fisier.read()


#Exercitiul 4
#Se da un fisier de logging "log.txt" care contine date referitor la evenimentele dintr-un sistem:
#Sa se scrie un program care citeste fisierul "log.txt" si afiseaza numarul de evenimente de fiecare tip (INFO, WARNING, ERROR)
#si afiseaza ora si evenimentul de tip ERROR care a avut loc cel mai recent.

def proceseaza_loguri():
    contor_evenimente = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    ultima_eroare_ora = None
    ultima_eroare_mesaj = None

    with open("log.txt", 'r') as fisier:
        for linie in fisier:
            linie = linie.strip()
            if not linie:
                continue
                
            # Incrementăm numărul de evenimente în funcție de tip
            for tip in contor_evenimente.keys():
                if tip in linie:
                    contor_evenimente[tip] += 1
                        
                    # Daca este ERROR, actualizam ultima eroare gasita
                    if tip == "ERROR":
                        # Presupunem formatul: "YYYY-MM-DD HH:MM:SS ERROR Mesaj"
                        parti = linie.split(' ', 2)
                        if len(parti) >= 3:
                            ultima_eroare_ora = parti[1]
                            ultima_eroare_mesaj = parti[2]

        # Afișare rezultate
        print("Statistici evenimente:")
        for tip, count in contor_evenimente.items():
            print(f"{tip}: {count}")
            
        if ultima_eroare_ora:
            print(f"\nCea mai recenta eroare:")
            print(f"Ora: {ultima_eroare_ora} | Mesaj: {ultima_eroare_mesaj}")
        else:
            print("\nNu au fost gasite erori in fisier.")



#Exercitiul 5
#Se da un fisier de logging "login.txt" care contine date referitor la incercarile de autentificare ale utilizatorilor:
#Sa se scrie un program care citeste fisierul "login.txt" si salveaza in fisierul "user_attempts.txt" numarul de incercari de autentificare
#pentru fiecare utilizator si ora si data ultimei incercari de autentificare reusite in formatul:
   # <user> | <numar_incercari> | <ultima_data_ora_reusita>


# with open("login.txt", 'r') as file:
#         for line in file:
#             # Presupunem formatul: DataOra | Utilizator | Status
#             parts = [p.strip() for p in line.split('|')]
#             if len(parts) < 3:
#                 continue
            
#             data_ora, user, status = parts[0], parts[1], parts[2]

#             # Initializam utilizatorul in dictionar daca nu exista
#             if user not in user_data:
#                 user_data[user] = {'total': 0, 'ultima_reusita': 'N/A'}

#             # Incrementam numarul total de incercari
#             user_data[user]['total'] += 1

#             # Actualizam data ultimei autentificari reusite
#             if status.lower() == 'succes':
#                 user_data[user]['ultima_reusita'] = data_ora

#     # Scriem rezultatele in user_attempts.txt
#     with open("user_attempts.txt", 'w') as file:
#         for user, data in user_data.items():
#             line = f"# {user} | {data['total']} | {data['ultima_reusita']}\n"
#             file.write(line)
    
#     print(f"Raportul a fost salvat in {}")








if __name__ == "__main__":
    # salveaza_persoane()
    # print("\nProgramul s-a incheiat. Verificati fisierul 'persoana.txt'.")
    fisier_date()
    proceseaza_loguri()
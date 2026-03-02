''' Sa se creeze un script care sa accepte argumente din linia de comanda pentru nume, prenume, varsta, folosind modulul argparse. Scriptul sa afiseze numele complet al persoanei si varsta in urmatorul format:
    Nume: [nume]
    Prenume: [prenume]
    Varsta: [varsta] ani
'''


import argparse

def main():
    
    my_parser = argparse.ArgumentParser(description="Script pentru afisarea datelor: ")

    my_parser.add_argument("--nume", type=str, help="Numele persoanei")
    my_parser.add_argument("--prenume", type=str, help="Prenumele persoanei")
    my_parser.add_argument("--varsta", type=int, help="Varsta persoanei")

    args = my_parser.parse_args()

    print(f"Nume: [{args.nume}]")
    print(f"Prenume: [{args.prenume}]")
    print(f"Varsta: [{args.varsta}] ani")

if __name__ == "__main__":
    main()

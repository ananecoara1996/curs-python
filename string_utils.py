#Sa se creeze un modul numit "string_utils" care sa contina functii pentru manipularea stringurilor: inversarea unui string, verificarea daca un string este palindrom.
#Sa se scrie un script care sa importe modulul si sa se execute fiecare functie asupra unui string primit ca si argument din linia de comanda.

def inversare(text):
    return text[::-1]
    

def este_palindrom(text):
    text_nou = "".join(text.split()).lower()
    return text_nou == text_nou[::-1]


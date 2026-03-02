################################################################################################################################
##################DICTIONARE EXERCITII#########################

student = {
    'nume': 'Ana',
    'varsta': 25,
    'nota': 10
}

#1. Accesează o valoare specifică
print(f"Numele studentului este {student['nume']} are {student['varsta']} ani, iar nota este {student['nota']}.")

#2. Afișează doar valoarea asociată cheii "nota"
nota_student = student.get('nota')
print(f"Nota studentului este {nota_student}")

#3. Modifică o valoare

student['nota'] = 9
print(student)

nota_s = student.update({'nota': 11})
print(nota_s)
print(student)

#4. Adăugare și Modificare: Adaugă o nouă pereche cheie-valoare "oras": "Bucuresti" și modifică "nota" existentă la o valoare mai mare.

student['oras'] = 'Bucuresti'
student['nota'] = 12
print(student)

#5. Ștergere: Elimină cheia "varsta" din dicționar folosind metoda pop() sau cuvântul cheie del.

student.pop('varsta')
print(student)

#6. Parcurgere: Scrie un program care afișează separat toate cheile și apoi toate valorile dintr-un dicționar dat.

chei_dict = list(student)
print(chei_dict)

valori_dict = list(student.values())
print(valori_dict)


#7. Verificare existență: Verifică dacă o anumită cheie (de ex. "email") există în dicționar folosind operatorul in

if 'email' in student:
    print("Cuvantul exista")
else:
    print("Cuvantul nu exista")

#8. Frecvența caracterelor: Scrie o funcție care primește un șir de caractere (de ex. "programare") și returnează un dicționar cu numărul de apariții al fiecărei litere

text = "Frecvența caracterelor: Scrie o funcție care primește un șir de caractere și returnează un dicționar cu numărul de apariții al fiecărei litere"

frecventa = {}

for caracter in text:
    if caracter.isalpha():
        if caracter in frecventa:
            frecventa[caracter] +=1
        else:
            frecventa[caracter] = 1

print(frecventa)


#Exemplu nou de dictionar

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

#1. Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary and print the updated dictionary.
my_dict['profession'] ='Doctor'
print(my_dict)

#2. Modify Value: Change the value of the age key to 40 in the dictionary and print the updated dictionary.
my_dict['age'] = 40
print(f"Updated dictionary after modification: {my_dict}")

#3. Access Key: Print the value associated with the city key.
print('City:', my_dict.get('city'))

#4. Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
my_dict.pop('profession')
print(f"Updated dictionary after modification: {my_dict}")

#5. Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
for key, value in my_dict.items():
    print(f"{key}: {value}")


#6. Check if Key Exists in the dictionary

cheia_de_verificat = 'nume'
if cheia_de_verificat in my_dict:
    print("Cheia exista")
else:
    print("Cheia nu exista")


#Exemplu nou de dictionar

person1 = {'name': 'Jessa', 'country': 'USA', 'telephone': 1178}
person2 = {'Kelly': 68, 'Harry': 50, 'Olivia': 66}

# Get the list of keys and check if 'country' key is present
key_name = 'country'
if key_name in person1.keys():
    print("country name is", person1[key_name])
else:
    print("Key not found")

#Join two dictionary
#copy second dictionary into first dictionary
person1.update(person2)
print(person1)


#Exemplu nou de dictionar

# address dictionary to store person address
address = {"state": "Texas", 'city': 'Houston'}

# dictionary to store person details with address as a nested dictionary
person = {'name': 'Jessa', 'company': 'Google', 'address': address}

# Display dictionary
print("person:", person)

# Get nested dictionary key 'city'
print("City:", person['address']['city'])

for key, value in person.items():
    if key == 'address':
        print("Person Address:")
        for nested_key, nested_value in value.items():
            print(nested_key, ':', nested_value)


#Exemplu nou de dictionar

dict1 = {'c': 45, 'b': 95, 'a': 35}

# sorting dictionary by keys
print(sorted(dict1.items()))

# sort dict keys
print(sorted(dict1))

# sort dictionary values
print(sorted(dict1.values()))

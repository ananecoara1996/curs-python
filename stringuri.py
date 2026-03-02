# var = 'Marius'

# print(var[0])
# print(var[1])
# print(var[2])
# print(var[3])
# print(var[4])
# print(var[5])
# print()
# print(var[-1])
# print(var[-2])
# print(var[-3])
# print(var[-4])
# print(var[-5])
# print(var[-6])


# fructe = 'Bananele si perele sunt fructe'
# print(fructe[-6::1])
# print(fructe[0:8:8])

# str1 = "Ana"
# str2 = "are "
# str3 = "mare "
# propozitie = str1 + " " + str2 + ' ' + str3
# print(propozitie)

# ana_multiplicata = str1 * 3
# print(ana_multiplicata)

# my_str = "Arad Arad 30"

# lungime_str = len(my_str)
# print(lungime_str)

# print(my_str[10:12])

# my_str = my_str.lower()
# print(my_str)

# print(my_str.upper())
# print(my_str.lower())

# print(my_str)

# print(my_str.capitalize())

# my_str = 'Arad Arad 30'
# my_str.replace('Arad', 'Timisoara')
# print(my_str.replace('Arad', 'Timisoara'))
# print(my_str)

# print(my_str)
# print(my_str.count('Arad'))

# my_str.lower().count('a')
# print(my_str.lower().count('a'))

# print(type(my_str.lower().count('a')))

# nume = input('Introduceti nume:')
# varsta = input('Introduceti varsta:')
# var1 = 'Salut, {}! {} are {} ani'.format(nume, nume, varsta)
# var2 = f'Salut, {nume}! {nume} are {varsta} ani'
# print(var1)
# print(var2)

# var = 'Daniel Andrei Ioan'
# print(var)
# print(var.rstrip())


# my_list = var.split()
# print(my_list)  
# print(var.split('n'))

# new_string = ' '.join(my_list)  
# print(new_string)

# print(var.startswith('D'))
# print(var.endswith('Ioa'))

# print('Daniel'.isalpha())
# print('123'.isdigit())

# poezie = "'Ana' are \tmulte mere,\nIonel vine \"si\" cere"
# print(poezie)



text = 'Afara este frig, dar o sa fie si vreme buna! '
text_aparitie = text.count('a')
print(f"Litera 'a' apare de fix {text_aparitie} ori")

lungime_text = len(text)
print(lungime_text)

print(text.count('a', 10, 45))


day = 8
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case 8:
    print("Check again!")


numar = 1
while numar < 6:
  print(numar)
  numar += 1

i = 1
while i < 6:
  print(i)
  if (i == 4):
    break
  i += 1


  #Calculul Ariei: Scrie o funcție care primește lungimea laturii unui pătrat și returnează aria acestuia.

  def calculeaza_aria(latura):
    aria = latura ** 2
    return aria
  
rezultat = calculeaza_aria(5)

print(f"Aria patratului este: {rezultat}")


#Convertor de Temperatură: Creează două funcții: una care transformă gradele Celsius în Fahrenheit și alta invers.

#Formula: temp_Fahrenheit = (grade_Celsius * float(1.8)) + 32


def temperatura_Celsius(grade_Celsius):
    temp_Fahrenheit = (grade_Celsius * float(1.8)) + 32
    return temp_Fahrenheit


rezultat_Fahrenheit = temperatura_Celsius(20)
print(f"Temperatura in Fahrenheit este: {rezultat_Fahrenheit}")

def temperatura_Fahrenheit(grade_Fahrenheit):
  temp_Celsius = float((grade_Fahrenheit - 32) / 1.8)
  return temp_Celsius 

rezultat_Celsius = temperatura_Fahrenheit(68)
print(f"Temperatura in grade Celsius este: {rezultat_Celsius}")
x = 3 
y = 3.5
z= "20"

x = int(3)
print (x)

y = int(3.5)
print (y)

z = int("20")
print (z)

b = "Hello, World!"
print(b[2:5])  #Get the characters from position 2 to position 5 (not included)

c = "Afara este frig"
print (c[:6]) #Get the characters from the start to position 6 (not included)


#The upper() method returns the string in upper case:
a = "Mai sunt cateva zile pana la Craciun"
print (a.upper())

#The lower() method returns the string in lower case:
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end:
print(a.strip())

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

if a == b:
  print("the both numbers are equal")
else:
  print ("the numbers are different")

#liste 

fructe = ["mar", "portocala", "gutuie"]
print(fructe)

print(len(fructe))  #To determine how many items a list has, use the len() function

numere = [1, 7, 8, 5, 14]
print(numere)  

print(numere[2])
print(numere[-1])
print(numere[:3]) # afiseaza de la primul numar pana la pozitia 3, dar fara acesta
print(numere[2:]) # afiseaza de la pozitia 2 pna la final
print(type(numere))
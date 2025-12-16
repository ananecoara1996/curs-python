x = int (input ("Valoarea lui x:"))
y = int (input ("Valoarea lui y:"))

print(x, y)

print (x+y, x-y, x*y, x/y, x%y)


suma = (x+y)+(x-y)+(x/y)
print(round(suma, 2 ))

diferenta = (x-y)-(x+y)
print(diferenta)


x = 10 
y = input("y")
print (x + int(y))


var1 = 5
var2 = 7
print (var1 < var2)
print (var1 == var2)
print (var1 != var2)
print (var1 >= var2)
print (var1 > var2)

a = 5
b = 7 
c = 9 

a < b and a < c
print (a < b and a < c) # True
print (a < b and a > c) # False
print (a < b or a < c)  # True
print (a < b and not a > c)  # True

print ('a' in 'ana are mere')  # True


a = None 
b = None

print (a is b)


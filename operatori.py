'''
Operatorii aritmetici:
    +    Adunare              ex: a + b
    -    Scadere              ex: a - b
    *    Inmultire            ex: a * b
    /    Impartire            ex: a / b
    //   Impartire intreaga   ex: a // b
    %    Restul impartirii    ex: a % b
    **   Ridicare la putere   ex: a ** b
'''

x = int (input ("Valoarea lui x:"))
y = int (input ("Valoarea lui y:"))

print(x, y)

print (x+y, x-y, x*y, x/y, x%y)


suma = (x+y)+(x-y)+(x/y)
print(round(suma, 2 ))

'''
funtia round() - rotunjeste la cate zecimale ii specifici
    ex: x = 3.12345678
        x = round(x, 3) -> x = 3.123
'''


diferenta = (x-y)-(x+y)
print(diferenta)

'''
Operatorii de atribuire:
    =     Asignare                           ex: a = 5
    +=    Adunare si asignare                ex: a += 2   (echivalent cu a = a + 2)
    -=    Scadere si asignare                ex: a -= 2
    *=    Inmultire si asignare              ex: a *= 2
    /=    Impartire si asignare              ex: a /= 2
    //=   Impartire intreaga si asignare     ex: a //= 2
    %=    Rest si asignare                   ex: a %= 2
    **=   Putere si asignare                 ex: a **= 2
'''

x = 10 
y = input("y: ")
x += int (y) # x = x + y
print(x)


z = input("z: ")
x += int(z) # x = x + z
print(x)

a = input("a: ")
x **= int(a)
print(x)


'''
Operatorii de comparatie:
    ==    Egalitate              ex: a == b
    !=    Diferit                ex: a != b
    >     Mai mare               ex: a > b
    <     Mai mic                ex: a < b
    >=    Mai mare sau egal      ex: a >= b
    <=    Mai mic sau egal       ex: a <= b
'''
var1 = 5
var2 = 7
print (var1 < var2)
print (var1 == var2)
print (var1 != var2)
print (var1 >= var2)
print (var1 > var2)

'''
Operatorii logici:
    and    Si logic              ex: a and b (ambele trebuie sa fie adevarate)
    or     Sau logic             ex: a or b  (cel putin una trebuie sa fie adevarata)
    not    Negatie logica        ex: not a   (neaga valoarea curenta)
'''

a = 5
b = 7 
c = 9 

a < b and a < c
print (a < b and a < c) # True
print (a < b and a > c) # False
print (a < b or a < c)  # True
print (a < b and not a > c)  # True

'''
Operatorii de apartenenta:
    in      ex: 'a' in 'ana'
    not in  ex: 5 not in [1,2,3]
'''

print ('a' in 'ana are mere')  # True
print('a' in 'ana')  
print('an' in 'ana')
print('10' in '101') #True
print(10 not in [7,8,9,'10']) #True
print(1 in [1,2,3,4,5]) #True 

'''
Operatorii de identitate:
    is      ex: a is b
    is not  ex: a is not b
'''

a = None 
b = None

print (a is b)
print (a is not b)  # False         


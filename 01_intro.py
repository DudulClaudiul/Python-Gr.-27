

# Python este un limbaj interpretat.

print("Hello World.")
print(-4)

# Variabile:

number1 = 10
number2 = 30

var1 = "Hello"
var2 = "World"

cat = "Cat"

# cat 1 = "Cat"
# CTRL + /
# CTRL + < sau >

var3 = 100
print(var3)

var4 = number1 + var3
print(var4)

var4 = 3000
print(var4)

var4 = "Panzer 3000"
print(var4)

# tipuri de date.

# 10  -> int int -> integer -> numar intreg
# -5  -> int
# 4.5 -> float
# -0  -> int
# 0  ,  -0

# "hello" -> str
# True sau False -> bool -> booleans -> boolene

var5 = 4.5
var6 = -0
var7 = "hello"
#       h -> 0  e -> 1  l -> 2 ..... index
print(var7[2])

var8 = True
print(var8 == True)
# == -> operator binar de comparare

var9 = True
var10 = 2

# == in cazul asta nu verifica si identitatea acelor variabile
print(var9 == var10)

# print este o functie
# alte functii: max, min, pow, range

var11 = type(var10)
print(var11)

# liste
print("Liste:")

varlist1 = []
print(varlist1)

varlist2 = [10, 30, 45, 99, -1, 0, -99, 254234563457, "hello", "a", True, 0.5, type(0)]
print(varlist2)

varlist3 = [100, 200, [-1, -3, -10, [-99, -888, 0]], [True], var3, var10]
print(varlist3)

varlist4 = [40, 50, 100, 3, -10, 0]
#            0   1    2  3    4  5
#           -6  -5   -4 -3   -2 -1

print(varlist4[-6])

print(varlist4[4])
print(varlist4[0])

list4_length = len(varlist4)
print(list4_length)
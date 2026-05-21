#variabile prin referinta

lista1 = [10, 30, 5, 7, 100, -5]
lista2 = lista1
# lista2 = locul din memoria calculatorului (0x986123543)

print(lista1)
lista2.append(88)
print(lista1)

#liste, seturi, dict

# variabile prin valoare

var1 = 100
var2 = var1

var2 = 77

print(var1)

#structuri de date primitve: int, float, bool, string
# structuri complexe: liste, seturi, dict, tuplu

lista3 = [9, 10, 100, 5, 50, 4]
#         0   1   2   3   4  5

#slicing, splicing
# list[start:stop:step]
#      sunt indecsi

# lista3[0:2]
# print(lista3[0:3:2])
# print(lista3[:])
# print(lista3[::])
# print(lista3[::-1]) #inverseaza lista
# print(lista3[3:])

lista4 = lista3[:]
lista4.append(89)
print(lista3)

lista5 = [7, 10]
lista5.append(99)
lista5.extend([100, 101, 102])
lista5 = lista5 + [103, 104, 105]
lista5 += [106, 107, 108, 109]
lista5.remove(101) # sterge doar primul numar 101 intalnit in lista

print(lista5.index(100))

lista5.sort() #sorteaza lista
lista6 = sorted(lista5) #se foloseste sa creezi o lista noua sortat fara a afect lista initiala

#matrici

matrice1 = [
    [3, 4, 10],
    [7, 8, 11],
    [0, 3, 99]
]

print(matrice1)
print(matrice1[2][0])

# list comprehension

lista7 = [3, 4, 10]
lista8 = [x ** 3 for x in lista7]
print(lista8)

lista9 = [x ** 3 for x in lista7 if x % 2 == 0]
print(lista9)

#strings - se comporta ca o lista imutabila

alfabet = "abcdefghijklmn"
print(alfabet[::-1])

prop1 = "    Gabi a inceput sa invete Python. El, un student, urmeaza acest curs, cursul de Python.    "
print(prop1.split(","))
print(prop1.strip().lower().split(".").pop())

#formatare

name = "Alex"
age = 25
profession = "Programmer"

#nou f-string
print(f"Hello! My name is {name}, I'm {age} years old, and I'm a {profession}.")

#pe vechi - format

print("Hello! My name is {}. I'm {} and I'm a {}.".format(name, age, profession))





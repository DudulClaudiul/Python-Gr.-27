
# Liste

list1 = [4, 5, 10, 20, 30, 100, 500, 999, 1000]
#        0  1   2   3   4    5    6    7     8
print(list1[0])
print(list1[-1])

index = len(list1) // 2
print(list1[index])

list2 = [0, 1, 2, 50, 100, 100, 100, 100, 2, 2, 2, 9, 10, 99]
print(list2)
# putem schimba un element din lista folosind [] si punand indexul elementului in ele.
list2[3] = 100
print(list2)

# Dictionare:

# unordered.
persoana = {
    "key": "valoare",
    "nume": "Alex",
    "inaltime": "1.85m",
    "varsta": 27,
    "cetatean_roman": True,
    "bolnav": False,
    "greutate": 75.7,
    "inaltime": "2m",
}

# scurtaturi de copy/paste:
# CTRL+C , CTRL+V

print(persoana)
# fast lookup
print(persoana["key"])
print(persoana["varsta"])
persoana["inaltime"] = "3m"
persoana["CNP"] = "29382347857283523"

# cel mai intalnit tip de date.
# bool.

# string.
# Cont bancar:
# IBAN: 948394385834958BCR

#     "hello"
#      104 101 108 108 111
#      0101010010 101010101010 101010010101 1010100101

# seturi:
# cutie de bomboane, toate diferite.

# curly braces
# squigly brackets

elemset = {3, 6, 10, 9, 8, 100, 3}
print(elemset)

list2 = [0, 1, 2, 50, 100, 100, 100, 100, 2, 2, 2, 9, 10, 99]



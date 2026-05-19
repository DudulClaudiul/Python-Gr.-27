#git test stuff for git

print("Hello World")

print("this is a change")
print("this is another one")

#if-uri

nr_pare = []
nr_impare = []

lista2 = [6, 7, 10, 90, 100, 33, 88, 5, 13, 0]
for nr in lista2:
    if nr % 2 == 0:
        nr_pare.append(nr)
    else:
        nr_impare.append(nr)

print("Nr. pare: ", nr_pare)
print("Nr. impare: ", nr_impare)

# expresii logice

for nr in lista2:
    if nr % 2 == 0 and nr % 5 == 0:
        print("Nr urmator e si par, si multiplu de 5: ")
        print(nr)
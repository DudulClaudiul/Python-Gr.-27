
#functii
#definire functie
def greet():
    print("Hello world!")
    print("this is mama ta")

#apelare de functie

greet()

#a si b sunt parametrii

def add(a, b):
    return a + b

print(add(5, 10))

print(add(15, 18))
print(add(567, 862))


def mul(a, b):
    return a * b

var1 = mul(5,15)
add(var1, 35)

#parametrul se numeste acel "a". Argument este valoarea ce o dam acelui "a". Ex: 5

# creati sub care scade a-b, div care imparte a/b, si pow care ridica a**b

def sub(a, b):
    return a - b

def div(a,b):
    return a / b

def pow(a,b):
    return a ** b

# 6 - 4 * 10

rezultat = sub(6, mul(4,10))
print(rezultat)

5 + 4 * 8 ** 2

rezultat1 = add(5, mul(4, pow(8, 2)))
print(rezultat1)

#return implicit, None
def speak(word="woof!"):
    print(word)

speak()
speak("miau!")

def drive(car_model, max_speed=130):
    print(f"{car_model} is running at the max speed of {max_speed}")

drive("Audi")
drive("Mazda", "red")

#typed function

def modulo(a: int, b: int) -> int:
    """
    Returns the remainder of the division between a and b.
    :param a: the number to be divided
    :param b: the number that does the division
    :return: reminder
    """
    return a % b

# RST / Sphinx style docs ^

print(modulo(13, 5))


nr = [10, 11, 21, 5, -1, 20, 3]

def even_numbers(list1):
    #iteram prin lista. folosim modulo
    res = []
    for n in list1:
        if n % 2 == 0:
            print(f"am gasit numar par: {n}")
            res.append(n)
    return res

result = even_numbers(nr)
print(result)

nr2 = [7, 22, 4, 5, -2, 8, 10]
result2 = even_numbers(nr2)
print(result2)

#Tema

# "ERR-Value Error-ER:10"
# "INF-Program launch Info-CD:5"
# "WRN-Low memory-WR:11"

var2 = ["ERR-Value Error-ER:10", "INF-Program launch Info-CD:5", "WRN-Low memory-WR:11"]
for s in var2:
    print(s.split("-")[0])
    print(f"Mesaj: {s.split('-')[1]}")
    print("Mesaj: ", s.split('-')[1])
    print(s.split("-")[1])
    # s -> string :::: .split("-") -> list :::: [2] -> elem din lista dupa index ::::
    # elem este string, deci s.split("-")[2] -> string :::: .split(":") -> list ::::
    # acea_lista[1] -> al doilea element, care este numarul de cod ce ne intereseaza.
    print(s.split("-")[2].split(":")[1])

# [ERROR] - se foloseste if
# Mesaj: Value Error
# Cod: 10
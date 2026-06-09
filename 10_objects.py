from pprint import pprint
var1 = 10

var1 = 30 + 20
print(var1)
print(type(var1))

var2 = True

obj1 = {
    "name": "Ion"
}

obj1["age"] = 32
print(obj1)

obj1["cnp"] = 19023848753

var3 = True

obj1["cetatenie_romana"] = var3

pprint(obj1)

list1 = []
list1.append(10)

def speak(param1 = "Hello!"):
    print(param1)

# creez o functie noua care se poate apela din obj1
# obj1.speak = speak
# aceasta functie poate acum sa fie apelata din obj1
# obj1["speak"]() -> astfel se apelaza acea functie
obj1["speak"] = speak
obj1["speak"]("Hello this is Ionut!")

print(obj1)

obj1["note"] = [7, 10, 8]
pprint(obj1)

# Task: Creaza un obiect similar cu obj1, cu proprietati la fel, dar valori diferite. De ex, sa aiba age=40

# obj2 = obj1.copy()
# obj2["name"] = "George"
#
# pprint(obj2)

obj2 = {
    "age": 40,
    "name": "George",
    "cnp": 128393829487234
}
# .......

# definim o functie care poate crea oricate obiecte, cu o structura fixa, cum sunt obiectele de mai sus.
# acestui nou obiect ii dam si acea functie speak
def obj_constructor(name, age, cnp, cetatenie_romana):
    new_object = {"name": name, "age": age, "cnp": cnp, "cetatenie_romana": cetatenie_romana}
    new_object["speak"] = speak
    return new_object


obj3 = obj_constructor("Vlad", 34, 19293949134, True)
print(obj3)
obj3["speak"]("Hello this is Vlad!")

# param_obj poate fi orice variabila din exteriorul functiei, si daca are acea proprietate "age", se mareste cu 1 acel age
def do_work(param_obj):
    print("Doing some work.....")
    param_obj["age"] = param_obj["age"] + 1
    return 42


obj3["do_work"] = do_work
# apeland do_work(obj3), fiindca am pus obj3 in parametrii, atunci acelui obj3 i se modifica "age"-ul
obj3["do_work"](obj3)

obj3["do_work"](obj3)

obj4 = {"age": 21}
obj4["do_work"] = do_work
# si aici la fel, do_work mareste "age"-ul lui obj4 cu 1.
obj4["do_work"](obj4)

pprint(obj3)


# aceasta functie poate modifica variabile si obiecte din exteriorul ei, daca primeste acel obiect ca parametru.
def grow(param1):
    param1["size"] = param1["size"] + 1


var4 = {"size": 5}

grow(var4)
grow(var4)
grow(var4)
grow(var4)

print(var4)

#obj_param este referinta in memorie a acelui dictionar
def set_hobby(obj_param, key, value):
    obj_param[key] = value

obj5 = {"name": "John Wick"}

#functia altereaza obj5 in cazul asta, chiar daca nu avem un return

set_hobby(obj5, "hobby", "killing")
print(obj5)

#exemplu cu liste

def add_person(param_list, person):
    if len(person) > 2:
        param_list.append(person)
        param_list.sort()
    else:
        print("Name needs to be 3 characters or longer!")

lista_persoane = ["John Wick", "Winston", "Daisy"]

add_person(lista_persoane, "Cassian")
add_person(lista_persoane, "TN")
add_person(lista_persoane, "x")
add_person(lista_persoane, "Josef")

print(lista_persoane)

lista_persoane2 = []

add_person(lista_persoane2, "Ion")
add_person(lista_persoane2, "Marius")
add_person(lista_persoane2, "Vasile")
add_person(lista_persoane2, "Costica")

#exemplu de functie care manipuleaza mai multe tipuri de date:

def add_to_db(database, village, people):
    database[village] = people.copy()

db = {}

add_to_db(db, "Poiebari", lista_persoane)
add_to_db(db, "Gadinti", lista_persoane2)

#cand facem append la lista_persoane2 schimbarea se reflecta sin in dictionarul db
#fiindca dictionarul db tine minte o referinta spre aceasta lista
#daca adaugam people.copy in add_to_db(), nu mai avem acel bug
lista_persoane2.append("Ghita")

pprint(db)

var5 = [10]
#var5 tine minte referinta acelei liste, in memorie
#cand scriu var6 = var5, acum si var6 tine minte acea referinta spre aceeasi lista

var6 = var5
var6.append(20)

print(var5)
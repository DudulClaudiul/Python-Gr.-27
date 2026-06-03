#Creati o variabila care contine o lista de siruri de caractere:
#"ERR-Value Error-ER:10"
#"INF-Program launch Info-CD:5"
#"WRN-Low memory-WR:11"

#Si alta variabila, cu alte siruri de caractere:
#"INF-Program exit-CD:14"
#"WRN-Low disk space-WR:99"
#"WRN-Bandwith reached-WR:87"

#Treceti prin toate sirurile de caractere, extrageti valorile de la ERR, INF, WRN, si creati urmatorul text formatat, din sirurile de caracter date, de exemplu:

#Rezultatul ar trebui sa arate astfel:
#[ERROR]
#Mesaj: Value Error
#Cod: 10

#[INFO]
#Mesaj: Program launch Info
#Cod: 5

#[WARNING]
#Mesaj: Low memory
#Cod: 11

#Faceti asta pentru amandoua variabile, care contin acele siruri de caracter.

var1 = ["ERR-Value Error-ER:10", "INF-Program launch Info-CD:5", "WRN-Low memory-WR:11"]
var2 = ["INF-Program exit-CD:14", "WRN-Low disk space-WR:99", "WRN-Bandwith reached-WR:87"]

for s in var1 + var2:
    parts = s.split("-")
    types = parts[0]
    message = parts[1]
    code = parts[2].split(":")[1]

    if types == "ERR":
        formated_type = "[ERROR]"
    elif types == "INF":
        formated_type = "[INFO]"
    elif types == "WRN":
        formated_type = "[WARNING]"

    print(f"{formated_type} Mesaj: {message} Code: {code}")

#refactorizare


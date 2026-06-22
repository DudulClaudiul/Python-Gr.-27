import json

def incarca_categorii():
    """
    Citeste categoriile din fisierul categorii.txt si le returneaza ca lista.
    Daca fisierul nu exista (prima rulare a programului), returneaza lista vida.
    """
    categorii = []
    try:
        with open("categorii.txt", "r") as fisier:
            for linie in fisier:
                categorie = linie.strip()  # elimina \n si spatiile de la capete
                if categorie != "":        # ignoram liniile goale
                    categorii.append(categorie)
    except FileNotFoundError:
        # fisierul nu exista inca -> nu e o eroare reala, doar nu avem categorii
        categorii = []

    return categorii


def adauga_categorie(categorii):
    """
    Cere de la tastatura o categorie noua.
    Daca exista deja in lista (comparand fara a tine cont de majuscule),
    afiseaza un mesaj de eroare si nu o adauga.
    Daca nu exista, o adauga in lista.
    """
    categorie = input("Introduceti noua categorie: ").strip()

    categorii_lower = []
    for c in categorii:
        categorii_lower.append(c.lower())

    if categorie.lower() in categorii_lower:
        print(f"Eroare: categoria '{categorie}' exista deja!")
    else:
        categorii.append(categorie)
        print(f"Categoria '{categorie}' a fost adaugata cu succes.")


def salveaza_categorii(categorii):
    """
    Deschide fisierul in modul write si scrie categoriile pe o linie noua
    """
    with open("categorii.txt", "w") as fisier:
        for linie in categorii:
            fisier.write(linie + "\n")


def incarca_taskuri():
    """
    Citeste taskurile din fisierul taskuri.json si le returneaza ca lista de dictionare.
    Daca fisierul nu exista (prima rulare a programului), returneaza lista vida.
    """
    try:
        with open("taskuri.json", "r") as fisier:
            taskuri = json.load(fisier)
            return taskuri
    except FileNotFoundError:
        return []


def salveaza_taskuri(taskuri):
    """
    Deschide fisierul in modul write si scrie categoriile in fisier.
    """
    with open("taskuri.json", "w") as fisier:
        json.dump(taskuri, fisier, indent=4)


def adauga_task(taskuri, categorii):
    """
    Cere de la tastatura un task nou, impreuna cu data limita, persoana
    responsabila si categoria din care face parte.
    Daca textul taskului exista deja (comparand fara a tine cont de
    majuscule), afiseaza un mesaj de eroare si nu il adauga.
    Daca categoria introdusa nu exista in lista de categorii, afiseaza
    un mesaj de eroare si nu il adauga.
    Daca toate verificarile trec, construieste un dictionar cu cele 4
    campuri si il adauga in lista de taskuri.
    """
    task_text = input("Introduceti task: ").strip()

    task_lower = []
    for t in taskuri:
        task_lower.append(t["task"].lower())

    if task_text.lower() in task_lower:
        print(f"Eroare: Taskul '{task_text}' exista deja!")
    else:
        data = input("Introduceti data limita (ex: 22.01.2022 21:30): ").strip()
        persoana = input("Introduceti persoana responsabila: ").strip()
        categorie = input("Introduceti categoria: ").strip()

        categorii_lower = []
        for c in categorii:
            categorii_lower.append(c.lower())

        if categorie.lower() not in categorii_lower:
            print(f"Eroare: categoria '{categorie}' nu exista!")
        else:
            task_nou = {"task": task_text, "data": data, "persoana": persoana, "categorie": categorie}
            taskuri.append(task_nou)
            print(f"Taskul '{task_text}' a fost adaugat cu succes.")


def afiseaza_taskuri(taskuri):
    """
    Afiseaza pe ecran lista de taskuri primita, fara a o modifica sau sorta.
    Fiecare task este numerotat de la 1, ca utilizatorul sa aiba un
    identificator unic pe rand pentru operatiile de editare/stergere.
    """
    for index, task in enumerate(taskuri):
        print(f"{index + 1}. {task['task']}, {task['data']}, {task['persoana']}, {task['categorie']}")


def listeaza_taskuri(taskuri):
    """
    Sorteaza lista de taskuri in functie de categorie (ordine ascendenta)
    si afiseaza rezultatul, fara a modifica ordinea din lista originala.
    """
    taskuri_sortate = sorted(taskuri, key=lambda t: t["categorie"])
    afiseaza_taskuri(taskuri_sortate)


def sorteaza_taskuri(taskuri):
    """
    Afiseaza un meniu cu 8 criterii de sortare (ascendent/descendent pe
    task, data, persoana responsabila si categorie), citeste optiunea
    aleasa de utilizator, sorteaza lista de taskuri dupa criteriul ales
    si afiseaza rezultatul. Daca optiunea introdusa este invalida,
    afiseaza un mesaj de eroare si nu afiseaza nimic.
    """
    print("1. Sortare ascendenta task")
    print("2. Sortare descendenta task")
    print("3. sortare ascendentă data")
    print("4. sortare descendentă data")
    print("5. sortare ascendentă persoana responsabilă")
    print("6. sortare descendentă persoană responsabilă")
    print("7. sortare ascendentă categorie")
    print("8. sortare descendentă categorie")

    optiune = input("Alegeti o optiune: ").strip()

    if optiune == "1":
        taskuri_sortate = sorted(taskuri, key=lambda t: t["task"])
    elif optiune == "2":
        taskuri_sortate = sorted(taskuri, key=lambda t: t["task"], reverse=True)
    elif optiune == "3":
        taskuri_sortate = sorted(taskuri, key=lambda t: t["data"])
    elif optiune == "4":
        taskuri_sortate = sorted(taskuri, key=lambda t: t["data"], reverse=True)
    elif optiune == "5":
        taskuri_sortate = sorted(taskuri, key=lambda t: t["persoana"])
    elif optiune == "6":
        taskuri_sortate = sorted(taskuri, key=lambda t: t["persoana"], reverse=True)
    elif optiune == "7":
        taskuri_sortate = sorted(taskuri, key=lambda t: t["categorie"])
    elif optiune == "8":
        taskuri_sortate = sorted(taskuri, key=lambda t: t["categorie"], reverse=True)
    else:
        print("Optiune invalida!")
        return

    afiseaza_taskuri(taskuri_sortate)


def filtreaza_taskuri(taskuri):
    """
    Cere de la tastatura campul dupa care se face filtrarea (task, data,
    persoana responsabila sau categorie) si un text de cautare.
    Construieste o lista noua, doar cu taskurile la care campul ales
    contine textul introdus (comparare fara a tine cont de majuscule),
    si afiseaza lista rezultata. Lista originala nu este modificata.
    """
    print("1. Task")
    print("2. Data")
    print("3. Persoana")
    print("4. Categorie")

    camp = input("Alegeti campul de filtrare: ").strip()

    if camp == "1":
        cheie = "task"
    elif camp == "2":
        cheie = "data"
    elif camp == "3":
        cheie = "persoana"
    elif camp == "4":
        cheie = "categorie"
    else:
        print("Optiune invalida!")
        return

    text = input("Introduceti textul de filtrare: ").strip().lower()

    taskuri_filtrate = []
    for t in taskuri:
        if text in t[cheie].lower():
            taskuri_filtrate.append(t)

    afiseaza_taskuri(taskuri_filtrate)


def editeaza_task(taskuri, categorii):
    """
    Afiseaza lista de taskuri numerotata si cere utilizatorului sa aleaga
    un task (prin numarul afisat) si campul pe care vrea sa il editeze
    (task, data, persoana responsabila sau categorie).
    Pentru task: verifica sa nu existe deja un alt task cu acelasi text.
    Pentru categorie: verifica ca noua categorie exista in lista de categorii.
    Pentru data si persoana: nu exista validare speciala, valoarea este
    inlocuita direct.
    Trateaza si cazurile de input invalid (numar in afara intervalului
    sau text in loc de numar).
    """
    if len(taskuri) == 0:
        print("Nu exista taskuri de editat!")
        return

    afiseaza_taskuri(taskuri)

    numar = input("Alegeti numarul taskului de editat: ").strip()

    try:
        numar = int(numar)
    except ValueError:
        print("Trebuie sa introduceti un numar valid!")
        return

    if not (1 <= numar <= len(taskuri)):
        print("Numar invalid!")
        return

    index = numar - 1

    print("1. Task")
    print("2. Data")
    print("3. Persoana")
    print("4. Categorie")

    camp = input("Alegeti campul de editare: ").strip()

    if camp == "1":
        cheie = "task"
    elif camp == "2":
        cheie = "data"
    elif camp == "3":
        cheie = "persoana"
    elif camp == "4":
        cheie = "categorie"
    else:
        print("Optiune invalida!")
        return

    if cheie == "task":
        text_nou = input("Introduceti noul text al taskului: ").strip()

        task_lower = []
        for i, t in enumerate(taskuri):
            if i != index:
                task_lower.append(t["task"].lower())

        if text_nou.lower() in task_lower:
            print(f"Eroare: taskul '{text_nou}' exista deja!")
            return

        taskuri[index]["task"] = text_nou
        print("Taskul a fost editat cu succes.")

    elif cheie == "data":
        text_nou = input("Introduceti noua data: ").strip()
        taskuri[index]["data"] = text_nou
        print("Data a fost editata cu succes.")

    elif cheie == "persoana":
        text_nou = input("Introduceti noua persoana: ").strip()
        taskuri[index]["persoana"] = text_nou
        print("Persoana a fost editata cu succes.")

    elif cheie == "categorie":

        text_nou = input("Introduceti noua categorie: ").strip()

        categorii_lower = []

        for c in categorii:
            categorii_lower.append(c.lower())

        if text_nou.lower() not in categorii_lower:
            print(f"Eroare: categoria '{text_nou}' nu exista!")

        else:
            taskuri[index]["categorie"] = text_nou
            print("Categoria a fost editata cu succes.")


def stergere_task(taskuri):
    """
    Afiseaza lista de taskuri numerotata si cere utilizatorului sa aleaga
    un task (prin numarul afisat) pentru a fi sters definitiv din lista.
    Trateaza si cazurile de input invalid (numar in afara intervalului
    sau text in loc de numar).
    """
    if len(taskuri) == 0:
        print("Nu exista taskuri de sters!")
        return

    afiseaza_taskuri(taskuri)

    numar = input("Alegeti numarul taskului de editat: ").strip()

    try:
        numar = int(numar)
    except ValueError:
        print("Trebuie sa introduceti un numar valid!")
        return

    if not (1 <= numar <= len(taskuri)):
        print("Numar invalid!")
        return

    index = numar - 1

    task_sters = taskuri.pop(index)
    print(f"Taskul '{task_sters['task']}' a fost sters cu succes.")


def introducere_categorii_initiale(categorii):
    """
    Cere utilizatorului sa introduca una sau mai multe categorii noi,
    folosind functia adauga_categorie. Dupa fiecare categorie introdusa,
    intreaba utilizatorul daca mai doreste sa adauge una; bucla se
    incheie cand utilizatorul raspunde cu altceva decat "da".
    """
    print("Introduceti categoriile de taskuri:")

    while True:
        adauga_categorie(categorii)

        continua = input("Mai doriti sa adaugati o categorie? (da/nu): ").strip().lower()
        if continua != "da":
            break


def main():
    """
    Functia principala a programului. Incarca datele din fisiere,
    cere categoriile initiale daca nu exista deja, apoi afiseaza
    un meniu in bucla, din care utilizatorul poate alege diverse
    operatii asupra taskurilor si categoriilor, pana cand alege
    sa iasa din program.
    """
    categorii = incarca_categorii()
    taskuri = incarca_taskuri()

    if len(categorii) == 0:
        introducere_categorii_initiale(categorii)
        salveaza_categorii(categorii)

    while True:
        print("\n--- MENIU ---")
        print("1. Listare taskuri")
        print("2. Sortare taskuri")
        print("3. Filtrare taskuri")
        print("4. Adaugare task nou")
        print("5. Editare task")
        print("6. Stergere task")
        print("7. Adaugare categorie noua")
        print("0. Iesire")

        optiune = input("Alegeti o optiune: ").strip()

        if optiune == "1":
            listeaza_taskuri(taskuri)
        elif optiune == "2":
            sorteaza_taskuri(taskuri)
        elif optiune == "3":
            filtreaza_taskuri(taskuri)
        elif optiune == "4":
            adauga_task(taskuri, categorii)
            salveaza_taskuri(taskuri)
        elif optiune == "5":
            editeaza_task(taskuri, categorii)
            salveaza_taskuri(taskuri)
        elif optiune == "6":
            stergere_task(taskuri)
            salveaza_taskuri(taskuri)
        elif optiune == "7":
            adauga_categorie(categorii)
            salveaza_categorii(categorii)
        elif optiune == "0":
            print("La revedere!")
            break
        else:
            print("Optiune invalida!")


main()

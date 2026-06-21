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


def listeaza_taskuri(taskuri):
    taskuri_sortate = sorted(taskuri, key=lambda t: t["categorie"])
    for index, task in enumerate(taskuri_sortate):
        print(f"{index + 1}. {task['task']}, {task['data']}, {task['persoana']}, {task['categorie']}")


def afiseaza_taskuri(taskuri):
    for index, task in enumerate(taskuri):
        print(f"{index + 1}. {task['task']}, {task['data']}, {task['persoana']}, {task['categorie']}")


def listeaza_taskuri(taskuri):
    taskuri_sortate = sorted(taskuri, key=lambda t: t["categorie"])
    afiseaza_taskuri(taskuri_sortate)


def sorteaza_taskuri(taskuri):
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
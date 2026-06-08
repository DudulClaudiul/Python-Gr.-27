# 5. Creati un program care are ca scop un meniu. Meniul se va selecta prin introducerea de la tastaura a unui numar intre 1 si 5 captat intr-o variabila. Printati in terminal acest mesaj:
# “”” 1 – Afisare lista de cumparaturi
# 2 – Adaugare element
# 3 – Stergere element
# 4 – Sterere lista de cumparaturi
# 5 - Cautare in lista de cumparaturi “””
# Apoi folosindu-va de o constructie if-elif-else afisati: - daca utilizatorul scrie de la
# tastaura 1 afisati “Afisare lista de cumparaturi” - daca utilizatorul scrie de la tastaura 2
# afisati “Adugare element” - daca utilizatorul scrie de la tastaura 3 afisati “Stergere
# element” - daca utilizatorul scrie de la tastaura 4 afisati “Sterere lista de cumparaturit”
# - daca utilizatorul scrie de la tastaura 5 afisati “Adaugare element” - daca utilizatorul
# scrie altceva de la tastaura afisati “Alegerea nu exista. Reincercati”
# Implementati logica pentru toate aceste operatii, optional folosind functii.

shopping_list = []

def show_list():
    if shopping_list:
        print(shopping_list)
    else:
        print("Shopping list is empty!")

def add_item():
    item = input("What item do you want to add? ")
    shopping_list.append(item)

def remove_item():
    if shopping_list:
        item = input("What item do you want to delete? ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print(f"{item} doesn't exist in shopping list!")
    else:
        print("Shopping list is empty!")

def clear_list():
    shopping_list.clear()

def search_item():
    search_prod = input("What item do you want to search for?")
    if search_prod in shopping_list:
        print(f"{search_prod} already exists in shopping list!")
    else:
        print(f"{search_prod} Does not exist in shopping list! Do you wish to add it?")
        add_list_item = input("Y/N ")
        if add_list_item == "Y":
            shopping_list.append(search_prod)
            print(f"{search_prod} has been added to shopping list!")
        else:
            print(f"{search_prod} hasn't been added to shopping list!")

while True:
    print("""What action do you wanna do? Type:
    1 - Show shopping list
    2 - Add item to shopping list
    3 - Delete item from shopping list
    4 - Clear shopping list
    5 - Search item in shopping list
    """)

    choice = int(input("Choose option (0 - 5): "))

    if choice == 1:
        show_list()

    elif choice == 2:
        add_item()

    elif choice == 3:
        remove_item()

    elif choice == 4:
        clear_list()

    elif choice == 5:
        search_item()

    elif choice == 0:
        print("Au revoir!")
        break
    else:
        print(f"The chosen option {choice} is not a valid one! Please choose a valid option between 0 and 5.")


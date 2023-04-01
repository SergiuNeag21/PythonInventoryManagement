from Domain.inventar import to_string
from Logic.CRUD import adauga_inventar, sterge_inventar, modificare_inventar
from Logic.Functionalitati import muta_din_inventar, concateneaza_string_pret_mai_mare, cel_mai_mare_pret_locatie, \
    ordonare_crescator_dupa_pret, suma_pret_locatie


def print_menu():
    print("1.Adaugare inventar: ")
    print("2.Stergere inventar: ")
    print("3.Modificare inventar: ")
    print("4.Muta in alta locatie: ")
    print("5.Concateneaza string dupa pret: ")
    print("6.Afisare cel mai mare pret din fiecare locatie: ")
    print("7.Afisare lista ordonata crescator dupa pret: ")
    print("8.Afisare suma pret pentru fiecare locatie: ")
    print("a. Afiseaza toate inventarele: ")
    print("u. Undo ")
    print("r. Redo ")
    print("x. Iesire: ")


def ui_adaugare_inventar(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        descriere = input("Dati descriere: ")
        pret = float(input("Dati pret: "))
        locatie = input("Dati locatia: ")
        rezultat = adauga_inventar(id, nume, descriere, pret, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_stergere_inventar(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul inventarului de sters: ")
        rezultat = sterge_inventar(id, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_modificare_inventar(lista, undo_list, redo_list):
    try:
        id = input("Dati id-ul inventarului de modificat: ")
        nume = input("Dati noul nume: ")
        descriere = input("Dati noua descriere: ")
        pret = float(input("Dati noul pret: "))
        locatie = input("Dati noua locatia: ")
        rezultat = modificare_inventar(id, nume, descriere, pret, locatie, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_muta_din_inventar(lista, undo_list, redo_list):
    try:
        locatie = input("Din ce locatie doresti sa muti?: ")
        locatie_noua = input("Locatia in care doresti sa muti: ")
        rezultat = muta_din_inventar(locatie, locatie_noua, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def ui_concateneaza_string_pret_mai_mare(lista, undo_list, redo_list):
    try:
        cuvant = input("Stringul care va fi concatenat: ")
        val = float(input("Descrierea va fi concatenata pentru pretul mai mare de: "))
        rezultat = concateneaza_string_pret_mai_mare(cuvant, val, lista)
        undo_list.append(lista)
        redo_list.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista
    except Exception as es:
        print("Eroare: {}".format(es))
        return lista


def ui_afiseaza_cel_mai_mare_locatie(lista):
    rezultat = cel_mai_mare_pret_locatie(lista)
    for locatie in rezultat:
        print("Locatia {} are pretul maxim {} ".format(locatie, rezultat[locatie]))


def show_all(lista):
    for inventar in lista:
        print(to_string(inventar))


def ui_ordonare_crescator_pret(lista):
    show_all(ordonare_crescator_dupa_pret(lista))


def ui_suma_pret_locatie(lista):
    rezultat = suma_pret_locatie(lista)
    for locatie in rezultat:
        print("Locatia {} are suma preturilor {}".format(locatie, rezultat[locatie]))


def run_menu(lista):
    redo_list = []
    undo_list = []
    while True:
        print_menu()
        optiune = input("Dati o optiune: ")
        if optiune == "1":
            lista = ui_adaugare_inventar(lista, undo_list, redo_list)
        elif optiune == "2":
            lista = ui_stergere_inventar(lista, undo_list, redo_list)
        elif optiune == "3":
            lista = ui_modificare_inventar(lista, undo_list, redo_list)
        elif optiune == "4":
            lista = ui_muta_din_inventar(lista, undo_list, redo_list)
        elif optiune == "5":
            lista = ui_concateneaza_string_pret_mai_mare(lista, undo_list, redo_list)
        elif optiune == "6":
            ui_afiseaza_cel_mai_mare_locatie(lista)
        elif optiune == "7":
            ui_ordonare_crescator_pret(lista)
        elif optiune == "8":
            ui_suma_pret_locatie(lista)
        elif optiune == "a":
            show_all(lista)
        elif optiune == "u":
            if len(undo_list) > 0:
                redo_list.append(lista)
                lista = undo_list.pop()
            else:
                print("Nu se poate face Undo, lista este goala! ")
        elif optiune == "r":
            if len(redo_list) > 0:
                undo_list.append(lista)
                lista = redo_list.pop()
            else:
                print("Nu se poate face Redo! ")
        elif optiune == "x":
            break
        else:
            print("Ati ales o optiune gresit! Reincercati! ")

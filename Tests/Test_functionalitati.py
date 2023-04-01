from Domain.inventar import get_locatie, get_descriere, creeaza_inventar
from Logic.CRUD import adauga_inventar
from Logic.Functionalitati import muta_din_inventar, concateneaza_string_pret_mai_mare, cel_mai_mare_pret_locatie


def test_muta_din_inventar():
    lista = []
    lista = adauga_inventar("1", "carte", "literatura", 10, "e1", lista)
    lista = adauga_inventar("2", "carte", "literatura", 25, "e2", lista)
    lista = muta_din_inventar("e2", "e5", lista)
    lista = muta_din_inventar("e1", "e6", lista)
    assert get_locatie(lista[0]) == "e6"
    assert get_locatie(lista[1]) == "e5"
    assert get_locatie(lista[1]) != "e6"


def test_concateneaza_string_pret_mai_mare():
    lista = []
    lista = adauga_inventar("1", "carte", "li", 10, "e1", lista)
    lista = adauga_inventar("2", "carte", "li", 25, "e2", lista)
    lista = adauga_inventar("3", "carte", "li", 5, "e3", lista)
    lista = concateneaza_string_pret_mai_mare("SSS", 5, lista)
    assert get_descriere(lista[0]) == "liSSS"
    assert get_descriere(lista[1]) == "liSSS"
    assert get_descriere(lista[2]) == "li"


def test_cel_mai_mare_pret_locatie():
    lista = []
    lista = adauga_inventar("1", "carte", "li", 10, "e1", lista)
    lista = adauga_inventar("2", "carte", "li", 25, "e2", lista)
    lista = adauga_inventar("3", "carte", "li", 5, "e1", lista)
    assert cel_mai_mare_pret_locatie(lista) == {"e1": 10, "e2": 25}
    lista = adauga_inventar("4", "carte", "li", 40, "e2", lista)
    assert cel_mai_mare_pret_locatie(lista) == {"e1": 10, "e2": 40}


# Test laborator 7
def test_undo_redo():
    # 1
    lista_mare = []
    undo_list = []
    redo_list = []

    # 2
    lista = creeaza_inventar("1", "carte", "mat", 10, "e2")
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'}]

    # 3
    lista = creeaza_inventar("2", "carte", "mat", 7, "e2")
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                          {'id': '2', 'nume': 'carte', 'descriere': 'mat', 'pret': 7, 'locatie': 'e2'}]

    # 4
    lista = creeaza_inventar("3", "carte", "mat", 5, "e2")
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                          {'id': '2', 'nume': 'carte', 'descriere': 'mat', 'pret': 7, 'locatie': 'e2'},
                          {'id': '3', 'nume': 'carte', 'descriere': 'mat', 'pret': 5, 'locatie': 'e2'}]

    # 5
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                          {'id': '2', 'nume': 'carte', 'descriere': 'mat', 'pret': 7, 'locatie': 'e2'}]

    # 6
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'}]

    # 7
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == []

    # 8
    redo_list.append(lista_mare)
    if len(undo_list) > 0:
        lista_mare = undo_list.pop()
    assert lista_mare == []

    # 9
    lista = creeaza_inventar("1", "carte", "mat", 10, "e2")
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'}]
    lista = creeaza_inventar("2", "carte", "mat", 7, "e2")
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                          {'id': '2', 'nume': 'carte', 'descriere': 'mat', 'pret': 7, 'locatie': 'e2'}]
    lista = creeaza_inventar("3", "carte", "mat", 5, "e2")
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                          {'id': '2', 'nume': 'carte', 'descriere': 'mat', 'pret': 7, 'locatie': 'e2'},
                          {'id': '3', 'nume': 'carte', 'descriere': 'mat', 'pret': 5, 'locatie': 'e2'}]

    # 10
    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
        assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                              {'id': '2', 'nume': 'carte', 'descriere': 'mat', 'pret': 7, 'locatie': 'e2'},
                              {'id': '3', 'nume': 'carte', 'descriere': 'mat', 'pret': 5, 'locatie': 'e2'}]

    # 11  2x undo
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                          {'id': '2', 'nume': 'carte', 'descriere': 'mat', 'pret': 7, 'locatie': 'e2'}]
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'}]

    # 12  redo
    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                          {'id': '2', 'nume': 'carte', 'descriere': 'mat', 'pret': 7, 'locatie': 'e2'}]

    # 13  redo
    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
        assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                              {'id': '2', 'nume': 'carte', 'descriere': 'mat', 'pret': 7, 'locatie': 'e2'},
                              {'id': '3', 'nume': 'carte', 'descriere': 'mat', 'pret': 5, 'locatie': 'e2'}]

    # 14 2 x undo
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                          {'id': '2', 'nume': 'carte', 'descriere': 'mat', 'pret': 7, 'locatie': 'e2'}]
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'}]

    # 15 add 04
    lista = creeaza_inventar("4", "carte", "mat", 21, "e2")
    undo_list.append(lista_mare)
    redo_list.clear()
    lista_mare = lista_mare + [lista]
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                          {'id': '4', 'nume': 'carte', 'descriere': 'mat', 'pret': 21, 'locatie': 'e2'}]

    # 16 redo
    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                          {'id': '4', 'nume': 'carte', 'descriere': 'mat', 'pret': 21, 'locatie': 'e2'}]

    # 17 undo
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'}]

    # 18 undo
    redo_list.append(lista_mare)
    lista_mare = undo_list.pop()
    assert lista_mare == []

    # 19 redo redo
    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'}]

    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                          {'id': '4', 'nume': 'carte', 'descriere': 'mat', 'pret': 21, 'locatie': 'e2'}]

    # 20 redo
    if len(redo_list) > 0:
        undo_list.append(lista_mare)
        lista_mare = redo_list.pop()
    assert lista_mare == [{'id': '1', 'nume': 'carte', 'descriere': 'mat', 'pret': 10, 'locatie': 'e2'},
                          {'id': '4', 'nume': 'carte', 'descriere': 'mat', 'pret': 21, 'locatie': 'e2'}]

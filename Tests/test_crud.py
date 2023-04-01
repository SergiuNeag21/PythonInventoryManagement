from Domain.inventar import get_id, get_nume, get_descriere, get_pret, get_locatie
from Logic.CRUD import adauga_inventar, sterge_inventar, get_by_id, modificare_inventar


def test_adauga_inventar():
    lista = []
    lista = adauga_inventar("1", "carte", "literatura", 10, "etaj", lista)

    assert get_id(lista[0]) == "1"
    assert get_nume(lista[0]) == "carte"
    assert get_descriere(lista[0]) == "literatura"
    assert get_pret(lista[0]) == 10
    assert get_locatie(lista[0]) == "etaj"


def test_sterge_inventar():
    lista = []
    lista = adauga_inventar("1", "carte", "literatura", "10", "etaj", lista)
    lista = adauga_inventar("2", "carte", "literatura", "25", "etaj", lista)
    lista = sterge_inventar("1", lista)
    assert len(lista) == 1
    assert get_by_id("1", lista) is None
    assert get_by_id("2", lista) is not None


def test_modifica_inventar():
    lista = []
    lista = adauga_inventar("1", "carte", "literatura", 10, "etaj", lista)
    lista = adauga_inventar("2", "carte", "literatura", 25, "etaj", lista)
    lista = modificare_inventar("1", "culegere", "matematica", 15, "etaj2", lista)

    assert get_id(lista[0]) == "1"
    assert get_nume(lista[0]) == "culegere"
    assert get_descriere(lista[0]) == "matematica"

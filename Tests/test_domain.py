from Domain.inventar import creeaza_inventar, get_id, get_nume, get_descriere, get_pret, get_locatie


def test_inventar():
    inventar = creeaza_inventar("1", "carte", "literatura", 10, "etaj")

    assert get_id(inventar) == "1"
    assert get_nume(inventar) == "carte"
    assert get_descriere(inventar) == "literatura"
    assert get_pret(inventar) == 10
    assert get_locatie(inventar) == "etaj"

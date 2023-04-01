def creeaza_inventar(id, nume, descriere, pret, locatie):
    """
    creeaza un dictionar ce reprezinta un inventar
    :param id: string
    :param nume:string
    :param descriere: string
    :param pret: float
    :param locatie: string
    :return: un dictionar ce contine un inventar
    """
    return{
        "id": id,
        "nume": nume,
        "descriere": descriere,
        "pret": pret,
        "locatie": locatie,
    }


def get_id(inventar):
    """
    Da id-ul unui inventar
    :param inventar: dictionar ce contine un inventar
    :return: id-ul inventarului
    """
    return inventar["id"]


def get_nume(inventar):
    return inventar["nume"]


def get_descriere(inventar):
    return inventar["descriere"]


def get_pret(inventar):
    return inventar["pret"]


def get_locatie(inventar):
    return inventar["locatie"]


def to_string(inventar):
    return "Id: {}, Nume: {}, Descriere: {}, Pret: {}, Locatie: {}".format(
        get_id(inventar),
        get_nume(inventar),
        get_descriere(inventar),
        get_pret(inventar),
        get_locatie(inventar)
    )

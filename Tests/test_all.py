from Tests.Test_functionalitati import test_muta_din_inventar, test_concateneaza_string_pret_mai_mare, \
    test_cel_mai_mare_pret_locatie, test_undo_redo
from Tests.test_crud import test_adauga_inventar, test_sterge_inventar, test_modifica_inventar
from Tests.test_domain import test_inventar


def run_all_tests():
    test_inventar()
    test_adauga_inventar()
    test_sterge_inventar()
    test_modifica_inventar()
    test_muta_din_inventar()
    test_concateneaza_string_pret_mai_mare()
    test_cel_mai_mare_pret_locatie()
    test_undo_redo()

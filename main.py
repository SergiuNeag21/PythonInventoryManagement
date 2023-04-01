from Logic.CRUD import adauga_inventar
from Tests.test_all import run_all_tests
# from UI.Command_line_console import ui_2
from UI.Console import run_menu


def main():
    run_all_tests()
    lista = []
    lista = adauga_inventar("1", "carte", "literatura", 5, "E2", lista)
    lista = adauga_inventar("2", "culegere", "matematica", 10, "E4", lista)
    run_menu(lista)
    # ui_2(lista)


main()

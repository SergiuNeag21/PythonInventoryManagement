from Logic.CRUD import adauga_inventar, sterge_inventar
from UI.Console import show_all


def help():
    print('Legenda:')
    print('add, id, nume, descriere, pret, locatie -> adauga inventar')
    print('showall -> afiseaza toate inventarele')
    print('delete, id -> sterge un inventar,  cu ID-ul dat')
    print('; -> sfarsitul unei comenzi')
    print('stop ,obligatoriu la final -> iesire (dupa stop nu se pune ;)')


def ui_2(lst_inventar):
    print(' ')
    help()
    print(' ')
    while True:
        comenzi = input('Scrie lista de comenzi separate prin ,  si ; pt finalul seriei de comenzi: ; stop  :  ')
        if comenzi == 'stop':
            break
        else:
            lst_comenzi = comenzi.split(';')
            for comanda in lst_comenzi:
                comanda_split = comanda.split(',')

                if comanda_split[0] == 'showall':
                    show_all(lst_inventar)
                elif comanda_split[0] == 'add':
                    lst_inventar = adauga_inventar(int(comanda_split[1]), comanda_split[2],
                                                   comanda_split[3], float(comanda_split[4]),
                                                   comanda_split[5], lst_inventar)
                elif comanda_split[0] == 'delete':
                    lst_inventar = sterge_inventar(int(comanda_split[1]), lst_inventar)

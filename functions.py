from data import repulogepek, erkezes, orszagok
from os import system

def menu():
    system("cls")
    print('-----------MENÜ---------')
    print('0 - Kilépés')
    print('1 - Repülőgépek')
    print('2 - Járatok')
    print('3 - Új gép felvétele')
    print('4 - Honnan érkezik a legtöbb gép')
    print("5 - Fájlbetöltés")
    print("6 - Járat törlése")
    return input('Választás: ')
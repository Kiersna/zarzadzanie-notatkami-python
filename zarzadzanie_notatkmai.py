import os
def dodaj_notatke():
    tytul = input("podaj nazwe pliku notatki: ")
    tresc = input("podaj tresc notatki: ")
    with open(f"{tytul}.txt", 'a') as file:
        file.write(tresc)
    print(f"dodano notatke o nazwie {tytul}")

def czy_pusty_plik(tytul):
    with open(f"{tytul}.txt", 'r') as file:
        return not file.read()
def przegladaj_notatki():
    tytul = input("podaj nazwe pliku notatki ktory chcesz otworzyc: ")
    try:
        with open(f"{tytul}.txt", 'r') as file:
            if czy_pusty_plik(tytul):
                print("plik jest pusty")
            else:
                print(file.read())
    except:
        print("nie moge znalezc notatki o takiej nazwie")
def wyczysc_notatki():
    tytul = input("podaj nazwe pliku notatki do wyczyszczenia: ")
    if not os.path.exists:
        print("notatka nie istnieje")
    else:
        with open(f"{tytul}.txt", 'w') as file:
            file.write("")
        print("notatka zostala wyczyszczona")

def menu():
    wybor = -1
    while(wybor != 0):
        try:
            wybor = int(input("Co chcesz zrobic?: \n 1. Dodaj notatke \n 2. Przegladaj notatki \n 3. wyczysc notatki \n Twoj wybor: "))
        except:
            pass
        match wybor:
            case 1:
                dodaj_notatke()
            case 2:
                przegladaj_notatki()
            case 3:
                wyczysc_notatki()
            case 0:
                exit()
            case -1:
                print("zle podany wybor!")

menu()

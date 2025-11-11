import time
from random import shuffle


def udelej_caru():
    print("-"*54)

def privitani():
    """
    Přivítá hráče ve hře.
    """
    udelej_caru()
    print("Hi there!")
    udelej_caru()
    print("I've generated a random 4 digit number for you.")
    print("Lets play a bulls and caws game.")

def vrat_tajne_cislo()->str:
    """
    Vrací tajné čtyřciferné číslo bez nuly na začátku.
    """
    seznam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        shuffle(seznam)
        tajne_cislo = "".join(map(str, seznam[:4]))
        if not tajne_cislo.startswith("0"):
            return tajne_cislo
            break

def filtruj_vstup()->str:
    """
    Požádá o zadání čísla a zadanou hodnotu pustí dál, jen pokud se jedná
    o čtyřciferné číslo bez nuly na začátku.
    Jinak vypíše upozornění a požaduje nové zadání.
    """
    dotazovani = True
    while dotazovani:
        udelej_caru()
        zadane_cislo = input("enter number: ")
        if not zadane_cislo.isnumeric():
            print("This is not number!")
        elif len(zadane_cislo)!= 4:
            print("Four-digit number is necessary!")
        elif zadane_cislo.startswith("0"):
            print("The first digit must not be zero!")
        else:
            spravne_cislo = True
            for _, cifra in enumerate(zadane_cislo):
                if zadane_cislo.count(cifra) > 1:
                    print("No digit can be used more than once!")
                    spravne_cislo = False
                    break
            if spravne_cislo:
                dotazovani = False
    return zadane_cislo

def vrat_bulls_cows(tajne_cislo: str, zadane_cislo: str)->tuple:
    """
    Porovnává číslo od hráče s tajným číslem.
    Při shodě v hodnotě i umístění určité číslice se bulls zvýší jednu.
    Při shode v hodnote ale špatném umístění se cows zvýší o jednu.
    """
    bulls = 0
    cows = 0
    for index, cifra in enumerate(zadane_cislo):
        if zadane_cislo[index] == tajne_cislo[index]:
            bulls += 1
        else:
            if zadane_cislo[index] in tajne_cislo:
                cows += 1
    return bulls, cows

def spravuj_plural(slovo: str, pocet: int)->str:
    """
    U anglických singulárů "bull", "cow" a "guess"
    dle zadaného počtu vrací plurál nebo singulár.
    """
    if pocet != 1:
        slovo += "es" if slovo.endswith("s") else "s"
    return slovo

def vypis_hodnoceni_pokusu(tajne_cislo: str, zadane_cislo: str)->int:
    """
    Vyhodnocuje pokusy, přiděluje a vypisuje bulls a cows.
    """
    pocet_pokusu = 1
    while zadane_cislo != tajne_cislo:
        bulls, cows = vrat_bulls_cows(tajne_cislo, zadane_cislo)
        bull_s = spravuj_plural("bull", bulls)
        cow_s = spravuj_plural("cow", cows)
        print(f"{bulls} {bull_s}, {cows} {cow_s}")
        zadane_cislo = filtruj_vstup()
        pocet_pokusu += 1

    return pocet_pokusu

def gratuluj_hraci(pocet_pokusu: int, potrebny_cas: float):
    """
    Vypíše gratulaci k uhodnutí tajného čísla.
    Současně informuje o počtu potřebných pokusů a době do uhodnutí.
    """
    guess_es = spravuj_plural("guess", pocet_pokusu)
    print(
        f"Correct, you've guessed the right number in "
        f"{pocet_pokusu} {guess_es}."
        )
    print(f"You needed {potrebny_cas} sec.")
    udelej_caru()
    print("That's amazing!")

def ovladej_hru():
    """
    Spustí hru. Na konci se ptá uživatele, zda chce hrát znovu nebo skončit.
    V případě kladné odpovědi zahájí dalsí hru.
    """
    privitani()
    odpoved = "y"
    while odpoved == "y":
        tajne_cislo = vrat_tajne_cislo()
        start_cas = time.time()
        zadane_cislo = filtruj_vstup()
        pocet_pokusu = vypis_hodnoceni_pokusu(tajne_cislo, zadane_cislo)
        konecny_cas = time.time()
        potrebny_cas = round((konecny_cas - start_cas), 1)
        udelej_caru()
        gratuluj_hraci(pocet_pokusu, potrebny_cas)
        udelej_caru()
        print("Another game?")
        dotaz = input("Yes: Enter y! No: Enter anything else! ")
        odpoved = dotaz.lower()
        udelej_caru()
    print("Good bye!")

if __name__ == "__main__":
    ovladej_hru()
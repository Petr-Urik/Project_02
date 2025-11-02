import inflect
import time
from random import shuffle
from random import choice


def udelej_caru():
  print("-"*53)

def privitani():
  """
  Přivítá hráče ve hře.
  """
  udelej_caru()
  print("Hi there!")
  udelej_caru()
  print("I've generated a random 4 digit number for you.")
  print("Lets play a bulls and caws game.")

def vrat_tajne_cislo()->str: # generovani tajneho ctyrciferneho cisla
  """
  Vrací tajné čtyřciferné číslo bez nuly na začátku.
  """
  seznam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  dotaz = True
  while dotaz:
    shuffle(seznam)
    tajne_cislo = "".join(map(str, seznam[:4]))
    if not tajne_cislo.startswith("0"):
      return tajne_cislo
  dotaz = False

def filtruj_vstup()->str: # ziskani cisla od hrace a filtrovani inputu
  """
  Požádá o zadání čísla a zadanou hodnotu pustí dál, jen pokud se jedná
  o čtyřciferné číslo bez nuly na začátku.
  Jinak vypíše upozornění a požaduje nové zadání.
  """
  dotazovani = True
  while dotazovani:
    udelej_caru()
    zadane_cislo = input("enter number: ")
    if not zadane_cislo.isnumeric(): # pusti pouze ciselne znaky
      print("This is not number!")
    elif len(zadane_cislo)!= 4: # aby zadane cislo bylo ctyrciferne
      print("Four-digit number is necessary!")
    elif zadane_cislo.startswith("0"): # aby cislo nezacinalo nulou
      print("The first digit must not be zero!")
    else: # aby se cislice neopakovaly
      spravne_cislo = True
      for index, cifra in enumerate(zadane_cislo):
        if zadane_cislo.count(cifra) > 1:
          print("No digit can be used more than once!")
          spravne_cislo = False # zmena na False u opakujici se cislice
          break # ukonceni vnitrni smycky u opakujici se cislice
      if spravne_cislo: # zmena dotazovani na False u vyhovujiciho cisla
        dotazovani = False
  return zadane_cislo

def vrat_bulls_cows(tajne_cislo: str, zadane_cislo: str)->tuple:
  """
  Porovnává číslo od hráče s tajným číslem.
  Při shodě v hodnotě i umístění určité číslice se bulls zvýší jednu.
  Při shode v hodnote ale špatném umístění cows se zvýší o jednu.
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
  U anglických podst. jmen dle zadaného počtu vrací plurál nebo singulár.
  """
  p = inflect.engine()
  if pocet == 1:
    slovo = p.singular_noun(slovo)
  return slovo

def vypis_hodnoceni_pokusu(tajne_cislo: str, zadane_cislo: str)->int:
  """
  Vyhodnocuje pokusy, přiděluje a vypisuje bulls a cows.
  """
  pocet_pokusu = 1
  while zadane_cislo != tajne_cislo:
    bulls, cows = vrat_bulls_cows(tajne_cislo, zadane_cislo)
    # sprava pluralu
    byci = spravuj_plural("bulls", bulls)
    kravy = spravuj_plural("cows", cows)
    print(f"{bulls} {byci}, {cows} {kravy}")
    zadane_cislo = filtruj_vstup() # vyzva k zadani dalsiho cisla
    pocet_pokusu += 1
  return pocet_pokusu

def gratuluj_hraci(pocet_pokusu: int, potrebny_cas: float):
  """
  Vypíše gratulaci k uhodnutí tajného čísla.
  Současně informuje o počtu potřebných pokusů a době do uhodnutí.
  """
  # sprava pluralu
  pokusy = spravuj_plural("guesses", pocet_pokusu)
  print(f"Correct, you've guessed the right number in {pocet_pokusu} {pokusy}")
  print(f"You needed {potrebny_cas} sec.")
  udelej_caru()
  print("That's amazing!")

def ovladej_hru():
  """
  Spustí hru. Na konci se ptá uživatele, zda chce hrát znovu nebo skončit.
  V případě kladné odpovědi zahájí dalsí hru.
  """
  privitani() # uvodni hra
  tajne_cislo = vrat_tajne_cislo()
  print(tajne_cislo) # docasny prikaz pro testovani
  start_cas = time.time()# zacatek mereni casu
  zadane_cislo = filtruj_vstup()
  pocet_pokusu = vypis_hodnoceni_pokusu(tajne_cislo, zadane_cislo)
  konecny_cas = time.time()# konec mereni casu
  potrebny_cas = round((konecny_cas - start_cas), 1)
  udelej_caru()
  gratuluj_hraci(pocet_pokusu, potrebny_cas)
  udelej_caru()
  print("Another game?")
  dotaz = input("Yes: Enter y! No: Enter anything else! ")
# dalsi hra
  while dotaz.lower() == "y": # pro pripad, ze bude zadano velke Y
    tajne_cislo = vrat_tajne_cislo()
    print(tajne_cislo) # docasny prikaz pro testovani
    start_cas = time.time()# zacatek noveho mereni casu
    zadane_cislo = filtruj_vstup()
    pocet_pokusu = vypis_hodnoceni_pokusu(tajne_cislo, zadane_cislo)
    konecny_cas = time.time()# konec noveho mereni casu
    potrebny_cas = round((konecny_cas - start_cas), 1)
    udelej_caru()
    gratuluj_hraci(pocet_pokusu, potrebny_cas)
    udelej_caru()
    print("Another game?")
    dotaz = input("Yes: Enter y! No: Enter anything else! ")
    udelej_caru()
  print("Good bye!") # vypis pri rozhodnuti nepokracovat ve hre

if __name__ == "__main__":
  ovladej_hru()
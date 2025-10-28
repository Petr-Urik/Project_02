from itertools import permutations
from random import choice
import time

cara = "-" * 54
print(f"Hi there!\n{cara}\nI've generated a random 4 digit number for you.")
print(f"Lets play a bulls and caws game.\n{cara}")

# generovani tajneho ctyrciferneho cisla
def vrat_tajne_4ccislo()->str:
  """
  Vrací tajné čtyřciferné číslo bez nuly na začátku.
  """
  def generuj_4cpermutace()->list:
    """
    Vrací čtyřčetné permutace znaků ze stringu "0123456789"
    """
    permutace = permutations("0123456789", 4)
    return ["".join(p) for p in permutace]

  #vyber permutaci bez nuly na zacatku
  list_permutaci = generuj_4cpermutace()
  soubor_tajne = []
  for clen in list_permutaci:
    if clen[0] == "0":
      continue
    soubor_tajne.append(clen)
  return choice(soubor_tajne)

# ziskani cisla od hrace a filtrovani inputu
def filtruj_vstup()->str:
  """
  Požádá o zadání čísla.
  Zadanou hodnotu pustí dál jen pokud se jedná
  o čtyřciferné číslo bez nuly na začátku.
  Jinak vypíše upozornění a požaduje nové zadání.
  """
  dotazovani = True
  while dotazovani:
    enter_number = input("enter_number: ")
    print(cara)
    if not enter_number.isnumeric():
      print("This is not number!")
    elif len(str(enter_number))!= 4:
      print("Four-digit number is necessary!")
    elif (str(enter_number)[0]) == "0":
      print("The first digit must not be zero!")
    else:# aby se cislice neopakovaly
      for p in range(10):
        if (str(enter_number)).count(str(p)) > 1:
          print("No digit can be used more than once!")
        else:
          dotazovani = False
  return enter_number

# porovnavani cisla od hrace s tajnym cislem
def vrat_buls_cows(secret_number: str, number: str)->int:
  """
  Porovnává číslo od hráče s tajným číslem.
  Pokud nastane shoda v hodnotě i umístění určité číslice bulls se zvýší jednu.
  Pokud je určitá číslice v hráčově čísle obsažena v tajném čísle,
  ale nesouhlasí umístění, caws se zvýší o jednu.
  ----------
  Parametry:
  secret_number: str
  number: str
  """
  p = 0
  bulls = 0
  cows = 0

  while p < 4:
    if number[p] == secret_number[p]:
      bulls += 1
    else:
      if number[p] in secret_number:
          cows += 1
    p += 1
  return bulls, cows

#ziskani tajneho a zadaneho cisla pro porovnani a vyhodnoceni
def vyhodnocuj_pokusy():
  """
  Porovnává uživatelem zadaná čísla s tajným číslem.
  Vyhodnocuje pokusy a přiděluje bulls a cows.
  Současně měří čas do uhodnutí tajného čísla.
  """
  secret_number = vrat_tajne_4ccislo()
  number = filtruj_vstup()
  start_time = time.time()#zacatek mereni casu

  #porovnani a vyhodnocovani
  guesses = 1
  while number != secret_number:
    bulls, cows = vrat_buls_cows(secret_number, number)
    # podminky pro zajisteni mluvnicke spravnosti vysledku
    if bulls == 1 and cows == 1:
      print(f"bull: {bulls}, cow: {cows}\n{cara}")
    elif bulls == 1 and cows != 1:
      print(f"bull: {bulls}, cows: {cows}\n{cara}")
    elif bulls != 1 and cows == 1:
      print(f"bulls: {bulls}, cow: {cows}\n{cara}")
    number = filtruj_vstup()
    guesses += 1
  end_time = time.time()#konec mereni casu
  elapsed_time = round((end_time - start_time), 1)

  print(f"Correct, you've guessed the right number in {guesses} guesses.")
  print(f"You needed {elapsed_time} sec.\n{cara}\nThat's amazing!")

def ridici_fce():
  """
  Spustí první hru. Na jejím konci se ptá uživatele,
  zda chce hrát znovu nebo program ukončit.
  """
  vyhodnocuj_pokusy()#prvni spusteni hry
  print(f"{cara}\nAnother game?")
  dotaz = input("Yes: enter y, No: enter n.")
  while dotaz == "y":
    vyhodnocuj_pokusy()#dalsi spusteni hry
    print(f"{cara}\nAnother game?")
    dotaz = input("Yes: enter y, No: enter n.")
    print(cara)
  print("Good bye!")

ridici_fce()

def mika_lista(): # funktio listan valitsemiselle eli vaihtoehto 1. Funktion paluuarvona käyttäjän syöttämä numero 
    print("\nSovelluksesta löytyy seuraavat listat:")
    print("1. Arkiruoat")  
    print("2. Viikonloppu")
    print("3. Syntymäpäiväjuhlat")
    return input("Minkä listan haluat avata? Kerro numero: ")

def mika_toiminto(): # funktio toiminnon valitsemiselle eli vaihtoehto 2. Funktion paluuarvona käyttäjän syöttämä numero
    print("\nMitä haluat tehdä listalle?")
    print("1. Näytä lista")
    print("2. Lisää uusi asia listalle")
    print("3. Poista asia listalta")
    print("4. Lopeta")
    print("5. Sulje tämä ja valitse toinen lista")
    return input("Valitse numero: ")


def nayta_lista(tiedoston_nimi):  # funktio listan näyttämiselle eli vaihtoehto 1. Funktion paremetrina tiedoston nimi
    try:     # yritetään avata tiedostoa, jos ei onnistu, tulostetaan virheilmoitus eikä anneta ohjelman kaatua
        with open(tiedoston_nimi, "r") as tiedosto: # avataan tiedosto read-tilassa, jotta voidaan lukea sen sisältöä
            print("\nOstoslista:") # tulostetaan otsikko
            for rivi in tiedosto:  # käydään tiedosto rivi riviltä läpi
                kpl, tuote = rivi.strip().split(",")  # erotellaan kappalemäärä ja tuote
                print(f"{kpl} x {tuote}") # tulostetaan kappalemäärä x-merkki ja tuotteen nimi
    except FileNotFoundError:     # jos tiedostoa ei löydy, tulostetaan virheilmoitus ja kerrotaan käyttäjälle
        print("Ostoslista on tyhjä. Lisää ensin tuotteita.")


def lisaa_listaan(tiedoston_nimi):   # funktio listalle lisäämiselle eli vaihtoehto 2. Funktion paremetrina tiedoston nimi
    try:                # yritetään avata tiedostoa, jos ei onnistu, tulostetaan virheilmoitus eikä anneta ohjelman kaatua
        with open(tiedoston_nimi, "a") as tiedosto:     # avataa tiedosto append-tilassa, jotta voidaan lisätä uusia tuotteita listan loppuun ilman että vanhat poistuvat
            tuote = input("Kirjoita lisättävä tuote: ") # kysytään käyttäjältä tuotteen nimi
            kpl = input("Kuinka monta kappaletta? ")    # kysytään käyttäjältä tuotteen kappalemäärä
            tiedosto.write(f"{kpl},{tuote}\n") # kirjoitetaan tiedostoon kappalemäärä, pilkku ja tuote
            print(f"{kpl} x {tuote} lisätty ostoslistaan.") # kuittaus käyttäjälle, että tuote on lisätty onnistuneesti
    except FileNotFoundError:      # jos tiedostoa ei löydy, tulostetaan virheilmoitus ja kerrotaan käyttäjälle
        print("Tiedostoa ei löytynyt. Yritä myöhemmin uudelleen.")


def poista_listalta(tiedoston_nimi): # funktio listalta poistamiselle eli vaihtoehto 3. Funktion paremetrina tiedoston nimi
    try: # yritetään avata tiedostoa, jos ei onnistu, tulostetaan virheilmoitus eikä anneta ohjelman kaatua
        with open(tiedoston_nimi, "r") as tiedosto: # avataan tiedosto read-tilassa, jotta voidaan lukea sen sisältöä
            rivit = tiedosto.readlines()    # luetaan tiedoston rivit listaksi, rivi kerrallaan ja tallennetaan muuttujaan rivit
        if not rivit: # jos tiedosto on tyhjä, tulostetaan virheilmoitus ja palataan takaisin
            print("Ostoslista on tyhjä.")
            return

        print("\nNykyinen ostoslista:") # kerrotaan nykyisen listan sisältö
        kelvolliset_rivit = [] # luodaan tyhjä lista, johon tallennetaan vain kelvolliset rivit
        for i, rivi in enumerate(rivit, start=1): # käydään listan rivit läpi ja tulostetaan ne numeroituna
            rivi = rivi.strip() # poistetaan rivin alusta ja lopusta ylimääräiset välilyönnit
            if "," in rivi: # jos rivissä on pilkku, se on kelvollinen rivi
                try: # yritetään jakaa rivi pilkun kohdalta kahteen osaan
                    kpl, tuote = rivi.split(",", 1) # erotetaan kappalemäärä ja tuote
                    print(f"{i}. {kpl} x {tuote}") # tulostetaan rivi numeroituna
                    kelvolliset_rivit.append(rivi)  # Lisää vain kelvolliset rivit listaan
                except ValueError: # jos tulee arvovirhe, kerrotaan käyttäjälle ja ohitetaan rivi
                    print(f"{i}. Virheellinen rivi ohitetaan: {rivi}")
            else: # jos jokin muu kuin pilkku, tulostetaan virheilmoitus ja ohitetaan rivi
                print(f"{i}. Virheellinen rivi ohitetaan: {rivi}")

        valinta = input("Anna poistettavan kohdan numero: ").strip() # pyydetään käyttäjää valitsemaan poistettava rivi
        if not valinta.isdigit():  # Varmistetaan, että syöte on kokonaisluku
            print("Virheellinen syöte. Anna numero.") # jos käyttäjä syöttää muun kuin numeron, tulostetaan virheilmoitus
            return # palataan takaisin

        valinta = int(valinta)  # Muutetaan numero kokonaisluvuksi
        
        if 1 <= valinta <= len(kelvolliset_rivit): #tarkistetaan, että valinta on listan sisällä
            poistettava = kelvolliset_rivit[valinta - 1] # Poistettava rivi on listan indeksissä valinta - 1, koska me aloitimme numeroinnin ykkösestä
            rivit.remove(poistettava + "\n")  # Poistetaan rivi myös alkuperäisestä listasta
            with open(tiedoston_nimi, "w") as tiedosto: # avataan tiedosto write-tilassa, jotta voidaan kirjoittaa uusi lista
                tiedosto.writelines(rivit) # kirjoitetaan uusi lista tiedostoon
            print(f"Poistettu: {poistettava}")  # kerrotaan käyttäjälle, että rivi on poistettu
        else:
            print("Virheellinen valinta. Numero ei vastaa listaa.") # jos käyttäjä syöttää muun kuin listan numeron, tulostetaan virheilmoitus
    except FileNotFoundError: # jos tiedostoa ei löydy, tulostetaan virheilmoitus ja kerrotaan käyttäjälle
        print("Tiedostoa ei löytynyt. Lisää ensin tuotteita.")
    except Exception as e:  # jos tulee jokin muu virhe, tulostetaan virheilmoitus ja kerrotaan käyttäjälle
        print(f"Tuntematon virhe: {e}")

def lopeta(): # funktio ohjelman lopettamiselle eli vaihtoehto 4
    print("Kiitos ohjelman käytöstä. Näkemiin!")



def main(): # pääohjelma
    print("Tervetuloa ostoslistasovellukseen!") # tulostetaan tervehdys
    while True: # toistetaan ohjelmaa niin kauan kunnes käyttäjä valitsee lopetuksen
        lista = mika_lista() # kutsutaan funktiota mika_lista ja tallennetaan sen paluuarvo muuttujaan lista
        if lista == "1": # jos käyttäjä valitsee listan 1, avataan tiedosto arkiruoat.txt
            tiedoston_nimi = "arkiruoat.txt"
        elif lista == "2": # jos käyttäjä valitsee listan 2, avataan tiedosto viikonloppu.txt
            tiedoston_nimi = "viikonloppu.txt"
        elif lista == "3": # jos käyttäjä valitsee listan 3, avataan tiedosto synttarijuhlat.txt
            tiedoston_nimi = "synttarijuhlat.txt"
        else: # jos käyttäjä syöttää muun kuin 1, 2 tai 3, tulostetaan virheilmoitus ja kysytään uudelleen
            print("Virheellinen valinta.")
            continue

        while True: # toistetaan ohjelmaa niin kauan kunnes käyttäjä valitsee lopetuksen
            toiminto = mika_toiminto() # kutsutaan funktiota mika_toiminto ja tallennetaan sen paluuarvo muuttujaan toiminto
            if toiminto == "1": # jos käyttäjä valitsee toiminnon 1, kutsutaan funktiota nayta_lista
                nayta_lista(tiedoston_nimi)
            elif toiminto == "2": # jos käyttäjä valitsee toiminnon 2, kutsutaan funktiota lisaa_listaan
                lisaa_listaan(tiedoston_nimi)
            elif toiminto == "3": # jos käyttäjä valitsee toiminnon 3, kutsutaan funktiota poista_listalta
                poista_listalta(tiedoston_nimi)
            elif toiminto == "4": # jos käyttäjä valitsee toiminnon 4, kutsutaan funktiota lopeta ja lopetetaan ohjelma
                lopeta() # kutsutaan funktiota lopeta
                return       # poistutaan silmukasta
            elif toiminto == "5": # jos käyttäjä valitsee toiminnon 5, poistutaan silmukasta ja palataan listan valintaan
                break # poistutaan sisemmästä silmukasta ja palataan valitsemaan listaa uudelleen
            else:
                print("Virheellinen valinta. Yritä uudelleen.")



if __name__ == "__main__": # kutsutaan pääohjelmaa
    main()



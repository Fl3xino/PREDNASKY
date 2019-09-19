import random
import time

def KdeToJsme():
    print("Vítejte do kasína!")
    time.sleep(2)
    print("Copak si chcete zahrát?")
    time.sleep(2)

def tiskni_hod_kostkou():
    znova = "ano"
    while znova == "ano" or znova == "Ano":
        cislo = random.randint(1,6)
        text = f"Hodil/a jsi èíslo {cislo} na kostce!"
        print(text)
        nepritel = random.randint(1,6)
        txt = f"Tvùj nepøítel hodil {nepritel} na kostce!"
        print(txt)
        zprava = random.randint(1, 5)
        if cislo > nepritel:

            if zprava == 1:
                print("Koukám, že jsi dneska mìl/a docela štìstí!")

            elif zprava == 2:
                print("Pìknì, jsem zvìdav jak se ti to povede pøíštì!")

            elif zprava == 3:
                print("Hmm, máš štìstí, to se mì nelíbí!")

            elif zprava == 4:
                print("Nemysli si, že pøíštì taky vyhraješ!")

            else:
                print("Podcenil jsem tì, pøíštì se musím pøipravit lépe...")


        elif cislo < nepritel:

            if zprava == 1 or 2:
                print("Ha, prohrál/a jsi!")

            elif zprava == 3 or 4:
                print("Tomu bych neøíkal štìstí, prostì jsem lepší!")

            else:
                print("Docela jsi mì podcenil, a to jsi nemìl!")



        else:
            print("shoda? tak to nefunguje! Házej znova!")
            reroll1 = random.randint(1,6)
            reroll2 = random.randint(1,6)
            rrll1 = f"Hodil/a jsi èíslo {reroll1} na kostce!"
            rrll2 = f"Tvùj nepøítel hodil {reroll2} na kostce!"
            print(rrll1)
            print(rrll2)

            if reroll1 > reroll2:
                print("Tak dobøe no, tak jsi vyhrál!")

            elif reroll1 < reroll2:
                print("HA,tak pøeci jenom jsem vyhrál!")

            else:
                print("Tohle už není normální, konèím tu s tebou!")
        znova = input("Chceš si zahrát znova? Tak napiš ano: ")
    print("Tak zase nìkdy!")

def Hadani_cisla():
    dalsipokus = "ano"
    while dalsipokus == "ano" or dalsipokus == "Ano":

        actual_cislo = random.randint(1, 50)

        cislo = int(input("Tak mi øekni co si myslíš že si myslím v rozmezí od 1 do 50: "))

        if cislo > 50 or cislo < 1:
            print("Nevím jestli èteš správnì ale øekl jsem od 1 do 50!")



        elif cislo < 50 or cislo == 50:
            if cislo == actual_cislo:
                 print(f"Pìkné, èíslo {actual_cislo} je moje oblíbené, pøíštì si na tebe vezmu nìco lepšího!!")

            else:
                 print(f"Chyba bylo to {actual_cislo}!")
        dalsipokus = input("Chceš to zkusit znova? Tak napiš ano!: ")

    print("No nevadí tak zase nìkdy!")

def Ruleta():
    print("Takže ruleta jo? Tak dobøe no!")
    print("Na zaèátku ti dám 500 žetonù zdarma, jestli to všechno prohraješ tak tvoje smùla!")
    zetony = 500
    dal = "ano"
    while "ano" in dal.lower():
        sazka = int(input("tak kolik chceš vsadit?: "))
        if sazka > zetony:
            print("smùla, tolik ještì nemáš!")
        else:
            barva = input("Tak jakou barvu tipuješ? Zelená 5x, èerná a èervená 2x: ")
            if "zelená" in barva.lower() or "zelena" in barva.lower():
                barlos = 3
            elif "èervená" in barva.lower() or "cervena" in barva.lower():
                barlos = 1
            elif "èerná" in barva.lower() or "cerna" in barva.lower():
                barlos = 2

            los = random.randint(1, 100)
            if los < 49:
                losbarva = 1
            elif 49 < los < 98:
                losbarva = 2
            else:
                losbarva = 3

            if losbarva == 1:
                if barlos == 1:
                    sazka = sazka*2
                    zetony += sazka
                    print(f"Trefil jsi se do èervené! Pìkná práce, právì teï máš {zetony} žetonù!")
                else:
                    zetony -= sazka
                    print("Smùla, tentokrát to nevyšlo! zkus to znova!")


            elif losbarva == 2:
                if barlos == 2:
                    sazka = sazka*2
                    zetony += sazka
                    print(f"Pìkný, trefil jsi se do èerné, tvoje konto teï obsahuje {zetony} žetonù!")
                else:
                    zetony -= sazka
                    print("Smùla, tentokrát to nevyšlo! zkus to znova!")


            elif losbarva == 3:
                if barlos == 3:
                    sazka = sazka*5
                    zetony += sazka
                    print(f"WOW, trefil jsi zelenou! Právì máš {zetony} žetonù!")
                else:
                    zetony -= sazka
                    print("Smùla, tentokrát to nevyšlo! zkus to znova!")


        dal = input("chceš hrát dál? Tak napiš Ano: ")





def __main__():
    KdeToJsme()
    time.sleep(1)
    print("1. Hod kostkami")
    print("2. Hádání èísla")
    print("3. Klasickou nudnou ruletu!")
    time.sleep(2)
    hra = input("Tak kterou?: ")
    if hra == "1":
        tiskni_hod_kostkou()
    elif hra == "2":
        Hadani_cisla()
    elif hra == "3":
        Ruleta()
    else:
        print("No nevadí, tøeba si to ještì rozmyslíš!")
__main__()
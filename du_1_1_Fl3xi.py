import random
import time

def KdeToJsme():
    print("V�tejte do kas�na!")
    time.sleep(2)
    print("Copak si chcete zahr�t?")
    time.sleep(2)

def tiskni_hod_kostkou():
    znova = "ano"
    while znova == "ano" or znova == "Ano":
        cislo = random.randint(1,6)
        text = f"Hodil/a jsi ��slo {cislo} na kostce!"
        print(text)
        nepritel = random.randint(1,6)
        txt = f"Tv�j nep��tel hodil {nepritel} na kostce!"
        print(txt)
        zprava = random.randint(1, 5)
        if cislo > nepritel:

            if zprava == 1:
                print("Kouk�m, �e jsi dneska m�l/a docela �t�st�!")

            elif zprava == 2:
                print("P�kn�, jsem zv�dav jak se ti to povede p��t�!")

            elif zprava == 3:
                print("Hmm, m� �t�st�, to se m� nel�b�!")

            elif zprava == 4:
                print("Nemysli si, �e p��t� taky vyhraje�!")

            else:
                print("Podcenil jsem t�, p��t� se mus�m p�ipravit l�pe...")


        elif cislo < nepritel:

            if zprava == 1 or 2:
                print("Ha, prohr�l/a jsi!")

            elif zprava == 3 or 4:
                print("Tomu bych ne��kal �t�st�, prost� jsem lep��!")

            else:
                print("Docela jsi m� podcenil, a to jsi nem�l!")



        else:
            print("shoda? tak to nefunguje! H�zej znova!")
            reroll1 = random.randint(1,6)
            reroll2 = random.randint(1,6)
            rrll1 = f"Hodil/a jsi ��slo {reroll1} na kostce!"
            rrll2 = f"Tv�j nep��tel hodil {reroll2} na kostce!"
            print(rrll1)
            print(rrll2)

            if reroll1 > reroll2:
                print("Tak dob�e no, tak jsi vyhr�l!")

            elif reroll1 < reroll2:
                print("HA,tak p�eci jenom jsem vyhr�l!")

            else:
                print("Tohle u� nen� norm�ln�, kon��m tu s tebou!")
        znova = input("Chce� si zahr�t znova? Tak napi� ano: ")
    print("Tak zase n�kdy!")

def Hadani_cisla():
    dalsipokus = "ano"
    while dalsipokus == "ano" or dalsipokus == "Ano":

        actual_cislo = random.randint(1, 50)

        cislo = int(input("Tak mi �ekni co si mysl� �e si mysl�m v rozmez� od 1 do 50: "))

        if cislo > 50 or cislo < 1:
            print("Nev�m jestli �te� spr�vn� ale �ekl jsem od 1 do 50!")



        elif cislo < 50 or cislo == 50:
            if cislo == actual_cislo:
                 print(f"P�kn�, ��slo {actual_cislo} je moje obl�ben�, p��t� si na tebe vezmu n�co lep��ho!!")

            else:
                 print(f"Chyba bylo to {actual_cislo}!")
        dalsipokus = input("Chce� to zkusit znova? Tak napi� ano!: ")

    print("No nevad� tak zase n�kdy!")

def Ruleta():
    print("Tak�e ruleta jo? Tak dob�e no!")
    print("Na za��tku ti d�m 500 �eton� zdarma, jestli to v�echno prohraje� tak tvoje sm�la!")
    zetony = 500
    dal = "ano"
    while "ano" in dal.lower():
        sazka = int(input("tak kolik chce� vsadit?: "))
        if sazka > zetony:
            print("sm�la, tolik je�t� nem�!")
        else:
            barva = input("Tak jakou barvu tipuje�? Zelen� 5x, �ern� a �erven� 2x: ")
            if "zelen�" in barva.lower() or "zelena" in barva.lower():
                barlos = 3
            elif "�erven�" in barva.lower() or "cervena" in barva.lower():
                barlos = 1
            elif "�ern�" in barva.lower() or "cerna" in barva.lower():
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
                    print(f"Trefil jsi se do �erven�! P�kn� pr�ce, pr�v� te� m� {zetony} �eton�!")
                else:
                    zetony -= sazka
                    print("Sm�la, tentokr�t to nevy�lo! zkus to znova!")


            elif losbarva == 2:
                if barlos == 2:
                    sazka = sazka*2
                    zetony += sazka
                    print(f"P�kn�, trefil jsi se do �ern�, tvoje konto te� obsahuje {zetony} �eton�!")
                else:
                    zetony -= sazka
                    print("Sm�la, tentokr�t to nevy�lo! zkus to znova!")


            elif losbarva == 3:
                if barlos == 3:
                    sazka = sazka*5
                    zetony += sazka
                    print(f"WOW, trefil jsi zelenou! Pr�v� m� {zetony} �eton�!")
                else:
                    zetony -= sazka
                    print("Sm�la, tentokr�t to nevy�lo! zkus to znova!")


        dal = input("chce� hr�t d�l? Tak napi� Ano: ")





def __main__():
    KdeToJsme()
    time.sleep(1)
    print("1. Hod kostkami")
    print("2. H�d�n� ��sla")
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
        print("No nevad�, t�eba si to je�t� rozmysl�!")
__main__()
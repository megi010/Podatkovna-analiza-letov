import json, requests, time
from podprogrami import iata
from podprogrami.izbiralec_letov import IzbiralecLetov
from posodabljanje_podatkov import posodobi_vse
import os
from Podatki import get_podatki
from podprogrami import grafi

def vnesi_datum(msg = "vpisite datum (yyyy-mm-dd): "):
    """funkcija, ki uporabnika prosi da vnese datum ter ga vrne"""
    while True:
            try:
                inp = input(msg)
                datum1 = inp.split("-")
                if len(datum1[0]) == 4 or inp=="": #recimo da je to dovolj dober test
                    break
            except:
                print("prosim vnesite primeren datum.")
    return inp

def naj_leti(kam_letis, tabela_letaisc = "LJU", n = 1):
    """funkcija sprejme letalisce v katero letimo, tabelo letalisc (tabela nizov znakov npr ljubljana bi bila "LJU") iz katerega letimo 
    in celo stevilo n.
    Funkcija nato vprasa uporabnika da vnes se ostale potrebne podatke in vrne n najbolsih letov, glede na
    uporabnikove preference
    """
    inp = input("zelite nastaviti svoje preference? (ja,ne): ")
    if inp == "ja":
        izbiralec.vpis_preference()
        izbiralec.vpis_sprejemljive_ure_cakanja()
    datum1 = vnesi_datum("vpisite datum odhoda (yyyy-mm-dd): ")
    datum2 = vnesi_datum("vpisite datum vrnitve (yyyy-mm-dd), ce hocete enosmeren let pustite prazno: ")
    
    naj_leti, link = izbiralec.najbolsi_let(tabela_letaisc, kam_letis, datum1, datum2, n)
    return naj_leti, link

def Zapisi_naj_lete_v_dat(najbolsi_leti, link):
    """funkcija zapiše nekatere podatke iz letov v datoteko najbolsi_leti.txt,
    podatke, ki jih shrani so, cena, cas potovanja, karbonske_emisije, hyperpovezavo do booking leta
    """
    with open("najbolsi_leti.txt", "w", encoding="utf-8") as dat:
        i = 0
        dat.write(f"link do booking letov: {link}\n")
        for let in najbolsi_leti:
            i += 1
            dat.write(f"{i}\n")
            dat.write(f"letalska druzba: {let["flights"][0]["airline"]}\n")
            dat.write(f"cena: {let["price"]} EUR\n")
            dat.write(f"cas potovanja: {let["total_duration"]} min\n")
            dat.write(f"karbonske emisije: {let["carbon_emissions"]["this_flight"]} kg CO2\n")
            dat.write("Podana je pot do destinacije v obliki: letalisce -> letalska druzba -> letalisce \n")
            for posamezen_let in let["flights"]:
                dat.write(posamezen_let["departure_airport"]["name"] + f"-> {posamezen_let['flight_number']} ->" + posamezen_let["arrival_airport"]["name"] + "\n")
            dat.write("\n")


def izbira_grafa(podatki):
    """funkcija, dobi podatke in izriše graf za katerega zaprosi uporabnik"""
    while True:
        print("\n\n- Iz seznama izbereš številko, tistega, kar želiš, da se izvede.")
        print("\nSedaj pa izberi iz seznama!")
        print("\n0 - nazaj\n1 - graf povprečne zamude na letališče\n2 - graf prometa med letališči in poprečne zamude na letališče\n",
               "3 - graf intenzitet letov na letalsko družbo\n4 - najbolj uporabljeno letalo\n5 - tortni diagram uporabljenih letal\n",
               "6 - graf hitrosti letal\n", "7 - graf število letov letalskih družb\n"
               , sep="")
        izbira = input("Vnesi številko iz seznama: ")
        if izbira == "0":
            break
        if izbira == "1":
            grafi.graf_zamude_letalisc(podatki)
        if izbira == "2":
            grafi.graf_prometa_in_zamud(podatki)
        if izbira == "3":
            grafi.graf_inenzitete_letov_na_letalsko_druzbo(podatki)
        if izbira == "4":
            grafi.najpodostejse_letalo(podatki)
        if izbira == "5":
            grafi.graf_najpogostejsih_letal_torta(podatki)
        if izbira == "6":
            grafi.graf_hitrosti(podatki)
        if izbira == "7":
            grafi.graf_st_letov_na_letalsko_druzbo(podatki)
        



izbiralec = IzbiralecLetov()

print("\n 〰〰〰️✈︎ Dobrodošli v programu za iskanje letalskih statistik in najboljših letov! 〰〰〰〰\n")
time.sleep(0.5)
print("\nNekaj splošnih informacij!\n")
time.sleep(0.5)
print("- V programu uporabljamo IATO kodo.")
niz = "IATA koda letališča je tridigitalna oznaka, s katero se letališča enostavno identificirajo po svetu. IATA kodo izbranega letališča lahko najdeš tudi tukaj: https://www.iata.org/en/publications/directories/code-search/".split()
for beseda in niz:
    print(beseda, end=' ', flush=True)
    time.sleep(0.07)

time.sleep(0.7)

while True:
    print("\n\n- Iz seznama izbereš številko, tistega, kar želiš, da se izvede.")
    print("\nSedaj pa izberi iz seznama!")
    print("\n0 - zaključitev programa\n1 - statistika letov po svetu\n2 - statistika letov po evropi\n3 - dodajanje podatkov k statistiki\n4 - iskalnik letov\n5 - iskalnik letov iz bližnjih letališč\n")
    izbira = input("Vnesi številko iz seznama: ")

    if izbira == "0": #zakljuci program
        break
    if izbira == "1": #statistika letov po svetu
        #preberemo podatke
        podatki = get_podatki.get_vsi_podatki()
        izbira_grafa(podatki)

    if izbira == "2": #statistika letov po evropi
        #preberemo pdoatke
        podatki = get_podatki.get_podatki_evrope()
        izbira_grafa(podatki)

    if izbira == "3": #dodaj/posodobi podatke
        posodobi_vse.posodobi_vse_podatke()

    if izbira == "4": #iskalnik letov
        kam = input("prosim vnesite ime letalisca kamor potujete:")
        najbolsi_leti, link = naj_leti(kam, "LJU", 5)

        izbiralec.izpisi_podatke_o_letih(najbolsi_leti)
        Zapisi_naj_lete_v_dat(najbolsi_leti, link)

    if izbira == "5": #iskalnik letov iz bliznih letalisc
        kam = input("prosim vnesite ime letalisca kamor potujete (IATA letalisca):")
        letalisca_blizu = "LJU,ZAG,TRS,TSF,RJK" #tukaj sem raje sam podal najbolj smiselna letalisca, kot da more uporabnik iskati kratice vseh letalisc
        najbolsi_leti, link = naj_leti(kam, letalisca_blizu, 5)

        izbiralec.izpisi_podatke_o_letih(najbolsi_leti)
        Zapisi_naj_lete_v_dat(najbolsi_leti, link)
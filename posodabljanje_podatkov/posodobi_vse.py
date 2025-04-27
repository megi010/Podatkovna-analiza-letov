from posodabljanje_podatkov import evropa
from posodabljanje_podatkov import svet
from posodabljanje_podatkov import vsa_letalisca
import os

def posodobi_vse_podatke():
    """funkcija posodobi datoteke podatkov, oziroma ce teh ni naredi nove"""
    try:
        svet.posodobi_svet()
    except:
        print("prislo je do napake pri posodobljanju podatkov za podatki_svet.json")
    try:
        evropa.posodobi_evropo()
    except:
        print("prislo je do napake pri posodobljanju podatkov za podatki_evropa.json")

    #ker pridobivanje podatkov vseh letalisc porabi prevec requestov in se podatki letalisc naceloma ne spreminjajo prevec 
    #podatke posodobimo, le ce datoteka ne obstaja
    pot = os.path.join('Podatki', 'vsa_letalisca.json')
    if not os.path.exists(pot):
        vsa_letalisca.pridobi_pod_vseh_letalisc()
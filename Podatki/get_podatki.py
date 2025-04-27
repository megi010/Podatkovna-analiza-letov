import os
import json

def get_vsi_podatki():
    """funkcija zdruzene podatke iz podatki_svet.json in podatki_evropa.json"""
    pot = os.path.join('Podatki', 'podatki_svet.json')
    with open(pot, "r") as dat:
        podatki = json.load(dat)
    pot = os.path.join('Podatki', 'podatki_evropa.json')
    with open(pot, "r") as dat:
        podatki = podatki + json.load(dat)
    return podatki

def get_podatki_evrope():
    """funkcija zdruzene podatke iz podatki_evropa.json"""
    pot = os.path.join('Podatki', 'podatki_evropa.json')
    with open(pot, "r") as dat:
        podatki = json.load(dat)
    return podatki

def get_vsa_letalisca():
    """funkcija vrne seznam vseh letalisc iz datoteke vsa_letalisca.json"""
    pot = os.path.join('Podatki', 'vsa_letalisca.json')
    with open(pot, "r") as dat:
        podatki = json.load(dat)
    return podatki
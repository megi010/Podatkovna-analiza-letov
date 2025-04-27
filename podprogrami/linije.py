import json, random
from podprogrami.poizvedbe import poizvedbe
from Podatki import get_podatki
import matplotlib.pyplot as plt
import os

def graf_inenzitete_letov_na_letalsko_druzbo(podatki):
    """funkcija prejme podatke letov in nariše graf intenzitete letov vsake letalske druzbe, kjer ima vsaka letalska druzba svojo barvo"""
    data = poizvedbe(podatki)
    data_letalisca = get_podatki.get_vsa_letalisca()

    import geopandas
    import geodatasets
    fig, ax = plt.subplots()
    path = geodatasets.get_path("naturalearth.land")
    df = geopandas.read_file(path)
    ax = df.plot(ax=ax, figsize=(10, 10), alpha=0.5, edgecolor="k") #ax=ax da ne naredi novega okna

    poti = {}
    for let in data.get_data():
        letalisce1 = let["departure"]["airport"]
        letalisce2 = let["arrival"]["airport"]
        letalska_druzba = let["airline"]["name"]
        try:
            pot = tuple(sorted([letalisce1,letalisce2])+ [letalska_druzba]) #sortiramo da stejemo povezave iz x->y enako kot x<-y 
        except:
            print("========",letalisce1,"<->",letalisce2,f"[{letalska_druzba}]","========")
            continue
        if pot in poti:
            poti[pot] += 1
        else:
            poti[pot] = 1

    najvec_letov = max(poti.values())

    rgb_letalske_druzbe = {}
    for let in data.get_data():
        letalska_druzba = let["airline"]["name"]
        rgb = (random.random(), random.random(), random.random())
        if rgb not in rgb_letalske_druzbe.values():
            rgb_letalske_druzbe[letalska_druzba] = rgb

    for letalisca, stevilo in poti.items():
        xi = []
        yi = []
        letalisce1, letalisce2, letalska_druzba = letalisca
        letalisca = (letalisce1, letalisce2)
        for letalisce in letalisca:
            xi = xi + [float(x["longitude"]) for x in data_letalisca if x["airport_name"]==letalisce]
            yi = yi + [float(x["latitude"]) for x in data_letalisca if x["airport_name"]==letalisce]
            

        intenz = stevilo/najvec_letov
        r, g, b = rgb_letalske_druzbe[letalska_druzba]
        if intenz > 0.1:
            ax.plot(xi,yi, color = (r,g,b,intenz))
            
    ax.set_title("Graf letov letalskih družb")
    plt.show()

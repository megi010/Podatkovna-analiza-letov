import json
import matplotlib.pyplot as plt
import time
import os


#pot = os.path.join('Podatki', 'vsi_podatki.json')
def graf_st_letov_na_letalsko_druzbo(data):
    """funkcija prejme podatke letov in narise graf koliko letov je opravila posamezna letalska druzba"""

    n = len(data)
    airlines = {}
    for let in data:
        airline = let["airline"]
        if airline:
            airline_name = airline["name"]
            if airline_name in airlines:
                airlines[airline_name] += 1
            else:
                airlines[airline_name] = 1
        else:
            if "None" in airlines:
                airlines["None"] += 1
            else:
                airlines["None"] = 1


    if None in airlines:
        ni_podatka = round((airlines[None]/n)*100, 1)
        print(f"Ni podatka za približno {ni_podatka}% vseh letov!")
    airlines.pop(None, None)
    airlines = dict(sorted(airlines.items(), key=lambda item: item[1], reverse=True))

    #odstranimo letalske druzbe ki imajo manj kot 20 letov
    sestevek = sum(airlines.values())
    ostalo = [x for x in airlines.values() if x < 20]
    st_odstranjenih = len(ostalo)
    ostalo = sum(ostalo)
    y_tab = list(airlines.values())[0:-st_odstranjenih] #+ [ostalo]
    x_tab = list(airlines.keys())[0:-st_odstranjenih] #+ ["ostalo"]


    plt.figure(num = "Graf stevila letov na letalsko družbo",figsize=(20, 8))
    plt.bar(x_tab, y_tab, color='b', edgecolor='w', width=1, linewidth=1)
    plt.xticks(rotation=90, fontsize=8)
    plt.title("Letalske družbe")
    plt.ylabel("število letov")
    plt.show()


    airline_max = max(airlines, key=airlines.get)
    procenti = round((airlines[airline_max] / sum(airlines.values()))*100, 1)
    print(f"Največ letov je bilo opravljeno z {airline_max} ({airlines[airline_max]}), kar je {procenti}% vseh letov, ki imajo na voljo podatek.")
    print(f"https://www.google.com/search?sca_esv=36d1bc09254dbabd&sxsrf=AHTn8zqsK7K3tqIs91PS6nACzIEe8qBn1w:1743290931587&q=aircraft+iata+code+{airline_max}&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0")

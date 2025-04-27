
import matplotlib.pyplot as plt

def najpodostejse_letalo(data):
    """funkcija izpiše najbolj uporabjeno letalo glede na vnešene podatke"""

    n = len(data)
    aircrafts = {}
    for let in data:
        aircraft = let["aircraft"]
        if aircraft:
            aircraft = aircraft["iata"]
            if aircraft in aircrafts:
                aircrafts[aircraft] += 1
            else:
                aircrafts[aircraft] = 1
        else:
            if "None" in aircrafts:
                aircrafts["None"] += 1
            else:
                aircrafts["None"] = 1

    if "None" in aircrafts:
        ni_podatka = round((aircrafts["None"]/n)*100, 1)
        print(f"Ni podatka za približno {ni_podatka}% vseh letov!")
    aircrafts.pop("None", None)


    aircraft_max = max(aircrafts, key=aircrafts.get)
    procenti = round((aircrafts[aircraft_max] / sum(aircrafts.values()))*100, 1)
    print(f"Največ letov je bilo opravljeno z {aircraft_max} ({aircrafts[aircraft_max]}), kar je {procenti}% vseh letov, ki imajo na voljo podatek.")
    print(f"https://www.google.com/search?sca_esv=36d1bc09254dbabd&sxsrf=AHTn8zqsK7K3tqIs91PS6nACzIEe8qBn1w:1743290931587&q=aircraft+iata+code+{aircraft_max}&udm=2&fbs=ABzOT_CWdhQLP1FcmU5B0")

def graf_najpogostejsih_letal_torta(data, najmansa_meja = 5):
    """funkcija prejme podatke letov in nariše torni graf najbolj pogosto uporabljenih letal"""
    n = len(data)
    aircrafts = {}
    for let in data:
        aircraft = let["aircraft"]
        if aircraft:
            aircraft = aircraft["iata"]
            if aircraft in aircrafts:
                aircrafts[aircraft] += 1
            else:
                aircrafts[aircraft] = 1
        else:
            if "None" in aircrafts:
                aircrafts["None"] += 1
            else:
                aircrafts["None"] = 1

    if "None" in aircrafts:
        ni_podatka = round((aircrafts["None"]/n)*100, 1)
        print(f"Ni podatka za približno {ni_podatka}% vseh letov!")
    aircrafts.pop("None", None)

    ostalo = 0
    labels = []
    sizes = []
    for ime, st in aircrafts.items():
        aircraft_max = max(aircrafts, key=aircrafts.get)
        procenti = round((aircrafts[ime] / sum(aircrafts.values()))*100, 1)
        if procenti < najmansa_meja:
            ostalo += procenti
        else:
            labels.append(ime)
            sizes.append(st)
    labels.append("ostalo")
    sizes.append(ostalo)

    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']  # Distinct colors for each category

    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

    plt.title('Najpogostejše uporabljena letala')

    plt.axis('equal')  
    plt.show()
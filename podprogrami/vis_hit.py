import json
import matplotlib.pyplot as plt
import os

def graf_hitrosti(data):
    """prejme podatke letov in narise graf povprecne hitrosti"""

    visina = []
    hitrost = []
    for let in data:
        if let["live"]:
            hitrost.append(let["live"]["speed_horizontal"])
            visina.append(let["live"]["altitude"])

    povp_visina = sum(visina) / len(visina)
    povp_hitrost = sum(hitrost) / len(hitrost)
    print(f"{int(povp_hitrost)} km/h")
    print(f"{int(povp_visina)} km")
    fig = plt.figure()

    plt.scatter(hitrost, visina, s=3)
    plt.xlabel("Hitrost (knots)")
    plt.ylabel("Višina (ft)")
    plt.title("Graf povprečnih hitrosti")
    plt.show()
#import koordinate_iata as coord_iata
import requests, json
import os



def posodobi_evropo(evropa_iata = ["STN", "MAN", "CPH", "PMI", "DME", "ORY", "VKO", "AYT", "PRG", "LED"]):
    """funkcija prejme iata id letalisc in posodobi podatki_evropa.json z leti iz teh letalisc
    opomba: letov je prevec in smo z zastonj uporabniskem racunu zelo omejeni zato ne dobimo vheh podatkov
    """
    novi_podatki = []
    for letalisce in evropa_iata: #Pridobivanje podatkov 
        params = {"access_key": "62905fc234eca138b48941106dcc9e98", "dep_iata": letalisce}
        res = requests.get("https://api.aviationstack.com/v1/flights", params=params)
        podatki = res.json()["data"]
        novi_podatki.extend(podatki)

    #pridobimo že obstoječe podatke
    pot = os.path.join('Podatki', 'podatki_evropa.json')
    try:
        with open(pot, "r") as dat:
            content = dat.read().strip()
            obstojeci_podatki = json.loads(content) if content else []
    except (FileNotFoundError, json.JSONDecodeError):
        obstojeci_podatki = []
    obstojeci_podatki.extend(novi_podatki)

    with open(pot, "w") as dat:
        json.dump(obstojeci_podatki, dat, ensure_ascii=False, indent=2)

    print("Nalaganje podatkov je končano!")
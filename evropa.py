import koordinate_iata as coord_iata
import requests, json


evropa_iata = ["STN", "MAN", "CPH", "PMI", "DME", "ORY", "VKO", "AYT", "PRG", "LED"]
novi_podatki = []
for letalisce in evropa_iata: #Pridobivanje podatkov 
    params = {"access_key": "62905fc234eca138b48941106dcc9e98", "dep_iata": letalisce}
    res = requests.get("https://api.aviationstack.com/v1/flights", params=params)
    podatki = res.json()["data"]
    novi_podatki.extend(podatki)

#pridobimo že obstoječe podatke
try:
    with open("podatki_evropa.json", "r") as dat:
        content = dat.read().strip()
        obstojeci_podatki = json.loads(content) if content else []
except (FileNotFoundError, json.JSONDecodeError):
    obstojeci_podatki = []
obstojeci_podatki.extend(novi_podatki)

with open("podatki_evropa.json", "w") as dat:
    json.dump(obstojeci_podatki, dat, ensure_ascii=False, indent=2)

print("Nalaganje podatkov je končano!")
import requests
import json
import os

def pridobi_pod_vseh_letalisc():
    """
    funkcija, ki prenese informacije vseh letalisc iz aviationstack.com,
    ter jih shrani v datpteko vsa_letalisca.
    Podatke shranimo, ker je za vsa letalisce potrebno uporabiti 66 requestov (na voljo jim imamo 100)
    """

    key = "dac4581eb8885686f5477fb21606b6e8"

    offset = 0
    total = 1
    data = []
    while offset < total:
        url = f"https://api.aviationstack.com/v1/airports?access_key={key}&offset={offset}"
        response = requests.get(url).json()
        offset = response["pagination"]["offset"]
        total = response["pagination"]["total"]
        offset += 100

        data = data + response["data"]

    pot = os.path.join('Podatki', 'vsa_letalisca.json')
    with open(pot, "w") as dat:
        json.dump(data, dat)
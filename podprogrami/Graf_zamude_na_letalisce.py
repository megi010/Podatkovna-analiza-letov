import matplotlib.pyplot as plt
from podprogrami.poizvedbe import poizvedbe
import geopandas
import geodatasets
from Podatki import get_podatki


##graf letalisc in povprecnih zamud na letalisce
def graf_zamude_letalisc(podatki):
    """funkcija prejme podatke letov in vrne graf poprecne zamude na letalisce"""
    data = poizvedbe(podatki)
    data_letalisa = get_podatki.get_vsa_letalisca()

    #grupiramo podatke po letaliscih
    data_po_letaliscih = data.get_grouped_data(["departure","airport"])
    tabela_zamud_po_letaliscih = []
    for letalisce, leti in data_po_letaliscih.items():
        zamudniki = poizvedbe.get_zamudniki_ob_odhodu(leti)
        vsota_zamud = sum([x["departure"]["delay"] for x in zamudniki])
        povp_zamuda = vsota_zamud/len(leti)

        try:
            tabela_zamud_po_letaliscih.append([[float(x["longitude"]) for x in data_letalisa if x["airport_name"]==letalisce][0],
                                        [float(x["latitude"]) for x in data_letalisa if x["airport_name"]==letalisce][0],
                                        povp_zamuda])
        except:
            pass

    ##graf gostote zamujanja po letaliscih

    fig, ax = plt.subplots()
    plt.close('all') #cudn popravek da zapre ekstra okenjce ki ga subplots odpre avtomatsko

    #background
    path = geodatasets.get_path("naturalearth.land")
    df = geopandas.read_file(path)
    ax = df.plot(figsize=(10, 10), alpha=0.5, edgecolor="k")

    #foregtound
    tab_x = [x[0] for x in tabela_zamud_po_letaliscih]
    tab_y = [x[1] for x in tabela_zamud_po_letaliscih]
    skalar = 30 #za povecavo poprecja zamud na grafu
    tab_povpzamuda = [x[2]*skalar for x in tabela_zamud_po_letaliscih]

    ax.scatter(tab_x, tab_y, s=tab_povpzamuda, c="red", alpha = 0.3,edgecolors=None)
    ax.scatter(tab_x, tab_y, s=15, c="blue")

    ax.set_title("Graf povprečnih zamud letališč")
    plt.show()

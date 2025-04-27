from podprogrami.poizvedbe import poizvedbe
from Podatki import get_podatki
##graf letalisc in povprecnih zamud na letalisce

def graf_prometa_in_zamud(podatki):
    """funkcija prejme podatke letov in nariše graf intenzitete prometa med letalisci in poprecne zamude glede na letalisce"""
    data = poizvedbe(podatki)
    data_letalisa = get_podatki.get_vsa_letalisca()

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

    #print(tabela_zamud_po_letaliscih) 
    #graf gostote zamujanja po letaliscih
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()


    #background
    import geopandas
    import geodatasets
    path = geodatasets.get_path("naturalearth.land")
    df = geopandas.read_file(path)
    ax = df.plot(ax=ax, figsize=(10, 10), alpha=0.5, edgecolor="k") #ax=ax da ne naredi novega okna


    #povezave
    slovar_poti = dict()
    #naredimo slovar {(letalisce1, letalisce2) : stevil letov med njima}
    for let in data.get_data():
        letalisce1 = let["departure"]["airport"]
        letalisce2 = let["arrival"]["airport"]
        try:
            pot = tuple(sorted([letalisce1,letalisce2])) #sortiramo da stejemo povezave iz x->y enako kot x<-y 
        except:
            print("========",letalisce1,letalisce2,"========")
            continue
        if pot in slovar_poti:
            slovar_poti[pot] += 1
        else:
            slovar_poti[pot] = 1

    najvec_letov  = max(slovar_poti.values())

    for letalisca, stevilo in slovar_poti.items():
        xi = []
        yi = []
        for letalisce in letalisca:
            xi = xi + [float(x["longitude"]) for x in data_letalisa if x["airport_name"]==letalisce]
            yi = yi + [float(x["latitude"]) for x in data_letalisa if x["airport_name"]==letalisce]
            

        intenz = stevilo/najvec_letov
        if intenz > 0.1:
            ax.plot(xi,yi, color = (0,0,0.6,intenz))
    #print(slovar_poti.items())
    #foreground
    tab_x = [x[0] for x in tabela_zamud_po_letaliscih]
    tab_y = [x[1] for x in tabela_zamud_po_letaliscih]
    skalar = 30 #za povecavo poprecja zamud na grafu
    tab_povpzamuda = [x[2]*skalar for x in tabela_zamud_po_letaliscih]

    ax.scatter(tab_x, tab_y, s=tab_povpzamuda, c="red", alpha = 0.3,edgecolors=None, vmin=0, vmax=100)
    ax.scatter(tab_x, tab_y, s=15, c="blue", vmin=0, vmax=100)

    ax.set_title("Graf povprečnih zamud in intenzitet letov med letališči")
    plt.show()
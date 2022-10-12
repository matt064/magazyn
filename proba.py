import csv

items = ['Trimble_R2', 'Trimble_R8', 'Leica_ATX_1230', 'Leica_NA520']

items_dict = {
        'Trimble_R2' : {
        'type': 'gps',
        'quantity': 3,
        'unit_price': 28_000,
        }, 
    'Trimble_R8' : {
            'type' : "gps",
            'quantity' : 5,
            'unit_price' : 14_000,
        }, 
    'Leica_ATX_1230' : {
            'type': "gps",
            'quantity': 2,
            "unit_price" : 5_000,
        }, 
    'Leica_NA520' : {
            'type': "niwelator",
            "quantity" : 6,
            "unit_price" : 6_500,
        },
}



with open("stan_magazynu.csv",'w',) as csvfile:
    fieldnames = []
    lista_typ = []
    lista_quantity = []
    lista_cena = []

    for k, v in items_dict.items():
        fieldnames.append(k)
        lista_typ.append(v['type'])
        lista_quantity.append(v['quantity'])
        lista_cena.append(v['unit_price'])
      
    
    csvwriter = csv.writer(csvfile)

    for n in range(fieldnames.__len__()):
        csvwriter.writerow([fieldnames[n], lista_typ[n], lista_quantity[n],lista_cena[n]])


    #print(fieldnames)
    #print(lista_typ)
    #print(lista_quantity)









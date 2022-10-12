import csv


user_choice = -1
#lista produktów
#items = ['Trimble_R2', 'Trimble_R8', 'Leica_ATX_1230', 'Leica_NA520',]
sold_items = {}

#slownik produktów
items_dict = {
        'Trimble R2' : {
        'type': 'gps',
        'quantity': 3,
        'unit_price': 28_000,
        }, 
    'Trimble R8' : {
            'type' : "gps",
            'quantity' : 5,
            'unit_price' : 14_000,
        }, 
    'Leica ATX 1230' : {
            'type': "gps",
            'quantity': 2,
            "unit_price" : 5_000,
        }, 
    'Leica NA520' : {
            'type': "niwelator",
            "quantity" : 6,
            "unit_price" : 6_500,
        },
}



def get_items():
    """wyświetla produkty w magazynie"""  #gotowe!!!
    print("Name\t\tType\t\tQuantity\tUnit_price")
    print("----\t\t----\t\t--------\t----------")
    for nazwa, info in items_dict.items():
        if info['type'] == 'niwelator':
            print(nazwa + "\t" + info['type'] + "\t" + str(info["quantity"]) + "\t\t" + str(info["unit_price"]))
        else:
            print(nazwa + "\t" + info['type'] + "\t\t" + str(info["quantity"]) + "\t\t" + str(info["unit_price"]))

def add_item():
    """dodaje nowy produkt do magazynu""" 
    new_item = input("Podaj nazwe produktu, ktory chcesz wprowadzic do bazy: ")
    type = input("Podaj typ produktu: ")
    quantity = int((input("Podaj ilość wprowadzanego produktu: ")))
    unit_price = int((input("Podaj cene jednostkowa: ")))
    
    
    items_dict.setdefault(new_item,{'type': type,'quantity': quantity,'unit_price': unit_price})
    print("Produkt wprowadzony")
    return items_dict

def sell_item():  # dodac blad gdy wprowadzi sie wartosc inna niz w zbiorze
    "usuwa produkt z listy"
    delete_item = input("Wprowadź nazwe produktu, ktory chcesz sprzedac: ")
    piece_of_product = int(input("Podaj ile sztuk produktu chcesz sprzedac: "))

    if delete_item in items_dict.keys():
        items_dict[delete_item]['quantity'] = items_dict[delete_item]['quantity'] - piece_of_product
        if items_dict[delete_item]['quantity'] == 0:
            del items_dict[delete_item]
        elif items_dict[delete_item]['quantity'] < 0:
            print("Wprowadzona ilość sztuk do sprzedazy jest wieksza niz posiadana w magazynie! Operacja nieudana.")
        else:
            sold_items[delete_item] = items_dict[delete_item].copy()
            sold_items[delete_item]['quantity'] = piece_of_product

    return items_dict, sold_items

def get_costs():
    """zlicza wartosc przedmiotow w magazynie"""
    lista_wartosci = []
    for name in items_dict.keys():
        wartosc = items_dict[name]['quantity'] * items_dict[name]['unit_price'] 
        lista_wartosci.append(wartosc)
    calkowita_wartosc = sum(lista_wartosci)
    return calkowita_wartosc
    #print("Wartosc produktów w magazynie wynosci:", calkowita_wartosc)

def get_income():
    """zlicza wartosc sprzedanych produktow"""
    lista_sprzedazy = []
    for name in sold_items.keys():
        wartosc = sold_items[name]['quantity'] * sold_items[name]['unit_price']
        lista_sprzedazy.append(wartosc)
    suma_sprzedaz = sum(lista_sprzedazy)
    return suma_sprzedaz
    #print("Zysk ze sprzedazy wynosci:", suma_sprzedaz)

def show_revenue():
    wartosc_magazynu = get_costs()
    wartosc_sprzedazy = get_income()

    print("Wartość produktów w magazynie wynosi:", wartosc_magazynu,"[PLN]")
    print("Zysk ze sprzedanych produktów wynosi:", wartosc_sprzedazy,"[PLN]")

    bilans =  wartosc_sprzedazy - wartosc_magazynu
    print("Bilans (wartosc ze sprzedanych produktów - koszt ich zakupu) wynosi:", bilans,"[PLN]")

def export_items_to_csv():
    """exportuje stan magazynu do pliku"""
    with open("stan_magazynu.csv",'w',newline='') as csvfile:
        names = []
        lista_typ = []
        lista_quantity = []
        lista_cena = []

        for k, v in items_dict.items():
            names.append(k)
            lista_typ.append(v['type'])
            lista_quantity.append(v['quantity'])
            lista_cena.append(v['unit_price'])
      
    
        csvwriter = csv.writer(csvfile)

        for n in range(names.__len__()):
            csvwriter.writerow([names[n], lista_typ[n], lista_quantity[n],lista_cena[n]])


def export_sales_to_csv():
    """eksportuje sprzedane produkty do pliku"""
    with open("sprzedane_produkty.csv",'w',newline='') as csvfile:
        names = []
        lista_typ = []
        lista_quantity = []
        lista_cena = []

        for k, v in sold_items.items():
            names.append(k)
            lista_typ.append(v['type'])
            lista_quantity.append(v['quantity'])
            lista_cena.append(v['unit_price'])
      
    
        csvwriter = csv.writer(csvfile)

        for n in range(names.__len__()):
             csvwriter.writerow([names[n], lista_typ[n], lista_quantity[n],lista_cena[n]])






print()
print("Witaj! Oto program do obslugi twojego magazynu.")
print()

while True:
    if user_choice == "1":
        get_items()
    
    if user_choice == "2":
        add_item()
    
    if user_choice == "3":
        sell_item()

    if user_choice == "4":
        show_revenue()
    
    if user_choice == "5":
        export_items_to_csv()
        export_sales_to_csv()
        
    if user_choice == 'exit':
        print("Zamykam program, do widzenia.")
        break
    
    print()
    print("Menu: ")
    print("1. Wyświetl produkty w magazynie ")
    print("2. Dodaj produkt do magazynu.")
    print("3. Sprzedaż towaru z magazynu.")
    print("4. Bilans zysków i kosztów")
    print("5. Zapisz ")


    print("(możesz wyjsc z programu w każdym momencie, wpisując 'exit')")
    user_choice = input("Wybierz co chcesz zrobic, podając liczbe z menu: ")
        
    print()



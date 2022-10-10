user_choice = -1
#lista produktów
items = ['Trimble_R2', 'Trimble_R8', 'Leica_ATX_1230', 'Leica_NA520',]
sold_items = {}

#slownik produktów
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
    quantity = (input("Podaj ilość wprowadzanego produktu: "))
    unit_price = (input("Podaj cene jednostkowa: "))
    
    items.append(new_item)
    items_dict.setdefault(new_item,{'type': type,'quantity': quantity,'unit_price': unit_price})
    print("Produkt wprowadzony")
    return items

def sell_item():  # dodac blad gdy wprowadzi sie wartosc inna niz w zbiorze
    "usuwa produkt z listy"
    delete_item = input("Wprowadź nazwe produktu, ktory chcesz sprzedac: ")
    piece_of_product = int(input("Podaj ile sztuk produktu chcesz sprzedac: "))

    if delete_item in items_dict.keys():
        items_dict[delete_item]['quantity'] = items_dict[delete_item]['quantity'] - piece_of_product
        if items_dict[delete_item]['quantity'] == 0:
            items.remove(delete_item)
            del items_dict[delete_item]
        elif items_dict[delete_item]['quantity'] < 0:
            print("Wprowadzona ilość sztuk do sprzedazy jest wieksza niz posiadana w magazynie! Operacja nieudana.")

    sold_items = items_dict[delete_item].copy

    return items_dict, sold_items



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
        print(sold_items)
    
    if user_choice == 'exit':
        print("Zamykam program, do widzenia.")
        break
    
    print()
    print("Menu: ")
    print("1. Wyświetl produkty w magazynie ")
    print("2. Dodaj produkt do magazynu.")
    print("3. Sprzedaż towaru z magazynu.")
    print("4. Lista sprzedanych produktów")


    print("(możesz wyjsc z programu w każdym momencie, wpisując 'exit')")
    user_choice = input("Wybierz co chcesz zrobic, podając liczbe z menu: ")
        
    print()



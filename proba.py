
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
"""
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
"""
sold_items = {}
delete_item = input("wprwadz nazwe")
piece_of_product = 2


sold_items[delete_item] = items_dict[delete_item].copy()
#sold_items[delete_item]['quantity'] = piece_of_product


print(sold_items[delete_item])










# def get_costs():
#     """zlicza wartosc przedmiotow w magazynie"""
#     lista = []
#     for name in items_dict.keys():
#         wartosc = items_dict[name]['quantity'] * items_dict[name]['unit_price'] 
#         print(wartosc)
#         lista.append(wartosc)
#     suma = sum(lista)
#     print(suma)


        
# get_costs()
# #print(wartosc)
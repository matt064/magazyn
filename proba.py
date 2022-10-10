
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

sold_items = {}
sold= 'Trimble_R2'
piece = 2


sold_items[sold] = items_dict[sold].copy()
#sold_items['quantity'] = piece

print(sold_items)

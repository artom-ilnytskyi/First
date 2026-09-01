def house_price(rooms, height, width, age):
    a =(rooms * 500 + height * 1000 + width * 200)
    if age < 5:
        final = a
    elif age <= 10:
        final = a * 0.95
    else:
        final = a * 0.90
    return(f"your house cost {final:.2f} dollars")
all_houses = [[ 2, 2, 8, 3
], [3, 3, 8, 7
], [5, 3, 15, 15
]
]
for house in all_houses:
    rooms, height, width, age = house
    final_cost = (house_price(rooms, height, width, age))
    print(final_cost)

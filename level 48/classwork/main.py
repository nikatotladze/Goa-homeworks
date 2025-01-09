#1

table = {
    "type": "furniture",
    "material": "wood",
    "color": "brown",
    "shape": "rectangular",
    "dimensions": {"length": 120, "width": 60, "height": 75},
    "has_drawers": True
}

#2


table = {
    "type": "furniture",
    "material": "wood",
    "color": "brown",
    "shape": "rectangular",
    "dimensions": {"length": 120, "width": 60, "height": 75},
    "has_drawers": True
}


print("Keys:")
for key in table:
    print(key)


#3


table = {
    "type": "furniture",
    "material": "wood",
    "color": "brown",
    "shape": "rectangular",
    "dimensions": {"length": 120, "width": 60, "height": 75},
    "has_drawers": True
}


print("Values:")
for value in table.values():
    print(value)


#4


table = {
    "type": "furniture",
    "material": "wood",
    "color": "brown",
    "shape": "rectangular",
    "dimensions": {"length": 120, "width": 60, "height": 75},
    "has_drawers": True
}


print("Keys and Values:")
for key, value in table.items():
    print(f"{key}: {value}")

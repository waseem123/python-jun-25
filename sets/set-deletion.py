myset = {'Scanner', 'RAM', 'CPU', 'Barcode reader', 'Monitor', 'SSD', 'Mouse', 'USB', 'Keyboard', 'Printer'}
print(myset)

# myset.pop()
# print(myset)

myset.remove('Mouse')
print(myset)

myset.discard('Charger')
print(myset)

# del myset[2]
myset.clear()
print(myset)

del myset
print(myset)
shopping_list = ['pienas', 'kiausiniai', 'duona', 'sviestas']
#1 sarasas
print(shopping_list)
#pirmas saraso elementas
print(shopping_list[0])

#randu duonos indexa
duonos_vieta = shopping_list.index('duona')

#pakeiciu duona i banana
shopping_list[duonos_vieta] = 'bananas'
print(shopping_list)

#pridedu obuoli i pradzia
shopping_list.insert(0, 'obuolys')
print(shopping_list)

#pridedu miltus ir cukru
shopping_list.append('miltai')
shopping_list.append('cukrus')
print(shopping_list)

print(shopping_list[2:4])
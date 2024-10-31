# python has 4 types of collections
# Tuple
# Set
# List
#Dictionary

# A list is a way to store more than one value in a single variable
# thoes values in the list are called ITEMS
# ITEMS can be accesed by their index (position on list)
# INDEX                    0                      1            2                  3
best_elden_ring_wepons = ["Blasphemous blade" , "moonveil" , "rivers of blood" , "iron ball" , "bloodhound's fang"]

#INDEX         0     1     2     3
best_years = [1776, 1985, 1994, 1957]

#Print the index of the value in the in the list
print(best_years.index(1985))

print(best_elden_ring_wepons [0])

print(best_elden_ring_wepons[len(best_elden_ring_wepons) -1])

# List items can be change
best_elden_ring_wepons[3] = "spiked fist"
print(best_elden_ring_wepons)

# Remove the last item on the list by its position
#the .pop() function removes an item by its position in the list
best_elden_ring_wepons.pop(4)

#remove by its value
best_elden_ring_wepons.remove("moonveil")


#Add a new item to the end of the list
best_elden_ring_wepons.append("mohgwyn's sacred spear")
print(best_elden_ring_wepons)

import random
numbers = [random.randint(1,100)]
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)
#Strings are just a list of characters
word = "potato"
print(word[0])
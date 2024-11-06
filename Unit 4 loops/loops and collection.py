#python has four thypes of collections 
#tuple
#Set
#list 
#Dictionary 

#today,were going to focus on listssssssssssssssssssssssssssssss
# A list is a way to store more than one value in a simgle variavle 
#those valuves om the ;ost are called items
#items can be accessed by their index ( position in the list)
# INDEX                      0                   1               2               3        
best_elder_ring_weapons = ["Blasphemous Blade","Moonveil","Rivers of blood", "Iron Ball" , "Bloodhound's Fang"]

#INDEX         0      1     2     3 
best_years = {1776, 1985, 1994, 1957}

print(best_years.index(1776))
# Print the besy elder ring weapons 
print (best_elder_ring_weapons [0])
#print (best_elder_ring_weapons[len(best_elder_ring_weapons)] it wont work 
#print(best_elder_ring_weapons[len(best_elder_ring_weapons)-1]) will work 
# print worset of the best elden ring weapon
best_elder_ring_weapons[3] = "spiked Fist "
print (best_elder_ring_weapons)
#Strings are lists!
#Strings are just a list of characcters
word = "potato"
print(word[0])


#remove the Last item in the list by its position in the list 
#The .pop() function removes an item in a list by its position in the list 
best_elder_ring_weapons.remove("mooonveil")
print(best_elder_ring_weapons)

#add a new item to the end of a list
best_elder_ring_weapons.append("mohgwyn's Sacred Spear")
print(best_elder_ring_weapons)

#Strings are lists!
#Strings are just a list of characters 

import random
numbers = [random.randint(1,100) , random.randint (1,100),  random.randint (1,100), random.randint (1,100), random.randint (1,100)]
print(numbers)
print (max(numbers))
print(min(numbers))
print(numbers.soft())
word = "potato"
print(word[0])
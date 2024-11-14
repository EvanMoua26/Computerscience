#loops control statement
#Allow you to change how loops operators
#D othings like quit the loop early, skip the current loop, and even do nothing 
#break,contine, and pass 

#break
#exists a loop prematurely,before it was supooed to end 

# EX

bag_of_fruit= ["Apple ," "orange" ,"Strawbery"  "watermeolon" , "pear"]

for fruit in bag_of_fruit:

     if fruit == "bug":
          print("uh oh. you found a bug in the bag...")
          break # the break statement exits the loops immediately and continues 
     else:
          print("you ate a " + fruit)




orders = [15,30,35 ,23,100, 3, 10, 22 ]

for order in orders:
     if order <20: 
          continue
     print("$" + str(order) + " order discounted 5% to $ + " + str(order * 0.95))


  
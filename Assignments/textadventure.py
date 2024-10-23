#Horror
#Whispers in the Shadows
#Police station 
def start_adventure():
    print("you saw a abandoned police station and decide to stand outside of the entrance of the dark police stand and takes a picture Do you:")
     
    print("1. leave the police station and go back home")
    print("2. enter the police station")

    choice = input()
 
    if choice == "1":
     Leave_the_police_station_and_Go_home()
    elif choice =="2":
     Enter_the_police_station()
    else:
      print("Invalid choice. Try again") 
      start_adventure

    

def Enter_the_police_station():
    print("You have step inside the police station and you look around for some ways to help you see in the dark")
 
    print ("do you go and look behind the counter to see if theres anything you can use to help you?")
    print ("do you want check the break room if there anything in there") 
    print ("do you want to check the weapon rooms and see if there ")
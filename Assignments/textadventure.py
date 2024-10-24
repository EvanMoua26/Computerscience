#Horror
#Whispers in the Shadows
#Police station 

("Whispers Is The Shadows\n")
input.title()
def intro():
    print("you have wonder around that what uses to be Coastedge, looking for what still left and checking if you can keep anything for yourself but than you spot a abandoned police station and you were suprise its still in a good shape, so you decide to stand outside of the entrance of the dark police stand and decided to take a picture.")

def first_choice():
    print("Go inside")
    print("leave the police station")
    choice = input("what are you going to do ??)").lower()
    if choice == "Go_inside":
     Go_inside()
    elif choice: == "leave the Police station":
   leave_the_Police_station()
    else: 
    print("invald choice. please choose 'Go inside' or 'leave the police station'.")
    first_choice()

def Go_inside():
   print (" you have enter the police station and its to dark to even see whats going on")
   print ("\n you step into the left room. It's the waiting room.")
   print("you heard some rattling noise from some bag ")
   print("You can inverstiage the waiting room or go back to the counter ")
   choice == input ( "what do you do? (Investigate the waiting room or leave the room):").lower()

if choice == "inverstigate the waitting room":
    investigate_waiting_room()
elif choice == "leave": 
     first_choice()
else:
   print("Invalid choice. Please choose 'investigate the waiting room or leave room")
   















intro()

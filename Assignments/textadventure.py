#Horror
#Whispers in the Shadows
#Police station 









import random


def intro():
    print("you have wonder around that what uses to be Coastedge, looking for what still left and checking if you can keep anything for yourself but than you spot a abandoned police station and you were suprise its still in a good shape, so you decide to stand outside of the entrance of the dark police stand and decided to take a picture.")

def first_choice():
    print("You enter the dimly lit police station.")
    print("There are two doors: one on the left and one on the right.")
    choice = input("Which door do you choose? (left/right): ").lower()
    if choice == "left":
        left_room()
    elif choice == "right":
        right_room()
    else:
        print("Invalid choice. Please choose 'left' or 'right'.")
        first_choice()

def left_room():
    print("\nYou step into the left room. It's the waiting room.")
    print("Suddenly,  some rattling noise echo through the room.")
    print("You can waiting room or leave the room.")
    choice = input("What do you do? (investigate/leave): ").lower()
    
    if choice == "investigate":
        investigate_evidence()
    elif choice == "leave":
        first_choice()
    else:
        print("Invalid choice. Please choose 'investigate' or 'leave'.")
        left_room()

def investigate_evidence():
    print("\nYou search through the waiting roomand find a strange old case file.")
    print("As you read it, you heard a loud bang or cry, and you feel a cold breeze and feel like someone is watching you.")
    
    if random.choice([True, False]):
        print("A figure appears! It's looks like some blind long hand and cant see crying loud creature.")
        print("The creature slowly walks around the room trying to smell you out and crying its a way around trying to wait for you to make a noice ")
        escape()
    else:
        print("You can sneak out of the wall. ")
        print("if you do sneak out of the wall you will be safe .")
        choice = input("What do you do? try to leave where the  creature came from /leave through the wall): ").lower()
        
        if choice == "leave main door":
            Leave_from_where_the_creature_came_from()
        elif choice == "leave from the wall":
            first_choice()
        else:
            print("Invalid choice. Please choose 'leave through ' or 'leave from the wall'.")
            investigate_evidence()

def right_room():
    print("\nYou enter the right room. It's the interrogation room.")
    print("The walls are covered in eerie shadows.")
    print("You hear a loud bang and see a shadow dart across the room.")
    choice = input("Do you investigate the sound or leave the room? (investigate/leave): ").lower()
    
    if choice == "investigate":
        investigate_sound()
    elif choice == "leave":
        first_choice()
    else:
        print("Invalid choice. Please choose 'investigate' or 'leave'.")
        right_room()

def investigate_sound():
    print("\nYou cautiously approach the source of the sound.")
    print("You find an old radio that suddenly turns on, playing a haunting melody.")
    
    if random.choice([True, False]):
        print("The radio crackles, and a ghostly voice tells you the truth about a hidden crime.")
        escape()
    else:
        print("The shadows coalesce into a ghostly figure!")
        print("It asks you to solve a riddle to escape.")
        riddle()

def riddle():
    print("\nThe ghost asks: 'I speak without a mouth and hear without ears. What am I?'")
    answer = input("Your answer: ").lower()
    
    if answer == "echo":
        print("The ghost smiles and allows you to escape! You have solved the riddle!")
        print("Congratulations! You've uncovered the mystery of the haunted police station.")
    else:
        print("The ghost is angry! You must run back to the main room.")
        first_choice()

def escape():
    print("\nYou decide to escape the station with the knowledge you've gained.")
    print("As you leave, you can feel the spirits of the station watching over you.")
    print("Congratulations! You've made it out alive!")

# Start the game
intro()
first_choice()







intro()

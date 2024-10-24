def intro():
    print("Welcome to the Haunted Police Station!")
    print("You are a detective investigating strange occurrences.")
    print("Rumors say the station is haunted by the spirits of unsolved cases.")
    print("Can you uncover the mystery and escape the station?")
    print()

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
    print("\nYou step into the left room. It's the evidence locker.")
    print("Suddenly, you hear whispers echoing through the room.")
    print("You can investigate the evidence or leave the room.")
    choice = input("What do you do? (investigate/leave): ").lower()
    
    if choice == "investigate":
        investigate_evidence()
    elif choice == "leave":
        first_choice()
    else:
        print("Invalid choice. Please choose 'investigate' or 'leave'.")
        left_room()

def investigate_evidence():
    print("\nYou search through the evidence and find a strange old case file.")
    print("As you read it, the lights flicker, and you feel a cold breeze.")
    
    if random.choice([True, False]):
        print("A ghostly figure appears! It's the spirit of a detective long gone.")
        print("He warns you to leave before it's too late!")
        escape()
    else:
        print("You find a clue that reveals the identity of the ghost!")
        print("You can now confront the spirit or leave.")
        choice = input("What do you do? (confront/leave): ").lower()
        
        if choice == "confront":
            confront_spirit()
        elif choice == "leave":
            first_choice()
        else:
            print("Invalid choice. Please choose 'confront' or 'leave'.")
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
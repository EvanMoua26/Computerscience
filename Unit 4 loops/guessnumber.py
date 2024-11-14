import random

guess = -1
number =random.randint(0,101)

while guess != number:
    guess = int(input("Whats your guess?\n>"))
    except:
    print("Hmm... That's not right")
    if guess > number:
      print("Too large, try again..")
    elif guess < number:
     print ("too small, try again")

else:
    print("Good job! the correct number was " + str(number))

print ("nice job") 
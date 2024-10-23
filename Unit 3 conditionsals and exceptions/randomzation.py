import random

r = random.randrange(0,10)
#0 is INCLUSIVE and the 10 us EXCLUSIVE 
#0 <= result <10
print(r)

p= random. random()
if p< 0.25:
    print("SuCCESS")

else:
    print("FAIL!")



# To use the random module, you first need to import it into your script:

#import random
#Generating Random Numbers
#The random module offers several ways to generate random numbers:

 #random.random():

 #This function returns a random float between 0.0 and 1.0.
 #print(random.random())  # Output: e.g., 0.56432
 #random.randint(a, b):

 # Generates a random integer between the specified range a and b (inclusive).
 # print(random.randint(1, 10))  # Output: e.g., 7 (a number between 1 and 10)
 # random.uniform(a, b):

 # Returns a random float between a and b.
 # print(random.uniform(5, 10))  # Output: e.g., 7.654 (a float between 5 and 10)
 #random.randrange(a, b):

 # Returns a random integer between a and b.
 # print(random.randrange(5, 10))  # Output: e.g., 9 (an integer between 5 and 10)
 #Random Choices from a List
 #The random module also provides functions to select random elements from a sequence like a list or tuple:

 #random.choice(sequence):

 #Selects and returns a random item from a non-empty sequence.
 #colors = ['red', 'blue', 'green', 'yellow']
 #print(random.choice(colors))  # Output: e.g., 'green'
 #random.choices(sequence, k=N):

 #Returns a list of N random elements from the sequence, with replacement (meaning elements can be repeated).
 #print(random.choices(colors, k=3))  # Output: e.g., ['blue', 'red', 'yellow']
 #random.sample(sequence, k=N):

 #Returns a list of N random elements from the sequence without replacement (meaning elements are unique).
 #print(random.sample(colors, k=2))  # Output: e.g., ['red', 'green']
 #Shuffling Data
 #You can use the shuffle() function to randomly reorder elements in a list.

 #deck = [1, 2, 3, 4, 5]
 #random.shuffle(deck)
 #print(deck)  # Output: e.g., [3, 1, 5, 2, 4]
 #This function shuffles the list in place, modifying the original sequence.

 #Seeding the Random Number Generator
 #By default, the random module generates pseudo-random numbers that are different each time the program runs. If you want the random numbers to be reproducible (e.g., for testing), you can use the random.seed() function.

 #random.seed(42)
 #print(random.random())  # Output: 0.6394267984578837
 #Setting the seed ensures that the random numbers generated will be the same each time you run the program with the same seed.
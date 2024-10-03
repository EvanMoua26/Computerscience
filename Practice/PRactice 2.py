def top_five_movies (movie1, movie2 ,movie3 ,movie4 ,movie5 ):     #Define a mew function  
    print("my top 5 favorite movie")    
    print("1. " + movie1)
    print("2. " + movie2)
    print("3. " + movie3)
    print("4. " + movie4)
    print("5. " + movie5)


def add(x,y):
    print(x,y)

num_1 = int(input("whats the first number?\n>"))
num_2 = int(input("What's the second number?\n>"))

x = 4   #Define GLOBAL VARIABLE X as 4 
def my_function():
    global x    #From now on, when I call x, I'm talking about the global version!! Not the local verison...
    x = 5       #Reassigning the global variable x
    print(x)    #Prints 5

my_function()       #print Glovak Variable X 
print(x)            #Run my_funtion
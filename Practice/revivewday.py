#2 functions
#EX: 
print("Hello World!")                   #Hello, World! is the Parameter
input("please enter your username\n>") # \n is called an escape character
#\n starts a new line(Linebreak)

# Variables
#Syntax 
#<name> = <value>
x = 5 

#Snake naming convebtion - all lowercase, underscore for spaces 
# Concise: Short and descriptive
username = "Evan"         #Define String
fav_animal = "Corgi"       #Define String
total_poptarts = 12        #Define integer ( Whole number)
percent_complete = 23.52  #Define float ( decimal number)
is_cool = True            # define Booleab ( True/False)
first_letter = 'c'         # Define Character (single symbol)

total_poparts = 8 # Reassign


#Arithmetic operators
# + _ * / ** % // 
print(4+4) #> 8
print("4" + "4") #> 44
print("cat" + "dog") #>catdog
print("cat" * 3) #>Catcatcat
print("cat"+ 3 ) #error: cannot use +for string and int

#make some working programs 
#1. add 2 number using input
x = input ("What is x?\n>")      #input ( always returns a string)
x = int(x)
#OR 
x = int(input("What is x?\n>"))         
y = input ("what is y?\n>")      #even if you type in a number
y = int (y)                      #Converst  from string to int
print (x+y)

#2. Converts celcius to farenheight
temp_celcius = 40
temp_farenheight = (temp_celcius * 1.8) + 32
print(temp_celcius + "degress c equals"  +  temp_farenheight + " degress f ")
# Or 
temo_celcius = input("What is the temperature in Celcius?\n>") 
temp_celcius = int(temp_celcius)
temp_farenheight = (temp_celcius * 1.8) + 32
print(temp_celcius + "degress c equals"  +  temp_farenheight + " degress f ")




#some conversion functions 
str()
int()
float()
bin()
bool()

# The stuff that goes between the parenthesis is called parameters 
#Parameters are the valuve that the funtcion needs to run



#Functions 
#function are a lot like variables 
# They have names
#they can be recalled from memory bu calling their name
#Store information 
def potato():       #Def keyword + name () + :
    print("potato") # lines indented underneath are "inside" the fuction
# function are not ran when they are defined
# They must be called by their name to run
potato()         #Every function call needs open and closed parenthesis
                # even if it has no parameters 

def jump (how_high):
    print("you jumpped" + str(how_high) + "inches!")
jump(14)
def make_a_word(a,b,c,d,e,f,g,h,):
    print (a+b+c+d+e+f+g+h,)
make_a_word ("E" ,"v" , "a ", "n", "M","o","u","a")

#Functions can have many lines
def top_ten_games():
    print("Injustice2" )
    print("Smash Bro ultimate")
    print("Apex legend")
    print ("Overwatch")
    print ("Minecraft")
    print("Last of us 1 and 2 ")
    print ("God of war all of them")
    print ("shadow of colossus")
    print("Final fansty ")
    print("Rachet & clank")

    #Scope: Global and local variables!!
    #Scope refers to the context in which the varivale was defined
    #Global - defined at no indentation level
    #local - defined inside of a function

    #Global varivales can be used anywhere
    todd = "cool guy"  # Global variable- no indentation level 

    #Local variables only exist in the scope they were defined
    def my_function():
        smith = "not cool guy" #Local varivale - define in a function
        todd = "Strange guy"  # Local variable even though it has the same name
        print(todd)         #Prints "strange guy" - Local variable
    #When you call a variable in a function
    # It searches local variable first, then globak variable 

#If you want to reassign a global variable inside of a function
def my_function2():
    global todd           #In this function, whenever i call todd
    # i mean the global todd, not the local
    todd = "strange guy" # Reassign todd - global
    print(todd)          #print todd - global

    #return functions 
    #Functions can alsoreturn vauves
    # The value that is returned is sent back to where the function was called 
    #This is very similar to how a variable works
    #the function does its work and returns an answer back
    def add2(x,y):
        return x + y #return the sum of x and y to where the function was called 
    add2 (2,10)       #does not print anything1 we never told it to print..


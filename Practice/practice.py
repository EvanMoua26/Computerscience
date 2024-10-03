x = 4   #Define GLOBAL VARIABLE X as 4 
def my_function():
    global x    #From now on, when I call x, I'm talking about the global version!! Not the local verison...
    x = 5       #Reassigning the global variable x
    print(x)    #Prints 5

my_function()        #Run my_funtion 
print(x)             #PRINT GLOBAL VARIable x 
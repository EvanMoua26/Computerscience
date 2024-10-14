# Exception Handling
# write a program that asks for two numbers and adds them

# if = try
# elif = except specific error type
#else = except
def divide_two_numbers():
    try:
      x = int(input("what the first number?\n>"))
      y = int(input( "whats the second number?\n>"))
      print(x / y )

    except ValueError:
      print("Please enter a number...")
      divide_two_numbers()
    
    except ZeroDivisionError:
       print("cannot divide a zero...")
       divide_two_numbers

 

divide_two_numbers()
#there are a couple types of loops in python 
attempts = 0

real_pass = "Why"
enter_pass = ""
attempts = attempts + 1 
# A while loops continunes looping until the condition is no lomger true 
while real_pass != enter_pass:
     enter_pass == input("Guess the number \n>")
     if enter_pass == real_pass:
          print("Access Granted")
     else:
          print("Access Denied")
          print("Try Again...")
          print(str(attempts) + "attempts.")
print("Welcome!")


print("")


 #count = 0 
 #while count:
#count += 1 
   #print(count)

   #print("All done ")

user_input =""

while user_input != "exit":
     user_input = input("enter something ( type 'exit ' to quit)")
     print("you enterd: " + user_input)
print( "All done")
    
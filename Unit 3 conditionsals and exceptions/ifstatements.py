# If statements evaluateboolean expressions
# make decisions about which code to run next

# take a temperature 
# Print "<temperature> is hot" if the temperature is >= 80 
# Otherwise, print "<temperature> is not hot"
temperature = input ( "what is the temperature?\n>")
temperature = int(temperature)
#if boolean exoeression :
# sort of like a function, no parenthesis! 
if temperature >= 80: # if the bool evaulate to true, go inside
   print("the temperature is " + str(temperature) + "degress.")
   print (str(temperature)  + " degres is hot")

else: # else takes no condition and runs when the if above is flase
# otherwise...
   print("the temperature is " + str(temperature) + "degress.")
   print(str(temperature) + "degrees is not hot")

   #complete the activity-
   #create a program that ask for a password
   #print "Access Granted" if the password is correct
   #print "Access Denied " if the passwor is wrong
   #The password is skibidi68

#Activity 
skibidi68 = input ( "what is the password?\n>")
real_password = "slibidi68"

if skibidi68 == real_password:
   print("Access Granted")

else:
   print("Access denined")

# Acivity 2, electric boogaloo
#create a five question quiz that prints your score at the end 
#Choose any five questions
# Ez

print(5)

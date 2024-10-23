# nested if statement
# you are a prime memer or order is at least $25
# you are at least 18 years old or have parent consent 

prime = True
cost = 20 
age = 17 
consent = False

if prime: 
    if age >= 18:
        print(" you are eligible for free shipping!")
    else:
        if consent:
            print(" you are eligiable for free shipping!")
        else:
            print(" you are not eligible for free shipping!")
elif cost >=25:
    if age>=18:
          print("you are eligible for free shipping !")
    elif consent:
        print(" you are eligble for free shipping!")
    else:
        print("you are not eligibe fore freee shipping!")
else:
    print("you are not eligible for free shipping!")
    
# so we need an umbrella?

# we need an umbrella if it is raining and we are outside
raining = True
outside = True

if raining: 
    if outside:
     print("bring an umbrella")

    else:
     print("Dont bring an umbrella")

else:
    print("dont bring an umbrella")
#Logical Operators and or !
# comparison operators > < == >= <=
# Arithmetic operrators + - / * % ** // 

def check_eligibility(age, exp):
    # you must be at least 18 years old and have 1 year of experience to be eligible
    if age >= 18 and exp >= 1:
        print("you are eligible for the competition!")
    elif age < 18:
        print("you are not old enough to compete.")
    elif exp < 1:
        print(" you dont have enough experience to compete.")
    
a = int(input("how old are you?\n"))
e = int(input("how many years of experience do you have?\n"))
check_eligibility(a,e)
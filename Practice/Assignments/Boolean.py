# Comparison Operators Questions
q1_answer = int(input("1. Give a whole number that is less than 5.\n")) #Asking a question which pretty much the input would help it out  
print(q1_answer < 5) 

q2_answer = int(input("2. Give a whole number that is equal to 20.\n"))
print(q2_answer == 20)

q3_answer = int(input("3. Give a whole number that is greater than 99.\n"))
print(q3_answer > 99)

q4_answer = float(input("4. Give a whole  number that is less than or equal to 73.\n"))
print(q4_answer <= 73)

q5_answer = int(input("5. Give a whole number that is not equal to 3.\n"))
print(q5_answer != 3)

# Logical Operators Questions
q6_answer = input("6. Is it True that (5 > 3 ) and (2 < 4)? (yes/no)\n").strip().lower()
print((5 > 3) and (2 < 4) == (q6_answer == 'yes'))    #question 1 

q7_answer = input("7. Is it True that (12 < 5) or (3 > 12)? (yes/no)\n").strip().lower()
print((12 < 5) or (3   > 12) == (q7_answer == 'No')) # question 2 

q8_answer = input("8. Is it True that (2 == 2)? (yes/no)\n").strip().lower()
print( (2 == 2) == (q8_answer == 'yes')) #Question 3 

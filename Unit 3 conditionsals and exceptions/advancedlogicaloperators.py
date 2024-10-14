#  Amazon free shipping  eligbily system
# loyaly customers Or puchases of over $25
# under 18, you need parent consent to purchase

def free_shipping(age, parent_consent,cost, prime_customers):
    if (prime_customers == True or cost >= 25) and (age >= 18 or parent_consent == True):
        print("Free shipping applied!")
    else:
        print("Ineligible for free shipping...")
p = False
c = 18
a = 12 
con = False
free_shipping(p, c, a ,con )
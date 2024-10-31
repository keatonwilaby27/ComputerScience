# amazon free shipping eligibility
# Loyalty customers or purchase of over $25
# under 18, you need parent consent to purchase
def free_shipping(prime, amount, age, cons):
    if (prime == true or amount >= 25) and (age >=18 or cons == True):
        print(" free shipping applied!")


p = False
c = 18
a = 12
con = False

free_shipping(p, c, a, con)
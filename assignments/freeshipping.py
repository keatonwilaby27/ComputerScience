# amazon free shipping eligibility
# Loyalty customers or purchase of over $25
# under 18, you need parent consent to purchase
def free_shipping(prime, amount, age, cons):
    if (prime == True or amount >= 25) and (age >=18 or cons == True):
        print(" free shipping applied!")


p = input(" do you have prime?\n")
c = input(" how much does the order cost?\n")
a = input("Whats your age?\n")
con = input(" do you have parent consent?\n")

free_shipping(p, c, a, con)
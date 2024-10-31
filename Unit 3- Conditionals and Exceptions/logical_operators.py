#Logical operators and or !
# Comparison operators <> == <= >=
#Arithmetic operators + - / * % ** // 

def check_eligibility(age, exp):
    #you must be at least 18 years old and have 1 year experience to be eligible
    if age >= 18 and exp >= 1:
        print(" you are eligible for the competition!")

    elif age < 18:
        print("not old enough")

    elif exp < 1 :
        print("not enough experience")

a = int(input(" How old are you\n"))
e = int(input("How many years experience do you have\n"))
check_eligibility(a , e)
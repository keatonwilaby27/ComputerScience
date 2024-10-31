# Nested if statements
# You are a prime member or order is atleast $25


prime = True
cost = 20
age = 17
consent = False

if prime:
    if age >=18:
        print(" you are eligable for free shipping!")
    else:
        if consent:
            print("you are eligable")
        else:
            print("you are not eligable")
elif cost >=25:
    if age>=18:
        print(" You are eligable ")
    elif consent:
        print("you are eligable")
    else:
        print("You are not eligable for free shipping")
else:
    print("You are not eligable for free shipping")
        





raining = input("is it raining today")


if raining.lower() == "yes":
    outside = input("are you going outside today")

    if outside.lower() == "yes":
        print(" Bring an umbrella")
    else:
        print("Dont bring an umbrella")

else:
    print("dont bring an umbrella")
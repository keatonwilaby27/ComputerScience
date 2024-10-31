x = 5

if x > 0:
    print(" x is a positive number")

elif x<0:       #elif is always paired with an if
    print("x is a negative number")


else:         # else is always paired with if statement above it with nothing in between 
    print(" x is a negative number")



color= input("What color is the light\n")

if color.lower() == "green":      # Only on if
    print("GO")
elif color.lower() == "yellow":    #Can have as many elif as you need
    print("Stop if safe")

elif color.lower() == "red":
    print("Stop")

else:                           # Only one else
    print("call the police")



speed = input(" what is the wind speed\n")
speed= int(speed)
if speed < 74:
    print(" Tropical storm")

elif speed < 96:
    print("CAT 1")

elif speed < 111:
    print("CAT 2")

elif speed < 130:
    print("CAT 3")

elif speed < 157:
    print("CAT 4")

else:
    print("CAT 5")
# if statements evaluate boolean expressions
# Make decisions about which code to run next 

#take a temperature
# print "<temperature> is hot" if the temperature is >= 80
# Otherwise, print "<temperature> is not hot"
temperature = input(" What is the temperature? \n")
if temperature >= 80:
    print(" The temperature is " + str(temperature) + "degrees.")
    print(str(temperature) + " degrees is hot ")

else:
    print(str(temperature) + " degrees is not hot ")


password= "skibidi68"
if password == "skibidi":
   print("access granted")

else:
    print(" access denied")



def add():
    print("Add two numbers:")
    x = input("What is the first number?\n")
    x = int(x)
    y = input("What is the second number?\n")
    y = int(y)
    print(str(x) + "+" + str(y) + "=" + str(x+y))

def sub():
    print("subtract two numbers:")
    x = input ("Whats the first number?\n")
    x = int(x)
    y = input("Whats the second number:\n")
    y = int(y)
    print(str(x) + "-" + str(y) + "=" + str(x-y))

def mult():
    print("subtact two numbers:")
    x = input("whats the first number?\n")
    x = int(x)
    y = input("whats the second number?\n")
    y = int(y)
    print(str(x) + "*" + str(y) + "=" + str(x*y))

def div():
    print("divide two numbers:")
    x = input("Whats the first number?\n")
    x = int(x)
    y = input("Whats the second number?\n")
    y = int(y)
    print(str(x) + "/" + str(y) + "=" + str(x/y))

add()
sub()
mult()
div()

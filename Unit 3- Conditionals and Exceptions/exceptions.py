# Exceptions Handling
# Write a program that asks for two numbers and add them
# If = try
# elif = except specific error
# else = except
def divide():
    try:
        x = int(input(" Whats the first number\n"))
        y = int(input(" whats the second number \n"))
        print(x / y)

    except ValueError:
        print("Please enter a number")
        divide()
    except ZeroDivisionError as e:
        print(" cannot divide by zero")
        divide()
    
    finally:
        print()   # do not need, always runs

divide()
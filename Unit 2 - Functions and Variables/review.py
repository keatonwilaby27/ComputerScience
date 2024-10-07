

#2 functions
print("Hello World!")                 # "Hello World!" is the parameter
input("Please enter your username\n") # \n is called an escape character
                                      # \n starts a new line (linebreak)
                                      # input is never required
                                      # variables
                                      # Syntax
 #<name> = <value>
x=5
#Snake naming convention- all lower case underscore for spaces
#CONCISE: Short and descriptive 
username = "keaton"    #Define string
fav_animal = "moose"   #Define string
total_poptarts = 12    #Define integer
percent_complete = 23.52  #Define float
is_cool = True            #Define boolean (true/ false)
first_character = "c"     #Define character
total_poptarts = 8 #Reassign 
#Arithmetic Operations 
# + - = * / ** % //
print(4+4) #Print 8
print("4"+"4") #Print 44
print("Cat"+"Dog") #print CatDog
print("Cat"*3)  #Print CatCatCat
#add two numbers using input
x= input("What is x\n")#input() always returns a string
x= int(x) #convert from string to int
y= input("what is y\n")# even if you type a number
y= int(y)
print(x + y)

# converts celcius to ferenheight
temp_celcius = input("What is the temp in Celcius\n")
temp_celcius = int(temp_celcius)
temp_ferenheight = (temp_celcius * 1.8) + 32
print(temp_celcius + " degres C equals " + temp_ferenheight + " degrees F")
#conversion functions
str()
int()
float()
bin()
bool()  # True / False

# the stuff in between the parenthesis is called PARAMETERS
# Parameters are the values that the function needs to run



#Functions
#Functions are a lot like variables
#They have names
#They can be recalled from memory by calling their name
#Store information
# Variables store values, functions store code
def potato():    #def keyword + name + () + :
    print("potato")
#functions are not ran when they are defined
#they must be called by their name to run
potato()    # Every function call needs open and closed parenthesis
            # Even if it has no parameters

def jump(how_high):
    print("You jumpped" + str(how_high) + "inches!")

jump(14)

def make_a_word(a,b,c,d,e,f,g,h,i,j,k):
    print(a+b+c+d+e+f+g+h+i+j+k)

make_a_word("O", "s" , "o" , "w" , "s" , "k" , "i")

#Functions can have many many lines
def top_ten_games():
    print("elden ring")
    print("shadow")
    print("minecraft")
    print("diablo 3")
    print("gran turismo")
    print("overwatch")
    print("rachet")
    print("wow")
    print("path")
    print("enter")


#Scope: Global and Local variables
#Scope refers to the context in which the variable was defined
#GLOBAL - defined at no indentation level 
#LOCAL - defined inside of a function
#Global variables can be used anywhere
todd = "cool guy"   #Global variable
def my_function():
    smith = "not cool guy"   #Local variable
    todd = "strange guy"     #Local variable different then the other todd
    print(todd)              #Prints Local variable todd
    # When you call a variable in a function
    #it searches for a local variable first then global
    # if you want to reassign a global variable inside of a function
    def my_function2():
        global todd           #it calls global todd
        todd = "strange guy" #reassignment of global todd
        print(todd)

#Return functions
#Functions can also return values
def add2(x, y):
    return x + y

answer= add

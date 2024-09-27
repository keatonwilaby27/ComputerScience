def top_five_movies(Movie_1, Movie_2, Movie_3, Movie_4, Movie_5):                #Define a new function 
    print ("1." + Movie_1)
    print ("2." + Movie_2)   
    print ("3."+ Movie_3)
    print ("4."+ Movie_4)
    print ("5." + Movie_5)
movie1 = input ("whats your favorite movie?\n")
movie2 = input ("Whats your second favorite movie?\n")
movie3 = input ("whats your third favorite movie?\n")
movie4 = input("whats your fourth favorite movie?\n")
movie5 = input("whats your fith favorite movie?\n")
top_five_movies( movie1 , movie2 , movie3 , movie4 , movie5 )



def add(x, y):
    print(x+y)
add(4, 2)
add(16, 94)
add(43, 34)
num_1 = int(input("whats the first number\n"))
num_2 = int(input("whats the seccond number\n"))
add(num_1, num_2)




x = 4
def my_function():
    global x    #From now on, when I call x, I'm talking about the global version!! Not the local verison...
    x = 5       #Reassigning the global variable x
    print(x)    #Prints 5

print(x)  
my_function()
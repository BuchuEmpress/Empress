# print("Hello, Deepseeds")

# # why do we need variables
# name = "Rita"
# print("I am Gita, I love this name -Gita, was given to me by my father Paul Gita, and I really love the name, Gita")
# print("my name is " + name + " i love " + name + " was given by my father, " + name + " Paul ")

# name1 = "Cake"
# print("I am planning on taking a baking class. There we'll learn to bake all kinds of cake and there's this particular "+ name1 + " I want to bake. It's called spongy " + name1 + "." )
# # Variables
# #is astring, anything inside of a single or double quote
# my_name="Gita"
# #number, we have either float or integer
# #
# age=23
# height=3.56
# #this is a boolean
# isMarried=True
# # or is can be false
# # We've integer, float, string and boolean
# #naming conventions : you can't start naming with a number, Separate your words using underscores not 
# user_name="Peter" #this is the snake casing. Alert! Always use this in python
# userNameFrom="kilian" #camel casing 
# userNameFrom="Paul" #Pascal casing

# # Number
# whole_number= 42    #integer (int)
# decimal_nummber= 3.14159    #float
# complex_number= 3 + 3j #complex

# # Text
# greeting= "hello, World!"   #string (str)
# single_char='A'     #also a string

# # Boolean (True/False)
# is_sunny = True     #Boolean (bool)
# is_rainy= False
# # Check the type of any variable
# print(type(whole_number))   #<class 'int'>
# print(type(greeting))   #<class 'str'>

# # Personal information
# first_name= "Emma"
# last_name= "Watson"
# full_name= first_name + " " + last_name
# age = 33
# birth_year = 2024 - age

# print(f"Hello")

# #  Variables casic examples
# # concatenate variables
# first_name="Emma"
# last_name=" Rose"

# # This is not addition-> because we are adding strings instead, so thiis called concatenation
# combine_name=first_name + last_name
# print("My full names are " + combine_name) #this isn't really a formal way
# print(f"My full names are {combine_name}") #formal

# A ban name generator ; collects (name, age, favorite_meal, school, department, best_friend)
# and use the data to print the story
# name=input("what is your name? ")
# print(f"My name is {name}")
name= "Buchu Empress"
age= 19
favorite_meal= "Rice and Stew"
school= "COLTECH"
department= "CEN" 
best_friend= "I don't have any"
print(f"My name is {name} and I am {age} years old. My favorite meal is {favorite_meal}, I attend the University of Bamenda and the name of my school is {school}; my department {department} and as for my best friend, {best_friend}")

#  Calculator for triangle
length= 10
width= 5
# calculate perimeter (2*(l+w))    and area (l*w)
#print results
perimeter = 2 * (length + width)
print(f"Perimeter of rectangle is {perimeter}")
area= length * width
print(f"The area of recctangle is {area}")


# Temperature converter
# Formula: fahrenheit = (celsius * 9/5) + 32
# print both temperatures
calc= float(input("Enter temparature in celcius "))   # using int to convert the string (by input) into an integer
fahrenheit = (calc * 9/5) + 32
print(f"The temperature in Fahrenheit is: {fahrenheit} ")



# a = 
# b = a
# # swap the numbers such that when the user enters both, "a" displays "b" and "b" displays "a"
# one=int(input("Enter first number: "))
# two=int(input("Enter seconf number: "))
# print(f"The swapped version is {two} and {one}")
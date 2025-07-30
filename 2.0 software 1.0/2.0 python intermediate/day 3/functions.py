# Functions are clean, resuable and maintainable
# The organize your code and get rid of repititions


# Code to calculate the body mass index of a person
# BMI = weight/(h*h)
# if BMI < 18 under weight
# if BMI 18 & 25 normal weight
# if BMI 25 & 30 overwight
# if BMI > 30 obessed

# def bmi_calculator():
#     # print(bmi)
#     weight=float(input("Enter your weight: "))
#     height=float(input("\nEnter your height: "))
#     bmi = weight/(height*height)
    
#     if bmi < 18:
#         print("Under weight")
#     elif bmi >= 18 and  25:
#         print("Normal weight.")
#     elif bmi >= 25 and 30:
#         print("Over weight")
#     elif bmi > 30:
#         print("You're obessed")

# # Functions without output   :fucntion receives input, processes and sends out output
# print (bmi_calculator())

# weight=float(input("Enter your weight: "))
# height=float(input("\nEnter your height: "))
# bmi_calculator(weight, height)

# def calc_circle_area(radius):
# # calculate area of circle given the radius
#     pi= 3.14
#     area= pi * radius * radius
#     return area

# area1= calc_circle_area(5)
# area2= calc_circle_area(10)
# area3= calc_circle_area(7)
# print(f"{area1}")
# print(f"{area2}")
# print(f"{area3}")

# def greet_person(name):
#     # greeting a person by name
#    message= f"Hello {name}! Welcome to functions."
#    return message
#     # using the function
# greeting = greet_person("Alice")
# print(greeting)


# # function with multiple parameters/inputs

# def calc_rectangle_area(length, width):
#     # calculating the area of a rectangle
#     area= length * width
#     return area
# def introduce_person(first_name, last_name, age,city):
#     # creating a personal introduction
#     introduction= f"Hi! I am {first_name} {last_name}. I am {age} years old and I live in {city}"
#     return introduction
# # using the functions
# rect_area=calc_rectangle_area(7, 12)
# intro= introduce_person ("Kate", "Winslet", 28, "Bamenda")

# print(f"The area of rectangle is: {rect_area}")
# print(intro)

# def greet_with_title(name, title="Friend"):
#     # greeting someone with an optional title
#      return f"Hello, {title} {name}!"
 
# print(greet_with_title("Alice"))                    # prints the default title
# print(greet_with_title("Bob", "Dr."))               #prints the custom title
# print(greet_with_title("Charlie", "Profesor"))      #prints the custom title

# # functions the don't return values
# # printing e decorative separator line
# def print_separator():
#     print("--" * 50)
    
# def countdown(start_number):
#     # counting down from a given number
#     for i in range(start_number, 0, -1): # the  countdown begins from the number and ends at 0 decreasing by 1
#         print(f"Count dowm: {i}")
#         print("Blast off! 🚀")

# # using the function
# print_separator()
# print("Welcome to the launch sequence.")
# print_separator()
# # print(countdown(7))  # printing the countdown like this would print the return value "none which isn't defined"
# countdown(7)

# # Exercise 1
# # Personal Information
# def create_profile(name, age, occupation, city):
#     # creating a personal profile string
#     profile= f"Hello, I am {name} and I am {age} years old. I am a {occupation}, I live in {city}"
#     return profile
# # using the function
# my_profile= create_profile("Kate Winslet", 26, "Business woman", "Bamenda")
# print(my_profile)

# Exercise 2
# Grade calculator function
# if the last digit of your number is from 0-2 the it's a minus then from 7-9 it's a plus

def calculate_grade(score):
    if score >= 90:
        grade = "A"
    elif score  >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade= "F"
    last_digit= score % 10
    if last_digit <= 2:
        modifier= "-"
    elif last_digit >= 7:
        modifier= "+"
    else:
        modifier= ""
    return f"{grade}{modifier}"

# using the function

print(calculate_grade(95))
print(calculate_grade(87))
print(calculate_grade(83))


# Exercise 3: Shopping cart total function
def calculate_total(price, quantity, tax_rate=0.08):
    """Calculate total cost including tax."""
    # Your code here
    # Calculate subtotal(price * quantity), tax_amount (subtotal * tax_rate), and final_total (subtotal + tax_amount)
    # Return the final total
    subtotal= price * quantity
    tax_amount= subtotal * tax_rate
    final_total= subtotal + tax_amount
    return final_total

# Testing the function
final_total = calculate_total(29.99, 3)             # if the value is noy returned, then the final_total won't display because we're passing a 
# none type (the function displays none as default when the function doesn't return a value at the end)
print(f"Total cost: ${final_total:.2f}")



# Local and global scopes
# Global variable - lives in the "main house"
house_name = "Python Manor"

def cook_dinner():
    # Local variable - lives only in this "kitchen"
    recipe = "Spaghetti Carbonara"
    cooking_time = 30

    # This function can access both local and global variables
    print(f"Cooking {recipe} in {house_name}")
    print(f"Estimated cooking time: {cooking_time} minutes")

    return recipe

def set_table():
    # Different local scope - this is like a "dining room"
    plates = 4
    utensils = "fork, knife, spoon"

    # Can access global variable
    print(f"Setting table for dinner at {house_name}")
    print(f"Using {plates} plates with {utensils}")

    # Cannot access recipe or cooking_time from cook_dinner function
    # This would cause an error: print(recipe) because it's not in the same scope with the cook_dinner function

# Using the functions
dinner = cook_dinner()
set_table()

# Can access global variable
print(f"Welcome to {house_name}!")

# Cannot access local variables from outside their functions
# This would cause an error: print(recipe)

# Modifying global variables
# Global counter
total_visitors = 0

def welcome_visitor(name):
    """Welcome a visitor and update the counter."""
    global total_visitors  # Ask permission to modify global variable
    total_visitors += 1
    print(f"Welcome, {name}! You are visitor #{total_visitors}")

def show_visitor_count():
    """Display current visitor count."""
    print(f"Total visitors today: {total_visitors}")

# Using the functions
welcome_visitor("Alice")
welcome_visitor("Bob")
welcome_visitor("Charlie")
show_visitor_count()        #this is used because rge function didn't return any value so assigning this line of code to a variable
# would show an error as the return by default is zero
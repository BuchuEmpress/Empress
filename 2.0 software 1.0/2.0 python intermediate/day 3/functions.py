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


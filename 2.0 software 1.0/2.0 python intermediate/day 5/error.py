# Error handling

# def style():
#     print("-" * 40)
    
# def number_error():
#     try:
#      style()
#      user_input=int(input("Please enter your phone number\n"))
#      print(f"User input is {user_input}")
#     except ValueError:
#         print("\nPlease make sure you're inputting a number")       # if the "try" condition is not fulfilled, it automatically 
#         # goes down to fulfill the "except" condition instead of print what poeple don't understand

# number_error()              # number_error() automatically calls the "styel()" function

# # Divisibility
# def division_error():
#     try:
#      style()
#      first_number=int(input("Enter first number: \n"))
#      second_number=int(input("Enter second number: \n"))
#      return first_number/second_number             # here without the try it shows the errors programmers understand and is not presentable to the users
#     except ZeroDivisionError:
#         print("Please enter a number that is not zero")

# # number_error()
# division_error()


# dictionary errors
def dictionary_error(data):
    try:
    
     name=data["name"]
     print(f"Name is: {name}")
     color=data["Red"]
     print(f"My favorite color is: {color}")
    
    except KeyError:
        print("Your accessing a key tha's absent")
    pass

data= {"name":"Faith", "age":20, "FavMeal": "Corn-chaff"}
dictionary_error(data)



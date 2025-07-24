
# # if-else pair
# age=int(input("Please enter your age "))
# if age > 18:
#     print("Yes you can vote")
# else:
#     print("Please wait for next election")
    
    # Exercise: take a person's age, check if they are more than 16, if yes,
    # they can play in basketball team
    
# age=int(input("Enter your age: "))
# if age > 16:
#         print("You can play basket ball")
# else: 
#         print("Sorry! You're not up to the age of playing basketball.")
        
 
#  # if else-elif chain 
# command=input("Enter 'Exit' to end the program and 'Continue' to stay ")
# if command=="Exit":
# # write code that will take user out of cmd
#     print("Exiting cmd...")
# elif command=="Continue":
#    print("Enjoy your stay...")
# else:
#     print("Wrong command")
    
# School grade system

# print("__"*50)
# grade=float(input("Enter your mark: "))
# if grade >= 80:
#     print("Your grade: 'A' ")
# elif grade >= 70:
#     print("Your grade: 'B+' ")
# elif grade >= 60:
#     print("Your grade:'B' ")
# elif grade >= 50:
#     print("Your grade: 'C'")
# elif grade >= 40:
#     print("Your grade: 'D'")
# else:
#     print("Extremely poor")
    
# # Simple calculator
# first_number=float(input("Enter first number: "))
# second_number=float(input("Enter second number: "))
# operator=input("Enter operator: ")
# result=0


# if operator=="+":
#     result=first_number + second_number
#     print(f"Result: {result}")
# elif operator=="-":
#     result=first_number - second_number
#     print(f"Result: {result}")
# elif operator=="*":
#     result=first_number * second_number
#     print(f"Result: {result}")
# if operator=="%":
#     result=first_number % second_number
#     print(f"Result: {result}")
# elif operator=="/":                                         #nested if
#   if second_number!=0:
#      result=first_number / second_number
#      print(f"Result: {result}")
#   else:
#      print("Error! Is not allowed")

# Leap year
# Is divisible by 4  and not divisible 
# Or divisible 400 

# if year== year%4!=0 and year%100!=0  and year%400!=0:
#  print(f"{year}: Is not a leap year")
# else:
#     print(f"{year}: Is a leap year")

# year=int(input("Enter any random year "))
# if year%4!=0 and year%100!=0 and year%400!=0:
#     print(f"{year}: Is not a leap year")
# else:
#     print(f"{year}: Is a leap year")

# if year%4!=0 :                              #leap year
#  if year%100!=0:                           # not leap year
#     if year%400!=0:                        #not leap year
#       print("Is not a leap year")
#     else:
#         print("Is a leap year")
    
    #print("I WILL ALWAYS DO MY ASSIGNMENT\n"*50)
names=["Will", "Leo", "Kate", "Killian", "Akinimbom", "Gadmbom", "Jeanmbom", "colimbom", "jackmbom","afatimbom"]
# print(names[0])
# print(names[1])
# print(names[2])
       
 #  print(name)
# if name.endswith("mbom"):
#             print(f"We dan catch you: {name}")
# else:
#             print(f"Welcome to the party: {name}")
            

count=1
for name in names:
 print(f"{count}.{name}")
count += 1


   
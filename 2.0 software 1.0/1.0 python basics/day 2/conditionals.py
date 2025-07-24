
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

print("__"*50)
grade=float(input("Enter your mark: "))
if grade >= 80:
    print("Your grade: 'A' ")
elif grade >= 70:
    print("Your grade: 'B+' ")
elif grade >= 60:
    print("Your grade:'B' ")
elif grade >= 50:
    print("Your grade: 'C'")
elif grade >= 40:
    print("Your grade: 'D'")
else:
    print("Extremely poor")
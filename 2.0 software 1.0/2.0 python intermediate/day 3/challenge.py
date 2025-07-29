# challenge one
# FizzBuzz game
# If number is divisible by 3, print Fizz
# If number is divisible by 5, print Buzz
# If divisible by both, print FizzBuzz
#If not divisible by any print the number


# print("--"*50)
# print("This is a cool game. And here are the directions. \n You enter a random number and the computer would tell you if it's a \"Fizz\" (Meaning the number is divisible by 3). \n Or if it's a \"Buzz\" (Meaning it's divisible by 5). \n Or a \"FizzBuzz\" (Meaning it's divisible by both 3 and 5). \n And would display just the number if it's not divisible by any.")
# # print("Type \"Stay\" to keep playing and \"Q\" to quit!")
# print("Ready..? Let's go☺")
# print("--" * 50)
# while True:
       
#  value=int(input("Enter any random number: "))

#  if value % 3==0 and value % 5==0:
#         print("FizzBuZZ")
#  elif value % 3==0 :
#         print("Fizz")
#  elif value % 5 ==0:
#         print("Buzz")
#  elif value % 3 and 5 != 0:    
#         print(f"{value}")
#  else:
#        print("Unrecognized")
  
       
# #  Challenge two     
# #    Swap two numbers
# # turn a into c
# # turn  turn b into a
    
# input_one= float(input("Enter first value: "))
# input_two= float(input("\nEnter second value: "))
# input_three=input_one
# input_one=input_two
# input_two=input_three

# print(f" Swapping both numbers give: {input_one} and {input_two}")


# challenge three
# Guessing  Game
# Computer guesses a random number
# User tell what the number is in not more that 3 guesses
# when user guesses a number above or below it notifies you
import random
target = random.randint(1, 20)
trials=0
max_trials= 3
print(".." * 50)
print("I have guessed a number between 1 and 20. \n You have a maximum of 3 trials to guess the number or I win")
print("But if you guess right within the bound of trials, You win! ")
print("--" * 50)
while trials < max_trials:  # reason why it's strictly less than max_trials 
       # on the first iteration, trial which is 0 turns to 1; on second iteration which is 1 turns to 2 and lastly
       # the third which is 2 turns to 3 and the trials end
       user_guess=int(input("Enter the number guessed by computer.\n"))
       trials += 1
       if user_guess < target:
        print(f"Number is less than target. You have {max_trials - trials} attempts left!")
       elif user_guess > target:
        print(f"Number is greater than target. You have {max_trials - trials} attempts left!")
       else:
        print(f"You have the right number. You won in {trials} attempts!")
        break
else:
       print(f"Out of trails.\nSorry you didn't guess right, the number was {target}. Hence, I won!")
        
 
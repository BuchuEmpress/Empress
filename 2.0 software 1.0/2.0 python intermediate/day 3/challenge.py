# FizzBuzz game
# If number is divisible by 3, print Fizz
# If number is divisible by 5, print Buzz
# If divisible by both, print FizzBuzz
#If not divisible by any print the number

# while True:
#  value=int(input("Enter any random number: "))

#  if value % 3==0 and value % 5==0:
#         print("FizzBuZZ")
#  elif value % 3==0 :
#         print("Fizz")
#  elif value / 5:
#         print("Buzz")
#  elif value % 3 and 5 != 0:    
#         print(f"{value}")
# else:
#        print("Unrecognized")
       
       
#    Swap two numbers
# turn a into c
# turn  turn b into a
    
# input_one= float(int("Enter first value: "))
# input_two= float(int("\nEnter second value: "))
# input_three=input_one
# input_

# print(f"{input_three}")



# Guessing  Game
# Computer guesses a random number
# User tell what the number is in not more that 3 guesses
# when user guesses a number above or below it notifies you

import random
target = random.randint(1, 20)
max_trials= 3

guess=int(input("Enter the number guessed by computer. \n You have just three trials! \n"))
while guess <= max_trials:
 if guess < target:
        print("Number is less than target")
 elif guess > target:
        print("Number is greater than target")
 elif guess == target:
     print("You have the right number")
 break
else:
 print("Out of trails.")
        

# import random

# # 🖼️ Array of ASCII art diagrams
# ascii_art_diagrams = [
#     r"""
#      /\_/\
#     ( o.o )
#      > ^ <
#     """,

#     r"""
#      _______
#     |       |
#     |       O
#     |      /|\
#     |      / \
#     |
#     =========
#     """,

#     r"""
#     _______
#    /       \
#   |  (• ◡•)  |
#    \_______/
#     """,

#     r"""
#      __
#     /  \
#    |    |
#    |____|
#   /      \
#  /________\
#     """
# ]

# # 📝 Array of creative writing prompts
# story_prompts = [
#     "Write a story about a robot who wants to be human.",
#     "Describe a world where plants can talk to people.",
#     "Create a mystery involving a time-traveling detective.",
#     "Tell a bedtime story set on a spaceship.",
#     "Imagine a dragon who’s afraid of fire.",
#     "Write about a kid who finds a magical notebook.",
#     "Narrate a short poem about loneliness and the moon.",
#     "Describe an ancient civilization powered by sound."
# ]







# for loop
# 1. starting point
# 2. condition
# 3. increment database
# database of people
names=["Will", "Leo", "Kate", "Killian", "Akinimbom", "Gadmbom", "Jeanmbom", "colimbom", "jackmbom","afatimbom"]
# print(names[0])
# print(names[1]) 
# print(names[2])

# for name in names:              # he name in the names array
#     print(name)
# if name.endswith("mbom"):
#             print(f"We dan catch you: {name}")
# else:
#             print(f"Welcome to the party: {name}")
            
# count=1
# for name in names:
#  print(f"{count}.{name}")
#  if name.endswith("mbom"):
#              print(f"We dan catch you: {name}")
#  else:
#              print(f"Welcome to the party: {name}")
# count += 1

# my_names="Ashantimbom"

# # range(stop) - starts from 0
# for i in range(5):
#     print(5) # 0, 1, 2 ,3 ,4
    
# range(start, stop)
# for i in range(2, 7):
#     print(i)  # 2, 3, 4, 5, 6
    
#     # range(start, stop, step)
# for i in range(0, 10, 2):
#     print(i)  # 0, 2, 4, 6, 8 (counts in twos)
    
#     # countdown
# for i in range(10, 0, -1):  # countdown from 10 minussing 1 by each count
#     print(f"Countdown: {i}")  
#     print("Blast off! 🚀")
    
# range method in looping
# break keyword

# while True:
#     print("Madness")   # Ctrl + C to kill
    
# count=1
# while count <= 5:
#      print(f"Count is: {count}")
#      count+=1  # same as count= coutnt + 1
     
#     #  user input loop
# user_input= ""
# while user_input != "quit":             # situation where it's true; meaning user hasn't typed "quit yet"
#         user_input= input("Enter 'quit' to exit: ")
#         if user_input != "quit":            # is a situation where false meni
#             print(f"You entered: {user_input}")
    
# print("Goodbye!")



# # break - exit the loop completely
# print("Finding the first number: ")
# for number in range(1, 10):
#     if number % 2 ==0:
#         print(f"Found even number: {number}")
#         break
#     print(f"{number} is odd")
    
# # Contiue - skip to next iteration

# print("\nPrinting only odd numbers. ")
# for numbers in range(1,10):
#     if number % 2 == 0:
#         continue # skip even numbers
#     print(f"Odd number: {number}")
    
# # Multiplication table      nested loops
# print("Multiplication Table:")
# for i in range(1, 4):       #in rows
#     for j in range(1, 4):   # colums
#         result = i *j
#         print(f"{i} x {j} = {result}")
#         print()         #Empty line after each row
        
# Pattern printing
print("Triangle pattern: ")
for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()                                     # New line after each row
      
    
    
    
   
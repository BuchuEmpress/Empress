# Test 
# Write a function tha takes in an array and calculate average of that array
# loop through to find if target is in that array
# if yes display "Seen" if no, display "unseen"

# def display_average(arr, target):
#    average= sum(arr)/ len(arr)
#    target= "seen" if target in arr else "Unseen"
#    return average, target
              
# # using the function
# arr=[3, 5, 6, 7]
# target= 10
# average=display_average(arr, target)  
# print(f"Average is:{average} and target is: {target}")  
     
# OR
def display_average(arr, target):
    total=0
    length=0
    average=total/len(arr)
    for number in arr:
        # numbers = [3, 4, 5, 5, ,6 ,3]
        total = total + number
        length = length + 1
    found = False
    for number in arr:
        if number == target:
            found = True
            break
    if found == True:
        print("Seen")
    else:
        print("Unseen")
    average= total/length
    return average

# Using the function
numbers=[3, 4, 6, 7, 8]
target = 8
result= display_average(numbers, target)
print(f"Average = {result}")

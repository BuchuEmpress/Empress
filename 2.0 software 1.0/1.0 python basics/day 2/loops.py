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
            
count=1
for name in names:
 print(f"{count}.{name}")
 if name.endswith("mbom"):
             print(f"We dan catch you: {name}")
 else:
             print(f"Welcome to the party: {name}")
count += 1

my_names="Ashantimbom"

# range(stop) - starts from 0
for i in range(5):
    print(5) # 0, 1, 2 ,3 ,4
    
# range(start, stop)
for i in range(2, 7):
    print(i)  # 2, 3, 4, 5, 6
    
    # range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8 (counts in twos)
    
    # countdown
for i in range(10, 0, -1):  # countdown from 10 minussing 1 by each count
    print(f"Countdown: {i}")  
    print("Blast off! 🚀")
   
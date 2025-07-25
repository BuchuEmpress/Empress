

l=False
u=False
d=False


while True:
 password=input("A strong password must contain at least one uppercase, one lowercase and one digit. \nEnter Strong Password: ")

 if len(password) < 8:
        print ("Passwords must cotain at least 8 characters")
        continue
 for letter in password:
    if letter.islower():
        l=True
    if letter.isupper():                    # can continue with elif without while loop
        u=True
    if letter.isdigit():
        d=True
 if l and u and d:
     print("This is a strong password")
     break

 else:
     print("Please type in a strong password")
     
    
    # Assignment check for the length atleast 8 chars
    # Equally make it to loop till one types the correct password then stops
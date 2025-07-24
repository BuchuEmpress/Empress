

l=False
u=False
d=False

password=input("A strong password must contain at least one uppercase, one lowercase and one digit. \nEnter Strong Password: ")

for letter in password:
    if letter.islower():
        l=True
    elif letter.isupper():
        u=True
    elif letter.isdigit():
        d=True
if l and u and d:
    print("This is a strong password")
else:
    print("Please type in a strong password")
    
    
    # Assignment check for the length atleast 8 chars
    # Equally make it to loop till one types the correct password then stops
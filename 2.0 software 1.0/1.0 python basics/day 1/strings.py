# concatenation and interpolation (string operations in python)
first_name= "John"
last_name= "Ngalah"
# Concatenation
full_names=first_name + last_name

# Interpolation
print(f"fullnames are {full_names}")

laugh= "Ha" * 7
# hahaha
print(laugh)

message= "Hello, Python!"
print(len(message) )     #14

message = "Greta"
print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])

# String formatting
name="Alice"
age= 30
score= 95.5
# Method 1: f-strings (recommended - like fill-in-the-blank)
print(f"Hello, {name}! You are {age} years old.")
print(f"Your score is {score:.1f}%")

# Method 2: format() method
print("Hello, {}! You are {} years old.".format (name, age))

# Method 3: formatting (older style)
print("Hello, %s! You are %d years old." % (name, age))
  

#  Email validator (basic)
email="user@example.com"
if "@" in email and "." in email:
    username = email.split("@") [0]
    domain = email.split("@")[1]
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email format")
    
    # Text analyzer
    text = "The quick brown fox jumps over the lazy dog"
    print(f"Text: {text}")
    print(f"Length: {len(text)} characters")
    print(f"Words: {len(text.split())} words")
    print(f"Uppercase: {text.upper()}")
    print(f"Title case: {text.title()}")
    print(f"Contains 'fox': {'fox' in text}") 
    
    
    
    # 24 July 
    # String Methods ass strinf operators
    # just a function or simply something()
    
message="Good morning"
    # convert from uppercase to lowercase and vice versa
    
message_lower= message.lower()
message_upper= message.upper()
print(f"The lower case conversation is: {message_lower} and uppercase conversion is: {message_upper}")
    
    # slice method
greetings="Welcome back"
how_python_sees_it=list(greetings)
print(f"Python view: {how_python_sees_it}")
extract_text=greetings[0:3]
    

print(f"Extracted text is: {extract_text}")
    
    
    # Name Formatter
# Get a full name and format it properly
full_name="jOhN dOe"
# make it: "John Doe"
# print first name and last name separately

adjusted_name=  full_name.title()
print(f"My full name is: {adjusted_name}")

j=full_name[0].upper()
d=full_name[5].upper()
half=full_name[1:4].lower()
half2=full_name[6:8].lower()
print(f"My full name is: {j}{half} {d}{half2}")
    
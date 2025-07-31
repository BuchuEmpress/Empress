# Tuples are sealed envelopes
# They're like lists/arrays but are immutable/unchangeable
# They consume less space that lists

# ---------------------------------------------------------------------------------------
# Creating tuples - like sealing important information
point_coordinates = (10, 20)  # A point in 2D space
rgb_color = (255, 128, 0)     # Orange color values
student_record = ("Alice", 20, "Computer Science", 3.8)

# Tuples can be created without parentheses too
another_point = 5, 15
single_item_tuple = (42,)  # Note the comma - this is important!

print(f"Point coordinates: {point_coordinates}")
print(f"RGB color: {rgb_color}")
print(f"Student record: {student_record}")
print(f"Single item tuple: {single_item_tuple}")

# ---------------------------------------------------------------------------------------
# Accessing an element in an tuples
# Working with a tuple representing a book record
book_info = ("1984", "George Orwell", 1949, "Dystopian Fiction")

# Accessing individual elements
title = book_info[0]
author = book_info[1]
year = book_info[2]
genre = book_info[3]

print("--" * 50)
print(f"Book: {title}")
print(f"Author: {author}")
print(f"Published: {year}")
print(f"Genre: {genre}")

# Tuple unpacking - a powerful feature
title, author, year, genre= book_info
print(f"Using unpacking - Book: {title} by {author} ({year})")

# Partial unpacking with the rest operator
first_name, last_name, *other_info = ("John", "Smith", 30, "Engineer", "New York")
print(f"Name: {first_name} {last_name}")
print(f"Other info: {other_info}")

# -----------------------------------------------------------------------
# Tuple methods and operations
# Sample tuple with some repeated values
grades = (85, 90, 78, 90, 88, 92, 85, 88)

# Getting information about the tuple
print("--" * 50)
print(f"Number of grades: {len(grades)}")
print(f"Highest grade: {max(grades)}")
print(f"Lowest grade: {min(grades)}")

# Counting occurrences
print(f"Number of 90s: {grades.count(90)}")
print(f"Number of 85s: {grades.count(85)}")
print(f"Number of 88s: {grades.count(88)}")

# Finding the position of an element
print(f"First occurrence of 90: {grades.index(90)}")
print(f"First occurence of 88: {grades.index(88)}")
# print(f"The second occurence of 88: {grades.index(88)}")

# Checking if an element exists
print(f"Is 95 in grades? {95 in grades}")
print(f"Is 85 in grades? {85 in grades}")
print(f"Is 97 in grades? {97 in grades}")

# Slicing works with tuples too
print(f"First three grades: {grades[:3]}")
print(f"Last three grades: {grades[-3:]}")
print(f"From the fifth grade: {grades[5:]}")

# ---------------------------------------------------------------------------------------
# Practical Tuple Example
# Representing geographic coordinates
def get_distance_between_points(point1, point2):
    """Calculate distance between two points using tuples."""
    x1, y1 = point1                   #unpacks the coordinates of the two points into separate variables
    x2, y2 = point2

    # Using the distance formula d = ((x2-x1)**2/(y2-y1)**2)                             
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5         #the "**" is not for multiplication but for 
    # exponentiation(raising to the power) while the "*" is for multiplication
    return distance

# Using coordinate tuples
home = (0, 0)
work = (3, 4)
store = (1, 2)

print("--" * 50)
print(f"Distance from home to work: {get_distance_between_points(home, work):.2f}")  # calculates and print distance from home to work
print(f"Distance from home to store: {get_distance_between_points(home, store):.2f}")

# Function that returns multiple values using tuples
def analyze_text(text):
    """Analyze text and return statistics as a tuple."""
    words = text.split()    # to remove any space ".spilt()"
    word_count = len(words)
    char_count = len(text)
    sentence_count = text.count('.') + text.count('!') + text.count('?')     
    # splits the text into words and calculates the word count, character, count and sentance count

    return (word_count, char_count, sentence_count)      #return the calculated statistics as a tuple

# Using the function
sample_text = "Python is amazing! It's powerful and easy to learn. Try it today!"
word_count, char_count, sentence_count = analyze_text(sample_text)
# analyzes the sample text and unpacks the returned statistics into separate variables

print(f"Text analysis:")
print(f"Words: {word_count}")
print(f"Characters: {char_count}")
print(f"Sentences: {sentence_count}")

# Database-like records using tuples
employee_records = [
    ("Alice", "Johnson", "Software Engineer", 75000),
    ("Bob", "Smith", "Data Scientist", 80000),
    ("Charlie", "Brown", "Product Manager", 85000),
    ("Gracey", "Hart", "AI Engineer", 78000)
]
# defines a list of employee records where each record is a tuple containing the employee's first name, last name
#position, and salary
print("Employee Directory:")
for first_name, last_name, position, salary in employee_records:        #iterates over the employee records and unpacks ech reccord into separate vaiables
    print(f"{first_name} {last_name} - {position} - ${salary:,}")
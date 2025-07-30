# # creates values in key pairs i.e. keys and values; the unique key and the value
# # Creating dictionaries - like building an address book
# student_info = {
#     "name": "Alice Johnson",
#     "age": 20,
#     "major": "Computer Science",
#     "gpa": 3.8,
#     "is_graduate": False
# }

# # Phone directory
# phone_book = {
#     "Alice": "555-1234",
#     "Bob": "555-5678",
#     "Charlie": "555-9012"
# }

# # Empty dictionary
# empty_dict = {}

# print(f"Student info: {student_info}")
# print(f"Phone book: {phone_book}")

# # accessing dictionary values
# # Using our student dictionary
# student = {
#     "name": "Alice Johnson",
#     "age": 20,
#     "major": "Computer Science",
#     "gpa": 3.8,
#     "courses": ["Python", "Calculus", "Physics"]
# }

# # Accessing values by key
# print(f"Student name is: {student['name']}")
# print(f"Student age is: {student['age']}")
# print(f"Major: {student['major']}")

# # Safer way to access values (won't crash if key doesn't exist)         
# print(f"GPA: {student.get('gpa', 'Not Specified')}")            #safer because the get keyword has two parameters and 
# print(f"Graduation year: {student.get('grad_year', 'Not specified')}")

# # Checking if a key exists
# if "courses" in student:
#     print(f"Current courses: {student['courses']}")

# # Getting all keys and values
# print(f"All keys: {list(student.keys())}")          # uses the "list" to take the keys and values and format it to display as a list
# print(f"All values: {list(student.values())}")


# # modifying dictionaries
# # Starting with basic student info
# student = {
#     "name": "Alice Johnson",
#     "age": 20,
#     "major": "Computer Science"
# }

# print(f"Original: {student}")

# # Adding new information
# student["gpa"] = 3.8
# student["graduation_year"] = 2025
# print(f"After adding GPA and grad year: {student}")
# student["Department"]= "Electrical Engineering"
# print(f"After adding the department: {student}")

# # Updating existing information
# student["age"] = 21  # Birthday!
# student["major"] = "Software Engineering"  # Changed major
# student["gpa"]= 4.0
# print(f"After updates: {student}")

# # Adding multiple items at once
# student.update({
#     "email": "alice@university.edu",
#     "phone": "555-1234"
# })
# print(f"After adding contact info: {student}")

# # student.update({
# #     "location":"Mile 6 Nkwen"
# #     "quarter": "Mbelem"
# # })
# # print(f"After adding location: {student}")

# # Removing information
# removed_phone = student.pop("phone")  # Remove and return value
# print(f"Removed phone: {removed_phone}")
# print(f"After removing phone: {student}")
# removed_department=student.pop("Department")
# print(f"Removed department: {removed_department}")
# print(f"After removing department: {student}")

# # Remove a key-value pair (different method)
# del student["email"]
# print(f"After removing email: {student}")
# del student["age"]
# print(f"After removing the age: {student}")

# # Dictionary methods and operations
# # Inventory system for a small store
# inventory = {
#     "apples": 50,
#     "bananas": 30,
#     "oranges": 25,
#     "milk": 15,
#     "bread": 20
# }

# # Getting information about the dictionary
# print("--" * 50)
# print(f"Number of products: {len(inventory)}")
# print(f"Products: {list(inventory.keys())}")
# print(f"Quantities: {list(inventory.values())}")

# # Working with key-value pairs
# print("Current inventory:")
# for product, quantity in inventory.items():
#     print(f"- {product}: {quantity}")

# # Checking stock levels
# low_stock_items = []
# for product, quantity in inventory.items():
#     if quantity < 20:
#         low_stock_items.append(product)

# print(f"Low stock items: {low_stock_items}")

# # Copying dictionaries
# backup_inventory = inventory.copy()
# print(f"Backup created: {backup_inventory}")

# # Clearing all items
# test_dict = {"a": 1, "b": 2}
# test_dict.clear()
# print(f"After clearing: {test_dict}")

# # Nested dictionaries
# # Student database with multiple students
# students_database = {
#     "student_001": {
#         "name": "Alice Johnson",
#         "age": 20,
#         "major": "Computer Science",
#         "grades": {
#             "Python": 95,
#             "Calculus": 88,
#             "Physics": 92
#         }
#     },
#     "student_002": {
#         "name": "Bob Smith",
#         "age": 19,
#         "major": "Mathematics",
#         "grades": {
#             "Algebra": 91,
#             "Statistics": 87,
#             "Geometry": 94
#         }
#     }
# }

# # Accessing nested information
# alice = students_database["student_001"]
# print(f"Alice's name: {alice['name']}")
# print(f"Alice's Python grade: {alice['grades']['Python']}")

# # Adding new nested information
# students_database["student_001"]["email"] = "alice@university.edu"
# students_database["student_001"]["grades"]["Chemistry"] = 89

# print(f"Alice's updated info: {students_database['student_001']}")

# # Exercise 1
# # Personal Contact Manager
# contacts = {}

# def add_contact(name, phone, email):
#     """Add a contact to the directory."""
#     contacts[name] = {
#         "phone": phone,
#         "email": email
#     }
#     print("--" * 50)
#     print(f"Added contact: {name}")

# def update_contact(name, phone=None, email=None):
#     """Update an existing contact."""
#     if name in contacts:
#         if phone:
#             contacts[name]["phone"] = phone
#         if email:
#             contacts[name]["email"] = email
#         print(f"Updated contact: {name}")
#     else:
#         print(f"Contact {name} not found")

# def show_all_contacts():
#     """Display all contacts."""
#     if not contacts:
#         print("No contacts in directory")
#         return

#     print("Contact Directory:")
#     for name, info in contacts.items():
#         print(f"Name: {name}")
#         print(f"  Phone: {info['phone']}")       # info is the name for the value (which are the phone and email)
#         print(f"  Email: {info['email']}")
#         print()

# # Test your functions


# add_contact("Alice", "555-1234", "alice@email.com")
# add_contact("Bob", "555-5678", "bob@email.com")
# show_all_contacts()
# update_contact("Alice", phone="555-9999")
# show_all_contacts()



# Exercise 2
# Grade book system
gradebook = {}

def add_student(name):
    """Add a new student to the gradebook."""
    if name not in gradebook:
        gradebook[name] = {}
        print(f"Added student: {name}")
    else:
        print(f"Student {name} already exists")

def add_grade(student_name, subject, grade):
    """Add a grade for a student in a specific subject."""
    if student_name in gradebook:
        gradebook[student_name][subject] = grade
        print(f"Added grade for {student_name} in {subject}: {grade}")
    else:
        print(f"Student {student_name} not found")

def calculate_average(student_name):
    """Calculate the average grade for a student."""
    if student_name in gradebook and gradebook[student_name]:
        grades = list(gradebook[student_name].values())
        average = sum(grades) / len(grades)
        return average
    else:
        return None

def show_student_grades(student_name):
    """Display all grades for a specific student."""
    if student_name in gradebook:
        print(f"Grades for {student_name}:")
        for subject, grade in gradebook[student_name].items():
            print(f"  {subject}: {grade}")

        average = calculate_average(student_name)
        if average:
            print(f"  Average: {average:.1f}")
    else:
        print(f"Student {student_name} not found")

# Test the gradebook system
add_student("Alice")
add_student("Bob")
add_grade("Alice", "Math", 95)
add_grade("Alice", "Science", 88)
add_grade("Alice", "English", 92)
show_student_grades("Alice")


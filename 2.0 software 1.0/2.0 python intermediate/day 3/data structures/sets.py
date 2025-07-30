# Simply sets are a collection of items  cos ou can have a mixed set
# sets are special containers that automatically prevent duplicates. They ensure uniqueness
# Sets are perfect when you need to ensure all items are unique or when you want to perform mathematical 
# operations like finding common elements between groups
# Creating sets - like building unique collections
unique_numbers = {1, 2, 3, 4, 5}
colors = {"red", "blue", "green", "yellow"}
mixed_set = {1, "hello", 3.14, True}

# Creating sets from lists (removes duplicates automatically)
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers_from_list = set(numbers_with_duplicates)

# Empty set (note: {} creates an empty dictionary, not set)
empty_set = set()

print(f"Unique numbers: {unique_numbers}")
print(f"Colors: {colors}")
print(f"From list with duplicates: {unique_numbers_from_list}")
print(f"Empty set: {empty_set}")



# Set operations
# Student enrollment in different courses
python_students = {"Alice", "Bob", "Charlie", "Diana"}
java_students = {"Bob", "Charlie", "Eve", "Frank"}
javascript_students = {"Charlie", "Diana", "Eve", "Grace"}

# Union - students taking ANY programming course
all_programming_students = python_students | java_students | javascript_students
print(f"All programming students: {all_programming_students}")

# Intersection - students taking BOTH Python AND Java
python_and_java = python_students & java_students
print(f"Students taking both Python and Java: {python_and_java}")

# Difference - students taking Python but NOT Java
python_only = python_students - java_students
print(f"Students taking Python but not Java: {python_only}")

# Symmetric difference - students taking Python OR Java but not both
python_xor_java = python_students ^ java_students
print(f"Students taking Python or Java but not both: {python_xor_java}")



# Modifying sets
# Starting with a basic set of skills
my_skills = {"Python", "JavaScript", "HTML"}
print(f"Initial skills: {my_skills}")

# Adding single skills
my_skills.add("CSS")
my_skills.add("React")
my_skills.add("Angular")
print(f"After learning CSS and React: {my_skills}")

# Adding multiple skills at once
new_skills = {"Node.js", "MongoDB", "Docker"}   # create a new set to add the skills you're currently adding
my_skills.update(new_skills)                     # add the new set containing new items
print(f"After bootcamp: {my_skills}")

# Removing skills (maybe you forgot some!)
my_skills.remove("HTML")  # Raises error if not found
print(f"After forgetting HTML: {my_skills}")
my_skills.remove("React")
print(f"After for react: { my_skills}")

# Safer removal (won't raise error if not found)
my_skills.discard("PHP")  # Won't cause error even though PHP isn't in the set
print(f"After trying to remove PHP: {my_skills}")

# Removing and returning an arbitrary/random element
removed_skill = my_skills.pop()
print(f"Randomly removed skill: {removed_skill}")
print(f"Remaining skills: {my_skills}")
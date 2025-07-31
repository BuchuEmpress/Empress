# Working with different data structures
# Complex student management system
class_roster = {
    "CS101": {
        "course_name": "Introduction to Programming",
        "students": ["Alice", "Bob", "Charlie"],
        "assignments": [
            {"name": "Hello World", "due_date": "2024-02-15", "points": 10},
            {"name": "Variables and Types", "due_date": "2024-02-22", "points": 25}
        ],
        "grades": {
            "Alice": [10, 23],
            "Bob": [8, 22],
            "Charlie": [10, 25]
        }
    },
    "CS102": {
        "course_name": "Data Structures",
        "students": ["Alice", "Diana", "Eve"],
        "assignments": [
            {"name": "Arrays", "due_date": "2024-02-20", "points": 30},
            {"name": "Linked Lists", "due_date": "2024-02-27", "points": 35}
        ],
        "grades": {
            "Alice": [28, 33],
            "Diana": [30, 35],
            "Eve": [25, 30]
        }
    }
}

def calculate_student_average(course_code, student_name):
    """Calculate average grade for a student in a specific course."""
    if course_code in class_roster and student_name in class_roster[course_code]["grades"]:
        grades = class_roster[course_code]["grades"][student_name]
        total_points = sum(grades)

        # Calculate total possible points
        assignments = class_roster[course_code]["assignments"]
        total_possible = sum(assignment["points"] for assignment in assignments)

        percentage = (total_points / total_possible) * 100
        return percentage
    else:
        return None

def find_common_students(*course_codes):
    """Find students enrolled in multiple courses."""
    if not course_codes:
        return set()

    # Start with students from first course
    common_students = set(class_roster[course_codes[0]]["students"])

    # Find intersection with other courses
    for course_code in course_codes[1:]:
        course_students = set(class_roster[course_code]["students"])
        common_students &= course_students

    return common_students

# Using the system
print("--" * 50)
print("Alice's average in CS101:", f"{calculate_student_average('CS101', 'Alice'):.1f}%")
print("Students in both CS101 and CS102:", find_common_students("CS101", "CS102"))

# Recipe management system combining all data structures
recipe_database = {
    "Pancakes": {
        "ingredients": [
            ("flour", 2, "cups"),
            ("milk", 1.5, "cups"),
            ("eggs", 2, "pieces"),
            ("sugar", 2, "tablespoons")
        ],
        "instructions": [
            "Mix dry ingredients in a bowl",
            "Combine wet ingredients separately",
            "Gradually add wet to dry ingredients",
            "Cook on griddle until golden"
        ],
        "prep_time": 10,
        "cook_time": 15,
        "servings": 4,
        "dietary_tags": {"vegetarian"}
    },
    "Chicken Stir Fry": {
        "ingredients": [
            ("chicken breast", 1, "pound"),
            ("broccoli", 2, "cups"),
            ("soy sauce", 3, "tablespoons"),
            ("garlic", 2, "cloves")
        ],
        "instructions": [
            "Cut chicken into bite-sized pieces",
            "Heat oil in wok or large pan",
            "Cook chicken until done",
            "Add vegetables and sauce"
        ],
        "prep_time": 15,
        "cook_time": 12,
        "servings": 3,
        "dietary_tags": {"gluten-free", "high-protein"}
    }
}

def find_recipes_by_time(max_total_time):
    """Find recipes that can be made within a time limit."""
    suitable_recipes = []

    for recipe_name, recipe_info in recipe_database.items():
        total_time = recipe_info["prep_time"] + recipe_info["cook_time"]
        if total_time <= max_total_time:
            suitable_recipes.append((recipe_name, total_time))

    # Sort by total time
    suitable_recipes.sort(key=lambda x: x[1])
    return suitable_recipes

def get_shopping_list(recipe_names):
    """Generate shopping list for multiple recipes."""
    shopping_list = {}

    for recipe_name in recipe_names:
        if recipe_name in recipe_database:
            for ingredient, amount, unit in recipe_database[recipe_name]["ingredients"]:
                if ingredient in shopping_list:
                    # Simple aggregation (assumes same units)
                    shopping_list[ingredient] += amount
                else:
                    shopping_list[ingredient] = amount

    return shopping_list

# Using the recipe system
quick_recipes = find_recipes_by_time(30)
print("Recipes under 30 minutes:")
for recipe, time in quick_recipes:
    print(f"- {recipe}: {time} minutes")

shopping_list = get_shopping_list(["Pancakes", "Chicken Stir Fry"])
print("\nShopping list:")
for ingredient, amount in shopping_list.items():
    print(f"- {ingredient}: {amount}")
    
    
    
    
# Data Structure Selection Guide
# Understanding when to use each data structure is crucial for efficient programming:
# Practical examples of choosing the right data structure

# Use LIST when:
# - You need ordered data
# - You need to access items by position
# - You need to modify the collection frequently
shopping_cart_items = ["apple", "bread", "milk", "eggs"]  # Order matters for checkout

# Use DICTIONARY when:
# - You need fast lookups by key
# - You're storing related attributes
# - You need to map one thing to another
student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}  # Fast grade lookups

# Use TUPLE when:
# - Data shouldn't change
# - You need to return multiple values from a function
# - You're representing fixed records
coordinates = (10, 20)  # Point coordinates shouldn't change arbitrarily

# Use SET when:
# - You need unique items only
# - You need to find common or different items between groups
# - You need fast membership testing
unique_visitors = {"user1", "user2", "user3"}  # No duplicate visitors

def demonstrate_data_structure_choice():
    """Show practical examples of choosing the right data structure."""

    # Scenario 1: Event planning
    print("--" * 50)
    print("Event Planning System:")

    # Guest list (order matters for seating)
    guest_list = ["Alice", "Bob", "Charlie", "Diana"]

    # RSVP responses (fast lookup by name)
    rsvp_responses = {
        "Alice": "Yes",
        "Bob": "No", 
        "Charlie": "Yes",
        "Diana": "Maybe"
    }

    # Dietary restrictions (unique items only)
    dietary_restrictions = {"vegetarian", "gluten-free", "vegan"}

    # Event details (immutable record)
    event_details = ("Wedding Reception", "2024-06-15", "Grand Ballroom")

    print(f"Event: {event_details[0]} on {event_details[1]}")
    print(f"Confirmed guests: {[guest for guest in guest_list if rsvp_responses.get(guest) == 'Yes']}")
    print(f"Dietary restrictions to consider: {dietary_restrictions}")

demonstrate_data_structure_choice()
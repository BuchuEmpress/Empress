# # a list is a collection of items
# shopping_cart=["apples", "bread", "milk", "eggs"]
# numbers = [1, 2, 3, 4, 5]
# mixed_items=["Alice", 25, True, 3.14]
# empty_cart=[]
# print(f"Shopping cart: {shopping_cart}")
# print(f"Numbers: {numbers}")
# print(f"Mixed items: {mixed_items}")

# # accessing the list items
# fruits=["apple", "banana", "cherry", "date", "elderberry"]
# print(f"The first fruit is: {fruits[0]}")
# print(f"The second fruit is: {fruits[1]}")
# print(f"The third fruit is: {fruits[2]}")
# print(f"The fourth fruit is: {fruits[3]}")


# print(f"First three fruits are: {fruits[0:3]}")
# print(f"First fruit till end: {fruits[0:5]}")
# print(f"Every second fruit: {fruits[::2]}")
# print(f"Second fruit till the end: {fruits[1:]}")
# print(f"Second to last fruit: {fruits[-2]}")
# print(f"Last fruit: {fruits[-1]}")

# # modifying the list
# groceries=["milk", "bread", "eggs"]
# print(f"Original List is: {groceries}")

# # adding a single item to the list
# groceries.append("cheese")
# print(f"After adding a single item, we have: {groceries}")

# # adding multiple items to the list
# groceries.extend(["apples", "bananas"])
# print(f"After adding more than one item, we have: {groceries}")

# # adding an item at a specific index
# groceries.insert(1, "yogurt")
# print(f"After adding \"Yogurt\" at point two, we have: {groceries}")

# # changing an existing item
# groceries[0]="Almond milk"
# print(f"After changing \"Milk\" to \"Almond Milk\" we have: {groceries}")


# # removing an item
# groceries.remove("bread")
# print(f"The list after removing bread: {groceries}")

# removed_item= groceries.pop()       #remove and return the last item
# print(f"Removed item: {removed_item}")  # this creates a holder for the removed item and displays it
# print(f"After popping: {groceries}")

# specific_item= groceries.pop(1)     #remove and return item at index one
# print(f"Removed item at index one: {specific_item}")
# print(f"Final List: {groceries}")



# # Sample list of test scores
# test_scores = [85, 92, 78, 96, 88, 79, 94]

# # Getting information about the list
# print(f"Number of scores: {len(test_scores)}")
# print(f"Highest score: {max(test_scores)}")
# print(f"Lowest score: {min(test_scores)}")
# print(f"Average score: {sum(test_scores) / len(test_scores):.1f}")

# # Checking if items exist
# print(f"Is 85 in the list? {85 in test_scores}")
# print(f"Is 100 in the list? {100 in test_scores}")

# # Counting occurrences
# grades = ["A", "B", "A", "C", "B", "A", "D"]
# print(f"Number of A's: {grades.count('A')}")

# # Finding the position of an item
# print(f"Position of first 'B': {grades.index('B')}")

# # Sorting (this changes the original list)
# test_scores.sort()
# print(f"Sorted scores: {test_scores}")

# # Sorting in descending order
# test_scores.sort(reverse=True)
# print(f"Scores (highest to lowest): {test_scores}")

# # Reversing the list
# test_scores.reverse()
# print(f"Reversed list: {test_scores}")

# # Using loops in lists
# # List of students
# students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# # Simple iteration
# print("Class roster:")
# for student in students:            # iterates through every item in the list
#     print(f"- {student}")           # prints the student name with a hyphen as prefix (hyphen then name)

# # Iteration with index numbers
# print("\nNumbered class roster:")
# for i, student in enumerate(students):      # the enumerate returns the item and its index 
#     print(f"{i + 1}. {student}")

# # Processing each item
# prices = [19.99, 25.50, 12.75, 33.20, 8.99]
# print("\nPrice list with tax:")
# for price in prices:
#     price_with_tax = price * 1.08
#     print(f"${price:.2f} -> ${price_with_tax:.2f}")         #prints both the original tax and the and the current price (original price * 1.08)

# # Creating new lists based on existing ones 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = []
# for num in numbers:
#     if num % 2 == 0:
#         even_numbers.append(num)

# print(f"Even numbers: {even_numbers}")

# # List comprehension - a compact way to create lists
# squares = [x**2 for x in range(1, 11)]
# print(f"Squares: {squares}")

# even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# print(f"Even squares: {even_squares}")


# # Todo list manager
# todo_list = []

# def add_task(task):
#     """Add a task to the todo list."""
#     todo_list.append(task)
#     print(f"Added: '{task}'")

# def complete_task(task):
#     """Mark a task as completed by removing it."""
#     if task in todo_list:
#         todo_list.remove(task)
#         print(f"Completed: '{task}'")
#     else:
#         print(f"Task '{task}' not found in the list")

# def show_tasks():
#     """Display all pending tasks."""
#     if todo_list:
#         print("Your tasks:")
#         for i, task in enumerate(todo_list, 1):
#             print(f"{i}. {task}")
#     else:
#         print("No tasks pending. Great job!")

# # Using the todo list
# add_task("Buy groceries")
# add_task("Write Python code")
# add_task("Call mom")
# show_tasks()

# complete_task("Buy groceries")
# show_tasks()

# # Grade tracker
# def calculate_class_statistics(grades):
#     """Calculate statistics for a class."""
#     if not grades:
#         return "No grades to analyze"

#     total = sum(grades)
#     count = len(grades)
#     average = total / count

#     # Count letter grades
#     letter_grades = []
#     for grade in grades:
#         if grade >= 90:
#             letter_grades.append("A")
#         elif grade >= 80:
#             letter_grades.append("B")
#         elif grade >= 70:
#             letter_grades.append("C")
#         elif grade >= 60:
#             letter_grades.append("D")
#         else:
#             letter_grades.append("F")

#     return {
#         "average": average,
#         "highest": max(grades),
#         "lowest": min(grades),
#         "total_students": count,
#         "letter_grades": letter_grades
#     }

# # Example usage
# class_grades = [85, 92, 78, 96, 88, 79, 94, 87, 91, 83]
# stats = calculate_class_statistics(class_grades)
# print(f"Class average: {stats['average']:.1f}")
# print(f"Grade range: {stats['lowest']} - {stats['highest']}")
# print(f"Letter grades: {stats['letter_grades']}") 

# Exercise 1
# Favorite movie manager
favorite_movies = []

def add_movie(movie):
    """Add a movie to the favorites list."""
    # Your code here
    
    favorite_movies.append(movie)
    print(f"Added movie: {movie}")

def remove_movie(movie):
    """Remove a movie from favorites."""
    # Your code here
    
    if movie in favorite_movies:
        favorite_movies.remove(movie)
        print(f"Finished watching the movie: {movie}")
    else:
        print(f"No movie: \"{movie}\" found in favorites")

def show_movies():
    """Display all favorite movies."""
    if favorite_movies:
        print("Your movies: ")
        for i, movie in enumerate(favorite_movies, 1):
            print(f"{i}. {movie}")
    else:
            print("All movies watched. Good job!")

# Test your functions
add_movie("The Matrix")
add_movie("Inception")
add_movie("Pulp Fiction")
show_movies()
remove_movie("Inception")
show_movies()

# Exercise 2
# Number analyzer
def analyze_numbers(numbers):
    """Analyze a list of numbers and return statistics."""
    # Your code here
    # Return a dictionary with: sum, average, min, max, even_count, odd_count
    pass

# Test your function
test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = analyze_numbers(test_numbers)
print(result)
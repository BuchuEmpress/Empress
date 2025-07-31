# Simply sets are a collection of items  cos ou can have a mixed set
# sets are special containers that automatically prevent duplicates. They ensure uniqueness
# Sets are perfect when you need to ensure all items are unique or when you want to perform mathematical 


# operations like finding common elements between groups
# Creating sets - like building unique collections
# unique_numbers = {1, 2, 3, 4, 5}
# colors = {"red", "blue", "green", "yellow"}
# mixed_set = {1, "hello", 3.14, True}

# # Creating sets from lists (removes duplicates automatically)
# numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
# unique_numbers_from_list = set(numbers_with_duplicates)

# # Empty set (note: {} creates an empty dictionary, not set)
# empty_set = set()

# print(f"Unique numbers: {unique_numbers}")
# print(f"Colors: {colors}")
# print(f"From list with duplicates: {unique_numbers_from_list}")
# print(f"Empty set: {empty_set}")



# # Set operations
# # Student enrollment in different courses
# python_students = {"Alice", "Bob", "Charlie", "Diana"}
# java_students = {"Bob", "Charlie", "Eve", "Frank"}
# javascript_students = {"Charlie", "Diana", "Eve", "Grace"}

# # Union - students taking ANY programming course
# all_programming_students = python_students | java_students | javascript_students
# print(f"All programming students: {all_programming_students}")

# # Intersection - students taking BOTH Python AND Java
# python_and_java = python_students & java_students
# print(f"Students taking both Python and Java: {python_and_java}")

# # Difference - students taking Python but NOT Java
# python_only = python_students - java_students
# print(f"Students taking Python but not Java: {python_only}")

# # Symmetric difference - students taking Python OR Java but not both
# python_xor_java = python_students ^ java_students
# print(f"Students taking Python or Java but not both: {python_xor_java}")



# # Modifying sets
# # Starting with a basic set of skills
# my_skills = {"Python", "JavaScript", "HTML"}
# print(f"Initial skills: {my_skills}")

# # Adding single skills
# my_skills.add("CSS")
# my_skills.add("React")
# my_skills.add("Angular")
# print(f"After learning CSS and React: {my_skills}")

# # Adding multiple skills at once
# new_skills = {"Node.js", "MongoDB", "Docker"}   # create a new set to add the skills you're currently adding
# my_skills.update(new_skills)                     # add the new set containing new items
# print(f"After bootcamp: {my_skills}")

# # Removing skills (maybe you forgot some!)
# my_skills.remove("HTML")  # Raises error if not found
# print(f"After forgetting HTML: {my_skills}")
# my_skills.remove("React")
# print(f"After for react: { my_skills}")

# # Safer removal (won't raise error if not found)
# my_skills.discard("PHP")  # Won't cause error even though PHP isn't in the set
# print(f"After trying to remove PHP: {my_skills}")

# # Removing and returning an arbitrary/random element
# removed_skill = my_skills.pop()
# print(f"Randomly removed skill: {removed_skill}")
# print(f"Remaining skills: {my_skills}")



# -------------------------------------------------------------------------------------------------
# Practical set example
# Email subscription management
def manage_email_subscriptions():
    """Manage different email subscription lists."""
    newsletter_subscribers = {"alice@email.com", "bob@email.com", "charlie@email.com"}
    promotion_subscribers = {"bob@email.com", "diana@email.com", "eve@email.com"}

    # Find subscribers who get both newsletters and promotions
    both_subscriptions = newsletter_subscribers & promotion_subscribers
    print("--" * 50)
    print(f"Subscribers getting both: {both_subscriptions}")

    # Find all unique subscribers
    all_subscribers = newsletter_subscribers | promotion_subscribers
    print(f"All subscribers: {all_subscribers}")

    # Find newsletter-only subscribers
    newsletter_only = newsletter_subscribers - promotion_subscribers
    print(f"Newsletter only: {newsletter_only}")

    return all_subscribers

# Word uniqueness checker
def find_unique_words(text1, text2):
    """Find unique words in two texts."""
    # Convert to lowercase and split into words
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    # Clean up punctuation
    words1 = {word.strip(".,!?;:") for word in words1}
    words2 = {word.strip(".,!?;:") for word in words2}

    # Find common words
    common_words = words1 & words2

    # Find unique words in each text
    unique_to_text1 = words1 - words2
    unique_to_text2 = words2 - words1

    return {
        "common": common_words,
        "unique_to_first": unique_to_text1,
        "unique_to_second": unique_to_text2
    }

# Test the word analyzer
text1 = "Python is a great programming language for beginners"
text2 = "Java is also a popular programming language for developers"

word_analysis = find_unique_words(text1, text2)
print("Word Analysis:")
print(f"Common words: {word_analysis['common']}")
print(f"Unique to first text: {word_analysis['unique_to_first']}")
print(f"Unique to second text: {word_analysis['unique_to_second']}")

# Inventory system using sets
def track_inventory_categories():
    """Track different categories of products in inventory."""
    electronics = {"laptop", "phone", "tablet", "headphones"}
    discounted_items = {"laptop", "book", "shirt", "headphones"}
    popular_items = {"phone", "book", "laptop", "shoes"}

    # Find electronics that are on discount
    discounted_electronics = electronics & discounted_items
    print(f"Discounted electronics: {discounted_electronics}")

    # Find popular electronics
    popular_electronics = electronics & popular_items
    print(f"Popular electronics: {popular_electronics}")

    # Find all product categories
    all_products = electronics | discounted_items | popular_items
    print(f"All products: {all_products}")

manage_email_subscriptions()
track_inventory_categories()
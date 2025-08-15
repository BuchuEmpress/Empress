# grade_book.py

# Student grade book system
grade_book = {}

# function to add new student
def add_new_student(name):
    if not name:              #check if user entered name
        return "Please enter a student name."
    if name not in grade_book:            #add name if name doesn't already exist
        grade_book[name] = []  # initialize empty grade list for new student
        return f"Added student: {name}"
    else:
        return f"The name '{name}' already exists."

# function to add grades to an existing student
def add_grade_to_existing_student(name, grade_list):
    if name in grade_book:                 #check if name eists
        grade_book[name].extend(grade_list)               # add grades/scores to current stuent's grade list
        return f"Grades {grade_list} added to {name}."
    else:
        return f"Name '{name}' is not in grade book."

# function to calculate average for a student
def calculate_average(name):
    if name in grade_book and grade_book[name]:         #ensures student already exists and has grades recorded
        grades = grade_book[name]                        #get student's grades
        total = sum(grades)                               # sum up all those grades
        average = total / len(grades)                      #calculate average
        return average
    else:
        return None

# function to get letter grade for a score
def get_letter_grades(score):
     if score > 89:
            return  "A+"
     elif score > 79 and score < 90:
            return  "B"
     elif score > 69 and score < 80:
            return  "c"
     elif score > 59 and score < 70 :
            return  "D"
     else:
            return "F"

# function to calculate all letter grades for a student
def calculate_letter_grades(name):
    if name in grade_book:                   
        grades = grade_book[name]                     #checks list of grades
        return [get_letter_grades(score) for score in grades]           # convert each score to letter grade using list comprehension
    else:
        return []                                                       # if student is not found, return an empty list

# function to display a specific student's info
def display_student(name):
    if name in grade_book:
        scores = grade_book[name]              # get the student's scores
        if not scores:                         # if no scores were recorded-->
            return f"{name}: Has no scores recorded."
        letter_grades = calculate_letter_grades(name)   #get the letter grades for each score
        average = calculate_average(name)               # get the average score
        return {                                        # return all details for that student in a dictionary form
            "Name": name,
            "Scores": scores,
            "Letter Grades": letter_grades,
            "Average": round(average, 2)                #round average to 2 decimal places
        }
    else:
        return f"Student '{name}' not found."

# function to display all students' info
def display_all_students():
    if not grade_book:                   # if no student exists
        return "Grade book is empty."
    all_students = []                    # list all student info dictionaries
    for name in grade_book:              # loop through all students
        info = display_student(name)      # get the student details using the display_student() function
        if isinstance(info, dict):        # ensure the returned dats is a dictionary
            all_students.append(info)     # add to list
    return all_students                    # return list of all students

# function to find highest and lowest ranked students
def find_highest_and_lowest_rank_student():
    student_averages = {}                    # dictionary to hold students' names and average scores
    for name in grade_book:                  # loop through each student
        avg = calculate_average(name)        # calculate the student's average score
        if avg is not None:                  # only add if grades/marks are present
            student_averages[name] = avg     # store average in dictionary

    if student_averages:                     # if there's at least one student with grades
        overall_average = sum(student_averages.values()) / len(student_averages)                # calculate average of all students' averages
        top_student = max(student_averages, key=student_averages.get)                           # student with highest average
        bottom_student = min(student_averages, key=student_averages.get)                        # student with lowest
        return {                                                                                # return all results in a dictionary
            "Overall Average": round(overall_average, 2),
            "Top Student": (top_student, round(student_averages[top_student], 2)),
            "Lowest Student": (bottom_student, round(student_averages[bottom_student], 2))
        }
    else:
        return "No students have recorded averages."
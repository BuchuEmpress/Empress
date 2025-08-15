import streamlit as st
import sys

# Import backend functions
# sys.path.insert(0, '../')
from sup.exercise_1.student_gradebook import (
    add_new_student,
    add_grade_to_existing_student,
    calculate_average,
    display_student,
    display_all_students,
    find_highest_and_lowest_rank_student
)

st.title("📚 Grade Book Application")

# Menu
menu = [
    "Add Student",
    "Add Grades",
    "Calculate Average",
    "Display Student",
    "Display All Students",
    "Find Highest and Lowest Rank Student"
]
choice = st.selectbox("Select an option", menu)

# Add Student
if choice == "Add Student":
    name = st.text_input("Enter student name")
    if st.button("Add Student"):
        result = add_new_student(name)
        st.success(result)

# Add Grades
elif choice == "Add Grades":
    name = st.text_input("Enter student name")
    grades = st.text_input("Enter grades (comma-separated)")
    if st.button("Add Grades"):
        try:
            grade_list = [int(g.strip()) for g in grades.split(",") if g.strip().isdigit()]            # convert grades string to a list of integers, removing spaces
            result = add_grade_to_existing_student(name, grade_list)
            st.success(result)
        except ValueError:
            st.error("Please enter valid numeric grades separated by commas.")

# Calculate Average
elif choice == "Calculate Average":
    name = st.text_input("Enter student name")
    if st.button("Calculate Average"):
        average = calculate_average(name)
        if average is not None:
            st.info(f"Average for {name}: {average:.2f}")
        else:
            st.error("Student not found; hence grades/marks not recorded.")

# Display Student
elif choice == "Display Student":
    name = st.text_input("Enter student name")
    if st.button("Display Student"):
        result = display_student(name)
        if isinstance(result, dict):
            st.table([result])  # single student table
        else:
            st.warning(result)

# Display All Students
elif choice == "Display All Students":
    if st.button("Display All Students"):
        result = display_all_students()
        if isinstance(result, list) and result:
            st.table(result)  # multiple students table
        else:
            st.warning(result)

# Find Highest and Lowest Rank Student
elif choice == "Find Highest and Lowest Rank Student":
    if st.button("Find Highest and Lowest Rank Student"):
        result = find_highest_and_lowest_rank_student()
        if isinstance(result, dict):
            st.json(result)  # nicely formatted JSON view
        else:
            st.warning(result)




























































































































































































































# import streamlit as st
# from sup.exercise_1.student_gradebook import  add_new_student, add_grade_to_existing_student, calculate_average, calculate_letter_grades, display_student, display_all_students, find_highest_and_lowest_rank_student, des
# st.title("Grade Book Application")

# # create a grade book instance
# # grade_book = grade_book{}


# menu = ["Add Student", "Add Grades", "Calculate Average", "Display Student", "Display All Students", "Find Highest and Lowest Rank Student"]
# choice = st.selectbox("Select an option", menu)

# if choice == "Add Student":
#  name = st.text_input("Enter student name")
#  if st.button("Add Student"):
#      add_new_student(name)
#      st.success("Student added successfully")
     
# elif choice == "Add Grades":
#     name = st.text_input("Enter student name")
#     grades = st.text_input("Enter grades (comma-separated)")
#     if st.button("Add Grades"):
#         grade_list = [int(grade) for grade in grades.split(",")]
#         add_grade_to_existing_student(name, grade_list)
#         st.success("Grades added successfully")
        
# elif choice == "Calculate Average":
#     name = st.text_input("Enter student name")
#     if st.button("Calculate Average"):
#         average = calculate_average(name)
#         if average is not None:
#          st.write(f"Average: {average:.2f}")
#         else:
#             st.write("Student not found hence no grades recorded")

# elif choice == "Display Student":
#     name = st.text_input("Enter student name")
#     if st.button("Display Student"):
#         display_student(name)
        
# elif choice == "Display All Students":
#     if st.button("Display All Students"):
#         display_all_students()
        
# elif choice == "Find Highest and Lowest Rank Student":
#     if st.button("Find Highest and Lowest Rank Student"):
#         find_highest_and_lowest_rank_student()
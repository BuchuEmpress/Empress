# def read_simple_file():
#     """demostrate basic file reading______________"""
#     file=open("sample.txt", "r")            #to read the file
#     # print(f"here is the file i want to read___________: {file}")
#     content=file.read()
#     print(f"Here is the content of the file read: {content}")
#     file.close()
#     return content
# read_simple_file()  # calling the function     but this way is not really optimzed

# because you have to manually closethe file 
# incase you forget it'll use up space which not advantageous
# if something breaks it'll remain open. the with keyword solcves this problem

# def read_simple_text():
#     """"""
#     with open("sample.txt", "r") as file:
#         content=file.read()
#         print(f"Content is: {content}")
#         return content
# read_simple_text()  # always call your function and this method is best 

# a way to write the same code that would print an error message if the file asked for in not found
def read_simple_text():
    """"""
    filename="new_file.md"
    try:
        # opens the file read mode, with utf-8 encoding ; can add "errors='ignore'" to ignore any decoding errors
     with open(filename, "r", encoding='utf-8') as file: 
         #reads the entire content of the file into a string
        content=file.read()
        #returns the content of the file
        return content
    except FileNotFoundError:
        return "File not found, please try again"
 # to catch other exceptions that mau occur
    except Exception as e:
        #would return a error message with the specific exception details
        return f"An error occured: {e}"

# Using the function 
read_simple_text()
result=read_simple_text()
print(result)
 


# Reading file line by line
def line_by_line():
    """"""
    filename="to_be_created.txt"
    try:
     with open(filename, "r") as file:
         print("\n\nreading line by line")
         for i, line in enumerate(file,1):
             print(f"\n\nLine {i}:{line.strip()}")
    except FileNotFoundError:
        return "File not found, please try again"
line_by_line()
 

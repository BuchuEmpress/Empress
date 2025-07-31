# Prompt: please

# The computer would prompt "please let us know what you've learnt today"
#it would be a loop and keep promting until you type exit
# inside record.txt(file you'll create), you'll have today's date(from datetime import datetime
# datetime.now.strftime("%Y-%m-%d")    ; 'year - month  - day, time
# ) and the individual records e.g


# from datetime import datetime
# datetime.now.strftime("%Y-%m-%d")
# # current_time=datetime.now().strftime("%Y-%m-%d %H:%M")
# with open("record.text", "w") as file:
#     file.write("Welcome genai course") 

print("--" * 50)
print("Enter \"q\" to quit this environment")
print("--" * 50)


from datetime import datetime
filename="record.txt"
while True:
    user_input=input("\nTell us what you've learnt today\n")
    if user_input.strip().lower() == "q":
        print("End of session.")
        break
    current_time=datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(filename, "a") as file:
        file.write(f"- {current_time}: {user_input}\n")
        # info=f"- {current_time}: {user_input}"
        print(f"Saved your material: - {current_time}: {user_input}\n")
    # user_input + "\n"
     
    
    




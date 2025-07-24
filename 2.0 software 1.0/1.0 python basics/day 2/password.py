password=input("Enter your password")

lower_case=password.islower()
upper_case=password.isupper()
numeric=password.isdigit()
if lower_case and upper_case and numeric:
    print("This is a strong password.")
else:
    print("Please type a strong password")